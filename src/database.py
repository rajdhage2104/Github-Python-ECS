import sqlalchemy
import os
from flask_sqlalchemy import SQLAlchemy

db_user = 'ctgdevops'
db_password = 'devops123'
db_name = 'mydatabase'
db_host = 'python-db.cvggya6kg1r7.us-east-1.rds.amazonaws.com'

db_url = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
db = SQLAlchemy()

