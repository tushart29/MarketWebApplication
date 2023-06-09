import bcrypt

from market import db, login_manager
from market import bcrypt
# informs flask that this is a module that will be a table inside a database
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# you can access Bcrypt since you already did it in init file

# below are MODULES User and Item

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable = False ,unique=True)
    email_address = db.Column(db.String(length=50),nullable = False, unique=True)

    # hash the password for security purposes
    password_hash = db.Column(db.String(length=60), nullable = False)
    budget = db.Column(db.Integer(), nullable = False, default = 1000)


    items = db.relationship('Item', backref='owned_user', lazy = True)

    @property
    def nice_budget(self):
        if len(str(self.budget)) >= 4:
            return f'${str(self.budget)[:-3]}, {str(self.budget)[-3:]}'
        else:
            return f"$ {self.budget}"
    #additional atrribute that will be accessable for each instance
    @property
    def password(self):
        return self.password


    @password.setter
    def password(self, plain_password_setter):

        self.password_hash = bcrypt.generate_password_hash(plain_password_setter).decode('utf-8')

    def check_password_correction(self, attempted_password):
        # this function will accept the pasword that is hashed and the passowrd from the form
        # execute this function and return the value if the hashed passowrd is equal to the orginal password
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price
    def can_sell(self, item_obj):

        # at the top we have all the items, in the user class
        # so using this, we will check if this item object is in the user inventory, then we can sell if this is true in the routes.py
        return item_obj in self.items


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
    def buy(self, user):
        # associates the item with the owner in the database
        self.owner = user.id
        user.budget -= self.price
        # saves the operation to the databsase
        db.session.commit()

    def sell(self, user):
        # un-associates the item with the owner in the database
        self.owner = None
        user.budget += self.price
        # saves the operation to the databsase
        db.session.commit()



