import psycopg2
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

from app import cursor


# ----------------------------- TESTES ----------------------------------------------------------------------
class RegistrationForm(FlaskForm):  # inherits from FlaskForm
    global choose
    # ---------------------------getnomesrestaurantes---------------
    try:
        i = 0
        cursor.callproc('getNomeRestaurantes')
        # cursor.execute("SELECT * FROM restaurante")
        result = cursor.fetchall()
        # print(result)
        for column in result[0]:
            for bull in column:
                # print(column[i])
                if i == 0:
                    choose = [(column[0], column[0])]
                else:
                    choose += [(column[i], column[i])]
                i = i + 1
                print(i)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        print()
        # O formato da lista que recebe tem de ser igual a
        # choose = [('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]

        # print(choose)
        # print("done")

    # -----------------------------------------------------------

    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    nome_restaurante = SelectField(u'Restaurante', choices=choose, validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    isit = False

    def validate_username(self, username):
        global isit, choose
        try:
            cursor.callproc('VerifyUsername', [username.data])
            result = cursor.fetchall()
            for column in result:
                print("  VerifyUsername result = ", column[0])
                isit = column[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            print("done")
        if isit:
            raise ValidationError('Username taken. Choose a different one')

    def validate_email(self, email):
        global isitemail
        try:
            cursor.callproc('VerifyEmail', [email.data])
            result = cursor.fetchall()
            for column in result:
                print("  VerifyEmail result = ", column[0])
                isitemail = column[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            print("done")
        if isitemail:
            raise ValidationError('Email already has an account associated')


class LoginForm(FlaskForm):  # inherits from FlaskForm
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


# ----------------------------- TRANSACOES ----------------------------------------------------------------------


class TransacoesForm(FlaskForm):
    global lcarne, lbebida, lpeixe, lsobremesa, lentrada
    lugar = [("1", 'Esplanada'), ("2", 'Bar'), ("3", 'Salão'),("4", 'Sala VIP')]

    # ementacarne = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]

    try:

        cursor.callproc('getAllCarne')
        resultlCarne = cursor.fetchall()
        lcarne = [("-1", "SEM PEDIDO")]
        for column in resultlCarne:
            lcarne += [(str(column[0]), column[2])]
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    # ementapeixe = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]

    try:
        cursor.callproc('getAllPeixe')
        resultlpeixe = cursor.fetchall()
        lpeixe = [("-1", "SEM PEDIDO")]
        for column in resultlpeixe:
            lpeixe += [(str(column[0]), column[2])]
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    # ementaentrada = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]

    try:
        cursor.callproc('getAllEntradas')
        resultlentrada = cursor.fetchall()
        lentrada = [("-1", "SEM PEDIDO")]
        for column in resultlentrada:
            lentrada += [(str(column[0]), column[2])]
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    # ementabebida = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]
    try:
        cursor.callproc('getAllBebidas')
        resultlbebida = cursor.fetchall()
        lbebida = [("-1", "SEM PEDIDO")]
        for column in resultlbebida:
            lbebida += [(str(column[0]), column[2])]
        print(lbebida)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    # ementasobremesa = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]

    try:
        cursor.callproc('getAllSobremesas')
        resultlsobremesa = cursor.fetchall()
        lsobremesa = [("-1", "SEM PEDIDO")]
        for column in resultlsobremesa:
            lsobremesa += [(str(column[0]), column[2])]
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    title = StringField('ID cartão cliente', validators=[DataRequired()])
    lugar = SelectField(u'Lugar no restaurante', choices=lugar, validators=[DataRequired()])
    valor = StringField('valor', validators=[DataRequired()])
    carne = SelectField(u'Carne', choices=lcarne, validators=[DataRequired()])
    peixe = SelectField(u'Peixe', choices=lpeixe, validators=[DataRequired()])
    entrada = SelectField(u'Entrada', choices=lentrada, validators=[DataRequired()])
    bebida = SelectField(u'Bebida', choices=lbebida, validators=[DataRequired()])
    sobremesa = SelectField(u'Sobremesa', choices=lsobremesa, validators=[DataRequired()])

    submit = SubmitField('Registrar transação')


# ----------------------------- CLIENTES ----------------------------------------------------------------------


class ClientForm(FlaskForm):
    NomeCliente = StringField('Nome do cliente', validators=[DataRequired()])
    submit = SubmitField('Adicionar cliente')


# ----------------------------- Menu ----------------------------------------------------------------------


class MenuForm(FlaskForm):
    global ementabebida, ementacarne, ementapeixe, ementaentrada, ementasobremesa
    ementadia = [('0', 'Domingo'), ('1', 'Segunda'), ('2', 'Terça'),
                 ('3', 'Quarta'), ('4', 'Quinta'), ('5', 'Sexta'), ('6', 'Sábado')]
    ementalugar = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),
                   ('interior 4', 'interior 4')]

    # ementacarne = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]

    try:
        i = 0
        cursor.callproc('getAllCarne')
        resultEmentaCarne = cursor.fetchall()
        for column in resultEmentaCarne:
            if i == 0:
                ementacarne = [(str(column[0]), column[2])]
            else:
                ementacarne += [(str(column[0]), column[2])]
            i = i + 1
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    # ementapeixe = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]

    try:
        i = 0
        cursor.callproc('getAllPeixe')
        resultEmentapeixe = cursor.fetchall()
        for column in resultEmentapeixe:
            if i == 0:
                ementapeixe = [(str(column[0]), column[2])]
            else:
                ementapeixe += [(str(column[0]), column[2])]
            i = i + 1
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    # ementaentrada = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]

    try:
        i = 0
        cursor.callproc('getAllEntradas')
        resultEmentaentrada = cursor.fetchall()
        for column in resultEmentaentrada:
            if i == 0:
                ementaentrada = [(str(column[0]), column[2])]
            else:
                ementaentrada += [(str(column[0]), column[2])]
            i = i + 1
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    # ementabebida = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]
    try:
        i = 0
        cursor.callproc('getAllBebidas')
        resultEmentabebida = cursor.fetchall()
        for column in resultEmentabebida:
            if i == 0:
                ementabebida = [(str(column[0]), column[2])]
            else:
                ementabebida += [(str(column[0]), column[2])]
            i = i + 1
        print(ementabebida)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

   # ementasobremesa = [('esplanada 1', 'esplanada 1'), ('esplanada 2', 'esplanada 2'), ('interior 3', 'interior 3'),('interior 4', 'interior 4')]

    try:
        i = 0
        cursor.callproc('getAllSobremesas')
        resultEmentasobremesa = cursor.fetchall()
        for column in resultEmentasobremesa:
            if i == 0:
                ementasobremesa = [(str(column[0]), column[2])]
            else:
                ementasobremesa += [(str(column[0]), column[2])]
            i = i + 1
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    # title = StringField('Dia da semana', validators=[DataRequired()])
    dia = SelectField(u'Dia da semana', choices=ementadia, validators=[DataRequired()])
    carne = SelectField(u'Carne', choices=ementacarne, validators=[DataRequired()])
    peixe = SelectField(u'Peixe', choices=ementapeixe, validators=[DataRequired()])
    entrada = SelectField(u'Entrada', choices=ementaentrada, validators=[DataRequired()])
    bebida = SelectField(u'Bebida', choices=ementabebida, validators=[DataRequired()])
    sobremesa = SelectField(u'Sobremesa', choices=ementasobremesa, validators=[DataRequired()])
    submit = SubmitField('Confirmar atualização da ementa')


# ----------------------------- Product ----------------------------------------------------------------------


class ProductForm(FlaskForm):
    choosetipo = [('0', 'Entradas'), ('1', 'Bebidas'), ('2', 'Sobremesas'), ('3', 'Carne'), ('4', 'Peixe')]
    nome = StringField('Nome do Produto', validators=[DataRequired()])
    designacao = TextAreaField('Informação', validators=[DataRequired()])
    alergia = TextAreaField('Possiveis alergias do produto', validators=[DataRequired()])
    preco = StringField('Preço', validators=[DataRequired()])
    quantidade = StringField('Quantidade', validators=[DataRequired()])
    tipo = SelectField(u'Tipo', choices=choosetipo, validators=[DataRequired()])
    # myint = IntegerField('Number', widget=html5.NumberInput())
    submit = SubmitField('Registrar Produto')
