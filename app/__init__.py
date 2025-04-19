from flask import Flask

app = Flask(__name__)

# Import routes from the routes folder
from app.routes import routes
