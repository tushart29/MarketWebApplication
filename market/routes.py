from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User

from market.forms import RegisterForm, LoginForm
from market import db


# what url do you want to navigate to
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
# trying to send random data from this route to hstml. trying to see how I can access it
def market_page():
    # stores all the items we stored in the database can be accessed through line 54
    items = Item.query.all()
    return render_template('market.html', items = items)
    # we can access this key name, item_name, by using the Jinja web template  we got from flask


# the list methods is there so that the routes can handle post requests
@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    # this if statement verifys that they will be executed when submit button is clicked
    # this if statement checks certain requirements before submit such as passowrd matching
    if form.validate_on_submit():
        # only code where we create instances of the User
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        # password = form.password1.data) this line of code goes to password.setter decorator
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: # if no errors from validation
        print("Form errors:", form.errors)
        for err_msg in form.errors.values():
            flash(f'There was an error in creating users: {err_msg}', category='danger')
        # this return statement will send users right to the market_page method

    return render_template('register.html', form = form)
    # the information that we want to send to the template


@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)


# bootstrap - https://getbootstrap.com/docs/4.5/getting-started/introduction/

