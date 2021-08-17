# -*- coding: utf-8 -*-
import pymysql

from flask import Flask
from loguru import logger

from pegase3_api.configuration_manager import *


# dump_configuration()

config_users = load_configuration()
logger.info(config_users)

config = load_json_configuration()
logger.debug(config)

connect_mysql = pymysql.connect(user='root', password='root', database='pegase3', host='localhost', port=3310)
cursor_mysql = connect_mysql.cursor()




