# todoApp

This app leveraged the PostgreSQL ralational database and built up the Todo List, users can Create/Delete/Modify the todo List as well as the todo item inside a specific list.

### Please see the demo of our App:
![Screen_Recording_2023-10-02_at_10 52 26_AM_V1](https://github.com/cxiong1234/todoApp/assets/62785993/5f75e511-d2a0-47b5-b8fc-49ad3714af35)


### Introduction:
This application leveraged the Model View Controller(MVC) architecture for managing the web application. See the picture below for detailed relationships of the three layers:
#### Model Layer:
This layer manage data model like tables for us.this layer capture the logical relationships between tables models and objects.
#### Controller Layer:
Serve as the router, also sontrol how commands are sent to other two layers also control how the Model layer and view layer how to interact with each other.
#### View Layer:
This layer hanle how do we represent the web page. This the basically our front end written by (HTML, CSS, JS).




![alt text](https://github.com/cxiong1234/todoApp/assets/62785993/5197f054-f3e2-46dd-9c14-9928e46383b3)

<br\>
The App also implemented the CRUD (CREATE, READ, UPDATE, DELETE) operations of the database and can be used to handle and map the relationships between different tables by the [SQL Joins](https://www.w3schools.com/sql/sql_join.asp).


### Initial Setup:
1. install the PostGreSQL. Please follow [this tutorial](https://commandprompt.com/education/how-to-install-postgresql-on-macos/) that just download the package and follow the guide line.
2. start the PostGreSQL on mac. (I'm using the MacOS Monterey with M1 chip)
3. open your terminal:
```
brew services start postgresql
```
4. Install the dependency lib. I'm using the anaconda environment. (make sure you've already have conda installed via the [Anaconda official website](https://docs.anaconda.com/free/anaconda/install/mac-os/))

```
## create a new environment for todoapp
conda create --name todoappEnv
conda activate todoappEnv
```

```
##install FLASK
conda install -c conda-forge flask
##install psycopg2
conda install -c conda-forge psycopg2
##install FLASK-SQLAlchemy
conda install -c conda-forge flask-sqlalchemy
##install Flask-Migrate
conda install -c conda-forge flask-migrate
```
5. Adding the anaconda PATH to your $PATH, we utilize the anaconda environment as first priority.
```
export PATH=~/anaconda3/bin:$PATH
source ~/.zshrc
```
6. Go to your app.py folder and Run the web application:
```
cd /<your>/<app>/<folder>/   
export FLASK_APP=app.py  ## where app.py is the name of our application
FLASK_APP=app.py FLASK_DEBUG=true flask run
```
