from flask import render_template, url_for, flash, redirect, request
from app.forms import RegistrationForm, LoginForm, TransacoesForm, ClientForm, ProductForm, MenuForm
from app import app, psycopg2
from app import cursor

IsUserLoggedIn = False
AdminNameLoggedIn = ""

@app.route('/')
@app.route('/home')
def home():
    global IsUserLoggedIn
    global AdminNameLoggedIn
    return render_template("layout/home.html", title='Home', IsUserLoggedIn=IsUserLoggedIn, AdminNameLoggedIn=AdminNameLoggedIn)


@app.route('/register', methods=['GET', 'POST'])
def register():
    global IsUserLoggedIn, resultverifica, resultinsert
    global AdminNameLoggedIn
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            cursor.callproc('verificaAdministrador',
                            [form.username.data, form.email.data, form.password.data, form.nome_restaurante.data])
            resultverifica = cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        print(resultverifica[0][0])
        if (resultverifica[0][0]):
            try:
                cursor.callproc('createAdministrador',
                                [form.username.data, form.email.data, form.password.data, form.nome_restaurante.data])
                resultinsert = cursor.fetchall()
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error while connecting to PostgreSQL", error)
            print(resultinsert[0][0])
            if resultinsert[0][0]:
                flash(f'Account created!', 'success')
            else:
                flash(f'Account already exists!', 'danger')
        return redirect(url_for('login'))
    return render_template("layout/register.html", title='Register', form=form, IsUserLoggedIn=IsUserLoggedIn)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global IsUserLoggedIn
    global AdminNameLoggedIn
    form = LoginForm()
    if form.validate_on_submit():
        try:
            cursor.callproc('verificarLogin', [form.email.data, form.password.data])
            result = cursor.fetchall()
            print(result[0][0])
            IsUserLoggedIn = result
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        if (IsUserLoggedIn[0][0]):
            AdminNameLoggedIn = form.email.data
            return render_template('transacoes/tab_transacoes.html', title="Transações",
                                   IsUserLoggedIn=IsUserLoggedIn)
        else:
            flash(f'Login unsuccessful', 'danger')
            IsUserLoggedIn = False
            return render_template("layout/login.html", title='Login', form=form, IsUserLoggedIn=IsUserLoggedIn)
    return render_template("layout/login.html", title='Login', form=form)


@app.route("/logout")
def logout():
    global IsUserLoggedIn
    IsUserLoggedIn = False
    return redirect(url_for('home'))


@app.route("/tab_transacoes")
def tab_transacoes():
    global IsUserLoggedIn
    global AdminNameLoggedIn
    alltransacoes = None
    print('Value of logged in = ')
    print(IsUserLoggedIn)
    try:
        print(" Transacoes : sent " + AdminNameLoggedIn)
        cursor.callproc('getAllTransacoes', [AdminNameLoggedIn])
        alltransacoes = cursor.fetchall()
        print("Transacoes got from bd")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    return render_template('transacoes/tab_transacoes.html', title="Transações",
                           IsUserLoggedIn=IsUserLoggedIn, alltransacoes=alltransacoes)


@app.route("/new_transacoes", methods=['GET', 'POST'])
def new_transacoes():
    global IsUserLoggedIn
    global AdminNameLoggedIn
    form = TransacoesForm()
    if form.validate_on_submit():
        try:
            print("HELLO IT HAPPENED")
            print(" create Transacoes : sent " + AdminNameLoggedIn, 1)
            cursor.callproc('createTransacao',
                            [AdminNameLoggedIn, int(form.title.data), int(form.lugar.data), int(form.valor.data),
                             int(form.carne.data), int(form.peixe.data), int(form.entrada.data), int(form.bebida.data),
                             int(form.sobremesa.data)])
            alltransacoes = cursor.fetchall()
            print("Transacoes got from bd")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        flash(f'Done!', 'success')
        return redirect(url_for('tab_transacoes'))
    return render_template('transacoes/new_transacoes.html', title="Nova Transação", form=form,
                           legend='Registar a nova transação', IsUserLoggedIn=IsUserLoggedIn)


