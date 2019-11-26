from flask import render_template, url_for, flash, redirect, request, abort
from app.forms import RegistrationForm, LoginForm, PostForm
from app import app, db, bcrypt
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
now = datetime.now()


# posts = [
#    {
#        'author': 'corey taylor',
#        'band': 'slipknot',
#        'content': 'nu metal',
#        'date': 'april'
#   },
#    {
#        'author': 'taylor momsen',
#        'band': 'pretty reckless',
#        'content': 'metal',
#        'date': 'june'
#    }
# ]


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
    posts=Post.query.all()
    return render_template('dashboard.html', posts=posts,  title="Account")


@app.route("/tab_transacoes")
@login_required
def tab_transacoes():
    return render_template('tab_transacoes.html', title="tab_transacoes")


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user, date_posted=now)
        db.session.add(post)
        db.session.commit()
        flash(f'Done!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_post.html', title="New Post", form=form, legend='New Post')


@app.route("/post/<int:post_id>")
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id): # cant have same function name
    form = PostForm()
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    if form.validate_on_submit():
        post.content = form.content.data
        post.title = form.content.data
        db.session.commit() # nao faz sentido colocar add() pq ja existe na db, so vale a pena fazer commit para mudar
        flash(f'Changes were updated successfully', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title="Update Post", form=form, legend='Update Post')


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Delete successfull', 'info')
    return redirect(url_for('dashboard'))
