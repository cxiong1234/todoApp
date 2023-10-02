from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cxiong:13031122098@localhost:5432/todoapp'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class Todo(db.Model): ## This is child model
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolist.id'), nullable=False)   ##todolist is the parent table name and id is the primary key it refer to 
                                                                ##by default the nullable is False, we just want show here to be clear.
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

class TodoList(db.Model):  ## this is parent model
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todo = db.relationship('Todo', backref='todo_list', lazy=True)  ##where the 'Todo' just refer to the Todo child model and 'todo_list' is customized name of the parent table dotolist



with app.app_context():
    db.create_all()

@app.route('/todo/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        list_id = request.get_json()['list_id']
        todo = Todo(description=description, completed=False, list_id = list_id)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['completed'] = todo.completed
        body['description'] = todo.description
    
    except:
        error = True
        db.session.rollback()
        print("###############")
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)
    else:
        abort(400)


@app.route('/todo/<todo_id>/set-complete', methods=['POST'])
def update_todo(todo_id):
    error = False
    try:
        complete = request.get_json()['complete']
        todo = Todo.query.get(todo_id)
        todo.complete = complete
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:
        return redirect(url_for('index'))


@app.route('/todo/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    error = False
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        print('Todo: ', todo)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(500)
    else:    
        return '', 200




@app.route('/todo/<todo_id>/delete', methods = ['DELETE'])
def delete_todo(todo_id):
    error = False
    try:
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
    if not error:
        return jsonify({'success': True})
        
    else:
        abort(500)

@app.route('/lists/<list_id>')
def get_list_todo(list_id):   ##this function is route handler


    return render_template('index.html',
                           lists = TodoList.query.all(),
                           active_list = TodoList.query.get(list_id), 
                           todo=Todo.query.filter_by(list_id=list_id).order_by('id').all())


@app.route('/')
def index():
    return redirect(url_for('get_list_todo', list_id = 1))
 
@app.route('/lists/create', methods=['POST'])
def creat_list():
    error = False
    body = {}
    try:
        name = request.get_json()['name']
        todolist = TodoList(name= name)
        db.session.add(todolist)
        db.session.commit()
        body['id'] = todolist.id
        body['name'] = todolist.name
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info)
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)

@app.route('/lists/<list_id>/delete', methods=['DELETE'])
def delete_list(list_id):
    error = False
    try:
        list = TodoList.query.get(list_id)
        for a_todo in list.todo:
            db.session.delete(a_todo)
        db.session.delete(list)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
    if not error:
        return jsonify({'success': True})
        
    else:
        abort(500)

@app.route('/lists/<list_id>/set-listcompleted', methods=['POST'])
def set_completed_list(list_id):
    error = False

    try:

        
        list = TodoList.query.get(list_id)
        
        for todo in list.todo:
            todo.completed = True
        db.session.commit()
    
    except:
        print("########Error########")
        try:
            list = TodoList.query.get(list_id)
        except Exception as e:
            print(f"Error: {e}")
            abort(400, description="Invalid input")





        db.session.rollback()
        error = True
    finally:
        db.session.close()
    
    if not error:
        return '' , 200

    else:
        abort(500)    


