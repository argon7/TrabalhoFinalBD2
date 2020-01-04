from flask import render_template, url_for, flash, redirect, request, abort
from flask_bcrypt import generate_password_hash

from app.forms import RegistrationForm, LoginForm, PostForm, TransacoesForm, ClientForm, ProductForm, MenuForm
from app import app, db, bcrypt
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
import psycopg2
from app import ps_connection, cursor

now = datetime.now()
import psycopg2


# ---------------------------- LOGIN/REGISTO/HOME ------------------------------------------
@app.route('/')
@app.route('/home')  # home / about --- é os dois
def home():
    return render_template("layout/home.html", title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))  # MUDAR ISTO DEPOIS...
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  # para ficar em string
        #user = User(username=form.username.data, email=form.email.data, password=hashed_password, restaurante=form.nome_restaurante.data)
        # ---------------------------commit to db REGISTO---------------
        try:
            cursor.callproc('createAdministrador', ['tttt', 'tettttste', 'testeqweqwettttqwe', 'Restaurante Quinta dos Barreiros'])
            result = cursor.fetchall()
            for column in result:
                print("result createAdministrador = ", column[0])
            #cursor.execute("SELECT * FROM Administrador;")
            #result=cursor.fetchall()
            #for column in result:
            #    print("check")
            #    print(column[0])
            #print()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            print("done")
        # -----------------------------------------------------------
        flash(f'Account created!', 'success')
        return redirect(url_for('login'))
    return render_template("layout/register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    thereisuser = False
    if form.validate_on_submit():
        # ---------------------------check for user in db---------------
        try:
            cursor.execute("SELECT * FROM Administrador;")
            result=cursor.fetchall()
            for column in result:

                if (form.email.data == column[3] and form.password.data == column[4]):
                    L_id = column[0]
                    L_nRestaurante = column[1]
                    L_email = column[3]
                    L_pass = column[4]
                    thereisuser = True


        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            print("done")

        if (thereisuser):
            user = User(int(L_id),L_email,
                        generate_password_hash(L_pass),L_nRestaurante )

            login_user(user, remember=form.remember.data)  # login do user e guarda o remember
            return redirect(url_for('tab_transacoes'))
        else:
            flash(f'Login unsuccessful', 'danger')
    return render_template("layout/login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


# ---------------------------- Transações ------------------------------------------
@app.route("/tab_transacoes")
@login_required
def tab_transacoes():
    posts = Post.query.all()
    return render_template('transacoes/tab_transacoes.html', posts=posts, title="Transações")


@app.route("/new_transacoes", methods=['GET', 'POST'])
@login_required
def new_transacoes():
    form = TransacoesForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user, date_posted=now)
        db.session.add(post)
        db.session.commit()
        flash(f'Done!', 'success')
        return redirect(url_for('tab_transacoes'))
    return render_template('transacoes/new_transacoes.html', title="Nova Transação", form=form,
                           legend='Registar a nova transação')


@app.route("/tab_transacoes/<int:post_id>")
@login_required
def transacoes(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('transacoes/transacoes.html', title=post.title, post=post)


@app.route("/tab_transacoes/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_transacoes(post_id):  # cant have same function name
    form = TransacoesForm()
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    if form.validate_on_submit():
        post.content = form.content.data
        post.title = form.content.data
        db.session.commit()  # nao faz sentido colocar add() pq ja existe na db, so vale a pena fazer commit para mudar
        flash(f'Changes were updated successfully', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('transacoes/new_transacoes.html', title="Update Transação", form=form,
                           legend='Update Transação')


@app.route('/transacoes/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_transacoes(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Delete successfull', 'info')
    return redirect(url_for('transacoes/tab_transacoes'))


# ---------------------------- Clientes ------------------------------------------


@app.route("/tab_client")
@login_required
def tab_client():
    posts = Post.query.all()
    return render_template('client/tab_client.html', posts=posts, title="Clientes")


@app.route("/new_client", methods=['GET', 'POST'])
@login_required
def new_client():
    form = ClientForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user, date_posted=now)
        db.session.add(post)
        db.session.commit()
        flash(f'Done!', 'success')
        return redirect(url_for('tab_client'))
    return render_template('client/new_client.html', title="Novo Cliente", form=form, legend='Registar novo cliente')


# ---------------------------- Ementa --------------------------------------------


@app.route("/tab_menu")
@login_required
def tab_menu():
    posts = Post.query.all()
    return render_template('menu/tab_menu.html', posts=posts, title="Ementas")


@app.route("/new_menu", methods=['GET', 'POST'])
@login_required
def new_menu():
    form = MenuForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user, date_posted=now)
        db.session.add(post)
        db.session.commit()
        flash(f'Done!', 'success')
        return redirect(url_for('tab_menu'))
    return render_template('menu/new_menu.html', title="Nova Ementa", form=form, legend='Criar nova Ementa')


# ---------------------------- Produtos ------------------------------------------


@app.route("/tab_product")
@login_required
def tab_product():
    posts = Post.query.all()
    return render_template('product/tab_product.html', posts=posts, title="Produtos")


@app.route("/new_product", methods=['GET', 'POST'])
@login_required
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user, date_posted=now)
        db.session.add(post)
        db.session.commit()
        flash(f'Done!', 'success')
        return redirect(url_for('tab_product'))
    return render_template('product/new_product.html', title="Novo produto", form=form, legend='Registar novo produto')


# ---------------------------- + TESTES ------------------------------------------
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
    return render_template('testes/create_post.html', title="New Post", form=form, legend='New Post')


@app.route("/post/<int:post_id>")
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('testes/post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):  # cant have same function name
    form = PostForm()
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    if form.validate_on_submit():
        post.content = form.content.data
        post.title = form.content.data
        db.session.commit()  # nao faz sentido colocar add() pq ja existe na db, so vale a pena fazer commit para mudar
        flash(f'Changes were updated successfully', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('testes/create_post.html', title="Update Post", form=form, legend='Update Post')


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


@app.route("/dashboard")
@login_required
def dashboard():
    posts = Post.query.all()
    return render_template('testes/dashboard.html', posts=posts, title="Account")
