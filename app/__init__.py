from flask import Flask
import psycopg2
app = Flask(__name__)
app.config['SECRET_KEY'] = '76d5f16cf6bb57be0bd6851a8c61df1d'  # secret key for security


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