@app.route("/tab_transacoes/<int:post_id>")
def transacoes(post_id):
    global IsUserLoggedIn, transac
    global AdminNameLoggedIn
    try:
        cursor.callproc('getTransacao', [post_id])
        transac = cursor.fetchall()
        print(transac)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    return render_template('transacoes/transacoes.html', transac=transac[0], IsUserLoggedIn=IsUserLoggedIn)


@app.route('/transacoes/<int:post_id>/delete', methods=['POST'])
def delete_transacoes(post_id):
    global IsUserLoggedIn
    global AdminNameLoggedIn
    try:
        cursor.callproc('deletetransacao', [post_id])
        transac = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    flash(f'Delete successfull', 'info')
    return redirect(url_for('tab_transacoes'))


@app.route("/tab_client")
def tab_client():
    global IsUserLoggedIn, result
    global AdminNameLoggedIn
    try:
        cursor.callproc('getallClientesFromRestaurante', [AdminNameLoggedIn])
        result = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    return render_template('client/tab_client.html', posts=result, title="Clientes", IsUserLoggedIn=IsUserLoggedIn)


@app.route("/new_client", methods=['GET', 'POST'])
def new_client():
    global IsUserLoggedIn
    global AdminNameLoggedIn
    form = ClientForm()
    if form.validate_on_submit():
        try:
            print(" Nome cliente enviado : " + form.NomeCliente.data)
            cursor.callproc('createCliente', [form.NomeCliente.data, AdminNameLoggedIn])
            result = cursor.fetchall()
            print(result)
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        flash(f'Done!', 'success')
        return redirect(url_for('tab_client'))
    return render_template('client/new_client.html', title="Novo Cliente", form=form,
                           legend='Registrar novo cliente no seu restaurante', IsUserLoggedIn=IsUserLoggedIn)


@app.route("/tab_client/<int:post_id>")
def client(post_id):
    global IsUserLoggedIn, client
    global AdminNameLoggedIn
    try:
        cursor.callproc('getclientes', [post_id])
        client = cursor.fetchall()
        print(client)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    return render_template('client/client.html', client=client[0], IsUserLoggedIn=IsUserLoggedIn)


@app.route('/client/<int:post_id>/delete', methods=['POST'])
def delete_client(post_id):
    global IsUserLoggedIn
    global AdminNameLoggedIn
    try:
        cursor.callproc('deletecartao', [AdminNameLoggedIn, post_id])
        client = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    flash(f'Delete successfull', 'info')
    return redirect(url_for('tab_client'))


@app.route("/tab_menu")
def tab_menu():
    global IsUserLoggedIn, ementa, domingo, quinta, quarta, sabado, segunda, sexta, terca
    global AdminNameLoggedIn
    try:
        print("EMENTA : DOMINGO : ")
        cursor.callproc('getAllEmentas', [AdminNameLoggedIn, 0])
        domingo = cursor.fetchall()
        print(domingo)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    try:
        print("EMENTA : SEGUNDA : ")
        cursor.callproc('getAllEmentas', [AdminNameLoggedIn, 1])
        segunda = cursor.fetchall()
        print(segunda)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    try:
        print("EMENTA : TERÇA : ")
        cursor.callproc('getAllEmentas', [AdminNameLoggedIn, 2])
        terca = cursor.fetchall()
        print(terca)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    try:
        print("EMENTA : QUARTA : ")
        cursor.callproc('getAllEmentas', [AdminNameLoggedIn, 3])
        quarta = cursor.fetchall()
        print(quarta)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    try:
        print("EMENTA : QUINTA : ")
        cursor.callproc('getAllEmentas', [AdminNameLoggedIn, 4])
        quinta = cursor.fetchall()
        print(quinta)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    try:
        print("EMENTA : SEXTA : ")
        cursor.callproc('getAllEmentas', [AdminNameLoggedIn, 5])
        sexta = cursor.fetchall()
        print(sexta)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    try:
        print("EMENTA : SABADO : ")
        cursor.callproc('getAllEmentas', [AdminNameLoggedIn, 6])
        sabado = cursor.fetchall()
        print(sabado)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    return render_template('menu/tab_menu.html', posts=domingo, segunda=segunda, terca=terca, quarta=quarta,
                           quinta=quinta, sexta=sexta, sabado=sabado, title="Ementas", IsUserLoggedIn=IsUserLoggedIn)


