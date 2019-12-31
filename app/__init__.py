from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import psycopg2
app = Flask(__name__)
app.config['SECRET_KEY'] = '76d5f16cf6bb57be0bd6851a8c61df1d'  # secret key for security
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # path da db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warning
db = SQLAlchemy(app)  # instancia da db
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

ps_connection = psycopg2.connect(user="fphawxtr",
                                 password="RLu6UKWGf8AS-dQIKRYVrRujGy_surEA",
                                 host="rogue.db.elephantsql.com",
                                 port="5432",
                                 database="fphawxtr")
cursor = ps_connection.cursor()



# a package structure evita "dependency hell". Mas quando no modulo routes.py temos um import da variavel app, temos de
# nos certificar que a variavel está declarada antes de ser importada, senão temos uma dependencia circular
# pip installed packages nao sofrem de dependencia circular, embora estejamos a infrigir PEP8

from app import routes