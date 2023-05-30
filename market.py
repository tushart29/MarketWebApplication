from flask import Flask, render_template

#inialize the instance of Flask
# __name__ refering to local file your working with
app = Flask(__name__)

# what url do you want to navigate to
@app.route('/')
def home_page():
    return render_template('home.html')


# bootstrap - https://getbootstrap.com/docs/4.5/getting-started/introduction/

