from market import app
from flask import render_template
from market.models import Item
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

