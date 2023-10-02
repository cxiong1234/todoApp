# todoApp

This app leveraged the PostgreSQL ralational database and built up the Todo List, users can Create/Delete/Modify the todo List as well as the todo item inside a specific list.

### Please see the demo of our App:
![Screen_Recording_2023-10-02_at_10 52 26_AM_V1](https://github.com/cxiong1234/todoApp/assets/62785993/5f75e511-d2a0-47b5-b8fc-49ad3714af35)


### Initial Setup:
1. install the PostGreSQL. Please follow the tutorial (https://commandprompt.com/education/how-to-install-postgresql-on-macos/) that just download the package and follow the guide line.
2. start the PostGreSQL on mac. (I'm using the MacOS Monterey with M1 chip)
```
brew services start postgresql
```
3. Install the dependency lib. I'm using the anaconda environment. (make sure you've already have conda installed https://docs.anaconda.com/free/anaconda/install/mac-os/)

```
## create a new environment for todoapp
conda create --name todoappEnv
conda activate todoappEnv
```
```
##install FLASK
conda install -c conda-forge flask
##install FLASK-SQLAlchemy
conda install -c conda-forge flask-sqlalchemy
##install Flask-Migrate
conda install -c conda-forge flask-migrate
```


