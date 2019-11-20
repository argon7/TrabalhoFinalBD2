from flask import render_template, url_for, flash, redirect, request
from app.forms import RegistrationForm, LoginForm
from app import app, db, bcrypt
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    return render_template("home.html", title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))  # MUDAR ISTO DEPOIS...
    form = RegistrationForm()
    if form.validate_on_submit():
        # hash password and create user
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  # para ficar em string
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
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
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)  # login do user e guarda o remember
            next_page = request.args.get('next')  # get method melhor que brackets
            # O replace foi usado pq next guardava "/account" e nao "account"...  e depois nao localizava os templates
            # soluçao estupida, mas dá ... e por definição se dá não é estupida :)
            return redirect(url_for(next_page.replace('/', ''))) if next_page else redirect(url_for('dashboard'))
        else:
            flash(f'Login unsuccessful', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', posts=posts,  title="Account")


@app.route("/post/new")
@login_required
def new_post():
    return render_template('create_post.html', title="New Post")
