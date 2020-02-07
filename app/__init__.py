from flask import Flask
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = '76d5f16cf6bb57be0bd6851a8c61df1d'

ps_connection = psycopg2.connect(user="fphawxtr",
                                 password="EvqCxQNpbriPJdvPVjelyubKgI8bt0bE",
                                 host="rogue.db.elephantsql.com",
                                 port="5432",
                                 database="fphawxtr")

ps_connection.autocommit = True
cursor = ps_connection.cursor()

from app import routes
