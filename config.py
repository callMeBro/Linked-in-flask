import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_string'
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/UTA_Enrollment'
    }
