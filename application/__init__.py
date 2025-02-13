from flask import Flask                 #create an instance of the flask extention 
from config import Config               #import config settings 
from flask_mongoengine import MongoEngine               #import mongoengine class from the flask_mongoengine extention 
from flask_restplus import Api 

 
api = Api()
 
# create instance of a flask application 
app = Flask(__name__)
# load the config settings 
app.config.from_object(Config)
app.debug = True

# create an instance of mongoengine
db = MongoEngine(app)


# initialize MongoEngine with the flask application 
db.init_app(app)
api.init_app(app)


# Import routes after initializing the app to avoid circular import
from application import routes



# The app is created and configured using the Config class.
# MongoDB integration is set up using MongoEngine.
# Routes are imported after app initialization to prevent circular imports.Fp