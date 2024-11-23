from flask import Flask 

app = Flask(__name__)

# Import routes after initializing the app to avoid circular import
from application import routes