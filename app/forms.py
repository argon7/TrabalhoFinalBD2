from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
import psycopg2
from app import ps_connection, cursor


# ----------------------------- TESTES ----------------------------------------------------------------------
class RegistrationForm(FlaskForm):  # inherits from FlaskForm
    # ---------------------------getnomesrestaurantes---------------
    try:
        i = 0
        # cursor.callproc('getNomeRestaurantes')
        cursor.execute("SELECT * FROM restaurante")
        result = cursor.fetchall()
        #print(result)
        for column in result:
            #print(column[3])
            if i==0:
                choose = [(column[3],column[3])]
                i=i+1
            else:
                choose += [(column[3], column[3])]
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        print()
        # O formato da lista que recebe tem de ser igual a
        # choose = [('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]

        #print(choose)
        #print("done")

    # -----------------------------------------------------------

    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    nome_restaurante = SelectField(u'Restaurante', choices=choose, validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    isit = False

    def validate_username(self, username):
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
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


# ----------------------------- CLIENTES ----------------------------------------------------------------------


class ClientForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


# ----------------------------- Menu ----------------------------------------------------------------------


class MenuForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


# ----------------------------- Product ----------------------------------------------------------------------


class ProductForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
