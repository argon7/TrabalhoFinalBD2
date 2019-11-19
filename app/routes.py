from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm
from app import app, db, bcrypt
from app.models import User,Post

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
        # hash password and create user
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # .decode('utf-8') para ficar em string
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # inform user
        # aqui devia ser o admin a adicionar o user?
        flash(f'Account created!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'admin':
            flash(f'Login done!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful', 'danger')
    return render_template("login.html", title='Login', form=form)
