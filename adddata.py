from app import app, db, TodoList, Todo

with app.app_context():
    list = TodoList(name='Urgent2')
    db.session.add(list)
    db.session.commit()

    todo = Todo(description="This is important", completed= False)
    todo2 = Todo(description="This is important, also", completed = False)
    todo3 = Todo(description="urgent todo 2", completed = False)

    todo.todo_list = list
    todo2.todo_list = list
    todo3.todo_list = list

    db.session.add_all([todo, todo2, todo3])
    db.session.commit()
