
from market import db
# informs flask that this is a module that will be a table inside a database

# below are MODULES User and Item

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable = False ,unique=True)
    email_address = db.Column(db.String(length=50),nullable = False, unique=True)

    # hash the password for security purposes
    password_hash = db.Column(db.String(length=60), nullable = False)
    budget = db.Column(db.Integer(), nullable = False, default = 1000)


    items = db.relationship('Item', backref='owned_user', lazy = True)

    # backref is a back reference for the user module
    # Allows us to see the owner of the specfic item
    # lazy  = True allows you to grab all the items in one shot



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

    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    # related to the unique row at ID
    # foreign key will be related to the other module primary key
    # this function allows you to see the item by name in the database instead of the default ID flask gives
    def __repr__(self):
        return f'Item {self.name}'



