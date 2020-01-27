from flask import render_template, url_for, flash, redirect, request, abort
from app.forms import RegistrationForm, LoginForm, PostForm, TransacoesForm, ClientForm, ProductForm, MenuForm
from app import app
from datetime import datetime
import psycopg2
from app import ps_connection, cursor
now = datetime.now()
import psycopg2

IsUserLoggedIn = False


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


# ---------------------------- LOGIN/REGISTO/HOME ------------------------------------------
@app.route('/')
@app.route('/home')  # home / about --- é os dois
def home():
    return render_template("layout/home.html", title='Home',IsUserLoggedIn=IsUserLoggedIn)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
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
    return render_template("layout/register.html", title='Register', form=form,IsUserLoggedIn=IsUserLoggedIn)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global IsUserLoggedIn
    form = LoginForm()
    thereisuser = False
    passwordmatch = False
    if form.validate_on_submit():
        # ---------------------------check for user in db---------------
        try:
            cursor.execute("SELECT * FROM Administrador;")
            result=cursor.fetchall()
            for column in result:

                if form.email.data == column[3]:
                    L_email = column[3]

                    thereisuser = True
                if form.password.data == column[4]:
                    L_pass = column[4]
                    passwordmatch = True

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            print("done")
        # -----------------------------------------------------------
        # hash code error here because of not being encoded in utf-8 ?
        if (thereisuser and passwordmatch ):
            #user = User()
            #Customer.objects.get(customer_id)

            #attributes = ['name', 'email'...]
            #user.objects.get(1)
            #user = load_user(request.values.get('username'))
            # global IsUserLoggedIn
            IsUserLoggedIn = True
            return render_template('transacoes/tab_transacoes.html', posts=posts, title="Transações",IsUserLoggedIn=IsUserLoggedIn)
        else:
            flash(f'Login unsuccessful', 'danger')
            # global IsUserLoggedIn
            IsUserLoggedIn = False
            return render_template("layout/login.html", title='Login', form=form,IsUserLoggedIn=IsUserLoggedIn)
    return render_template("layout/login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    global IsUserLoggedIn
    IsUserLoggedIn = False
    return redirect(url_for('home'))


# ---------------------------- Transações ------------------------------------------
@app.route("/tab_transacoes")
def tab_transacoes():
    print('Value of logged in = ')
    print(IsUserLoggedIn)
    return render_template('transacoes/tab_transacoes.html', posts=posts, title="Transações",IsUserLoggedIn=IsUserLoggedIn)


@app.route("/new_transacoes", methods=['GET', 'POST'])
def new_transacoes():
    form = TransacoesForm()
    if form.validate_on_submit():
        flash(f'Done!', 'success')
        return redirect(url_for('tab_transacoes'))
    return render_template('transacoes/new_transacoes.html', title="Nova Transação", form=form,
                           legend='Registar a nova transação',IsUserLoggedIn=IsUserLoggedIn)


@app.route("/tab_transacoes/<int:post_id>")
def transacoes(post_id):
    return render_template('transacoes/transacoes.html', title=post.title, post=post,IsUserLoggedIn=IsUserLoggedIn)


@app.route("/tab_transacoes/<int:post_id>/update", methods=['GET', 'POST'])
def update_transacoes(post_id):  # cant have same function name
    form = TransacoesForm()
    if form.validate_on_submit():
        post.content = form.content.data
        post.title = form.content.data
        flash(f'Changes were updated successfully', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('transacoes/new_transacoes.html', title="Update Transação", form=form,
                           legend='Update Transação',IsUserLoggedIn=IsUserLoggedIn)


@app.route('/transacoes/<int:post_id>/delete', methods=['POST'])
def delete_transacoes(post_id):
    flash(f'Delete successfull', 'info')
    return redirect(url_for('transacoes/tab_transacoes'))


# ---------------------------- Clientes ------------------------------------------


@app.route("/tab_client")
def tab_client():
    return render_template('client/tab_client.html', posts=posts, title="Clientes",IsUserLoggedIn=IsUserLoggedIn)


@app.route("/new_client", methods=['GET', 'POST'])
def new_client():
    form = ClientForm()
    if form.validate_on_submit():
        flash(f'Done!', 'success')
        return redirect(url_for('tab_client'))
    return render_template('client/new_client.html', title="Novo Cliente", form=form, legend='Registar novo cliente',IsUserLoggedIn=IsUserLoggedIn)


# ---------------------------- Ementa --------------------------------------------


@app.route("/tab_menu")
def tab_menu():
    return render_template('menu/tab_menu.html', posts=posts, title="Ementas",IsUserLoggedIn=IsUserLoggedIn)


@app.route("/new_menu", methods=['GET', 'POST'])
def new_menu():
    form = MenuForm()
    if form.validate_on_submit():
        flash(f'Done!', 'success')
        return redirect(url_for('tab_menu'))
    return render_template('menu/new_menu.html', title="Nova Ementa", form=form, legend='Criar nova Ementa',IsUserLoggedIn=IsUserLoggedIn)


# ---------------------------- Produtos ------------------------------------------


@app.route("/tab_product")
def tab_product():
    return render_template('product/tab_product.html', posts=posts, title="Produtos",IsUserLoggedIn=IsUserLoggedIn)


@app.route("/new_product", methods=['GET', 'POST'])
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        flash(f'Done!', 'success')
        return redirect(url_for('tab_product'))
    return render_template('product/new_product.html', title="Novo produto", form=form, legend='Registar novo produto',IsUserLoggedIn=IsUserLoggedIn)


# ---------------------------- + TESTES ------------------------------------------
@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash(f'Done!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('testes/create_post.html', title="New Post", form=form, legend='New Post',IsUserLoggedIn=IsUserLoggedIn)


@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template('testes/post.html', title=post.title, post=post,IsUserLoggedIn=IsUserLoggedIn)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):  # cant have same function name
    form = PostForm()
    if form.validate_on_submit():
        post.content = form.content.data
        post.title = form.content.data
        flash(f'Changes were updated successfully', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('testes/create_post.html', title="Update Post", form=form, legend='Update Post',IsUserLoggedIn=IsUserLoggedIn)


@app.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):

    flash(f'Delete successfull', 'info')
    return redirect(url_for('dashboard'))


@app.route("/dashboard")
def dashboard():
    return render_template('testes/dashboard.html', posts=posts, title="Account",IsUserLoggedIn=IsUserLoggedIn)
