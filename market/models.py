
from market import db
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



