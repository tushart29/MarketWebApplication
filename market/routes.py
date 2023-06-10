from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user


# what url do you want to navigate to
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market',methods=['GET','POST'])
# the line below is responsible for taking the users to the login page
@login_required
# trying to send random data from this route to hstml. trying to see how I can access it
def market_page():
    # stores all the items we stored in the database can be accessed through line 54
    purhcase_form = PurchaseItemForm()

    selling_form = SellItemForm()
    # the below if statement is like the form.validate.on_submit method from flask.
    # the below if statement, takes away the form resumbssion error
    if request.method == 'POST':

        # purchase item logic
        purchased_item = request.form.get('purchased_item')
        # to inspect the item object, you have to call .first()
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Purchased {p_item_object.name} successfully for {p_item_object.price}", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase this  {p_item_object.name}", category='danger')
        # we have to send users to this page, once the purchase is done

        # sell item logic
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name} back to market!", category='success')
            else:
                flash(f"Something went wrong with selling {s_item_object.name}", category='danger')



        return redirect(url_for('market_page'))
    if request.method == "GET":
        # shows only the items where the item is not associated with the owner which means its avaliable
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items = items, purhcase_form =purhcase_form, owned_items = owned_items, selling_form=selling_form )
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
        login_user(user_to_create)
        flash(f'Account created Successfully. Your now logged in as: {user_to_create.username} ', category='success')
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
    if form.validate_on_submit():
        # first check if user exists
        # filters out the username by the provided username
        # .first grabs the object of that user
        # second, if user does exit, then if password is actually the correct as the user
        attempt_user = User.query.filter_by(username=form.username.data).first()
        if attempt_user and attempt_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempt_user)
            flash(f'Successfully Logged in as: {attempt_user.username} ', category='success')
            return redirect(url_for('market_page'))
        else:
            # danger displays red color message. Also, danger will be translated to base template has danger message
            flash(f'Username and password are not matching. Please try again !', category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    # enough to grab the current user and log out
    logout_user()
    flash('Logged Out Successfully',category='info')
    return redirect(url_for('home_page'))
# bootstrap - https://getbootstrap.com/docs/4.5/getting-started/introduction/