@app.route("/new_menu", methods=['GET', 'POST'])
def new_menu():
    global IsUserLoggedIn
    global AdminNameLoggedIn
    form = MenuForm()
    if form.validate_on_submit():
        try:
            print(" ementa enviado : " + AdminNameLoggedIn)
            cursor.callproc('createEmenta',
                            [AdminNameLoggedIn, int(form.dia.data), int(form.carne.data), int(form.peixe.data),
                             int(form.entrada.data), int(form.bebida.data), int(form.sobremesa.data)])
            result = cursor.fetchall()
            print(result)
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        flash(f'Done!', 'success')
        return redirect(url_for('tab_menu'))
    return render_template('menu/new_menu.html', title="Ementa", form=form,
                           legend='Editar a ementa do dia desta semana',
                           IsUserLoggedIn=IsUserLoggedIn)


@app.route("/tab_product")
def tab_product():
    global IsUserLoggedIn, result
    global AdminNameLoggedIn
    try:
        cursor.callproc('getAllProdutos')
        result = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    return render_template('product/tab_product.html', title="Produtos", IsUserLoggedIn=IsUserLoggedIn,
                           result=result)


@app.route("/new_product", methods=['GET', 'POST'])
def new_product():
    global IsUserLoggedIn
    global AdminNameLoggedIn
    form = ProductForm()
    if form.validate_on_submit():
        try:
            cursor.callproc('createProduto',
                            [int(form.tipo.data), form.nome.data, form.designacao.data, int(form.preco.data),
                             form.alergia.data, int(form.quantidade.data)])
            result = cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        flash(f'Done!', 'success')
        return redirect(url_for('tab_product'))
    return render_template('product/new_product.html', title="Novo produto", form=form, legend='Registar novo produto',
                           IsUserLoggedIn=IsUserLoggedIn)


@app.route("/product/<int:post_id>", methods=['GET', 'POST'])
def product(post_id):
    global IsUserLoggedIn, resultprod
    global AdminNameLoggedIn
    try:
        cursor.callproc('getAllProdutos')
        resultprod = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    form = ProductForm()
    if form.validate_on_submit():
        flash(f'Changes were updated successfully', 'success')
        return redirect(url_for('tab_product'))
    elif request.method == 'GET':
        form.choosetipo = [('0', 'Entradas'), ('1', 'Bebidas'), ('2', 'Sobremesas'), ('3', 'Carne'), ('4', 'Peixe')]
        form.nome.data = resultprod[post_id - 1][2]
        form.designacao.data = resultprod[post_id - 1][3]
        form.alergia.data = resultprod[post_id - 1][5]
        form.preco.data = resultprod[post_id - 1][4]  # correto
        form.quantidade.data = resultprod[post_id - 1][6]  # correto
        form.tipo.data = resultprod[post_id - 1][6]  # correto
        return render_template('product/update_product.html', title="Editar produto", form=form,
                               legend='Editar produto', IsUserLoggedIn=IsUserLoggedIn, post_id=post_id)

@app.route('/product/<int:post_id>/delete', methods=['POST'])
def delete_product(post_id):
    global IsUserLoggedIn
    global AdminNameLoggedIn
    try:
        print("del here")
        # cursor.callproc('', [AdminNameLoggedIn, post_id])
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    flash(f'Delete successfull', 'info')
    return redirect(url_for('tab_product'))
