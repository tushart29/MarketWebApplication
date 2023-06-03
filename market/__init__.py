from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
#inialize the instance of Flask
# __name__ refering to local file your working with
app = Flask(__name__)



# Get the absolute path to the current directory
base_dir = os.path.abspath(os.path.dirname(__file__))

# Set the path to the database file inside the "market" folder
db_path = os.path.join(base_dir, 'market.db')


# do this below so that the flask can know that there is a database
# we used the flask object, and added extra configuration so that flask can recongize this database.
# convention is to create a key, SQLALCHEMY_DATABASE_URI (Uniform Resource Identifier).
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

app.config['SECRET_KEY'] = '1445fb114aff23559e3ee8b0'



# this is our database instance
# we can start creating our classes, later on it will be converted into modules, database table.
db = SQLAlchemy(app)


# do this so routes can recongnize the routes you created
from market import routes





