
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#inialize the instance of Flask
# __name__ refering to local file your working with
app = Flask(__name__)

# do this below so that the flask can know that there is a database
# we used the flask object, and added extra configuration so that flask can recongize this database.
# convention is to create a key, SQLALCHEMY_DATABASE_URI (Uniform Resource Identifier).
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# this is our database instance
# we can start creating our classes, later on it will be converted into modules, database table.
db = SQLAlchemy(app)


# informs flask that this is a module that will be a table inside a database
class Item(db.Model):


    # this next one is a convention when created a flask modules
    # if not there, would get sqlalchemy.exc.ArgumentError
    id = db.Column(db.Integer(), primary_key=True)

    # can't describe a name more than 30 characters
    # don't want to have null fields - first argument
    # allows our name to not have the same in the database
    name = db.Column(db.String(length=30), nullable=False,unique = True )
    price = db.Column(db.Integer(), nullable = False)
    barcode = db.Column(db.String(length=12), nullable = False, unique = True)
    description = db.Column(db.String(length=1000), nullable = False, unique = True)

    # this function allows you to see the item by name in the database instead of the default ID flask gives
    def __repr__(self):
        return f'Item {self.name}'






# what url do you want to navigate to
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
# trying to send random data from this route to html. trying to see how I can access it
def market_page():
    # stores all the items we stored in the database can be accessed through line 54
    items = Item.query.all()
    return render_template('market.html', items = items)
    # we can access this key name, item_name, by using the Jinja web template  we got from flask




# bootstrap - https://getbootstrap.com/docs/4.5/getting-started/introduction/





