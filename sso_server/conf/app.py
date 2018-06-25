# coding: utf-8

import os

class Config(object):
    ADMIN = "yangdawei"
    APP_DEV_PORT = 8888
    SECRET_KEY = os.urandom(12)
    config_log = {
        'version': 1,
        'formatters':{
            'simple':{
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
            'simple2':{
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers':{
            'hostfile': {
                'class': 'logging.FileHandler',
                'filename': 'log/hosts.log',
                'level': 'DEBUG',
                'formatter': 'simple'
            },
    
            'httpfile': {
                'class': 'logging.FileHandler',
                'filename': 'log/http.log',
                'level': 'DEBUG',
                'formatter': 'simple'
            },
        },
        'loggers':{
            'hosts':{
                'handlers': ['hostfile'],
                'level': 'DEBUG',
            },
            'http':{
                'handlers': ['httpfile'],
                'level': 'INFO',
            }
        }
    }

class ProdConfig(Config):
    DEBUG = False
    # database
    DB_HOST = "127.0.0.1"
    DB_PORT = 3306
    DB_NAME = "ops"
    DB_USER = "root"
    DB_PASSWD = ""
    DB_CONNECT_TIMEOUT = 10
    DB_CHARSET = "utf8"
    TIMEOUT_TIMES = 3

class DevConfig(Config):
    DEBUG = True
    APP_DEV_PORT = 8888
    DB_HOST = "127.0.0.1"
    DB_PORT = 3306
    DB_NAME = "ops"
    DB_USER = "root"
    DB_PASSWD = ""
    DB_CONNECT_TIMEOUT = 10
    DB_CHARSET = "utf8"
    TIMEOUT_TIMES = 3
    MYSQL = "mysql+mysqldb://{username}:{password}@{server}:{port}/{database}".format(
        username = DB_USER,
        password = DB_PASSWD,
        server = DB_HOST,
        port = DB_PORT,
        database = DB_NAME
    )
    SQLALCHEMY_DATABASE_URI = MYSQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True



