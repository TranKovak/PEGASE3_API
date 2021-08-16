# -*- coding: utf-8 -*-
import pymysql

from flask import Flask
from loguru import logger

from pegase3_api.configuration_manager import *


# dump_configuration()
config = load_configuration()
app = Flask(__name__, static_folder='static')
# cursor_p3 = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.11.5.3;DATABASE=Pegase3prod;UID=P3_READONLY;PWD=ENz49ilPK8GcJQfp5VRP').cursor()
cursor_mysql = pymysql.connect(user='root', password='root', database='pegase3', host='localhost', port=3310).cursor()




