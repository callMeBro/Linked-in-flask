import os

class Config(object):
    SECRET_kY = os.envron.get('SECRET_KEY') or 'secrete_string'
    