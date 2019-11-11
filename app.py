from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = '76d5f16cf6bb57be0bd6851a8c61df1d'  # secret key for security

#DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #path da db
db = SQLAlchemy(app) #instancia da db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title},{self.date_posted}')"




posts = [
    {
        'author': 'corey taylor',
        'band': 'slipknot',
        'content': 'nu metal',
        'date': 'april'
    },
    {
        'author': 'taylor momsen',
        'band': 'pretty reckless',
        'content': 'metal',
        'date': 'june'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts, title='itworks')  # we have access to post in the template


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'admin':
            flash(f'Login done!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful','danger')
    return render_template("login.html", title='Login', form=form)


if __name__ == '__main__':
    app.run()
