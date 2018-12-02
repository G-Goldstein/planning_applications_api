from application import Application
from flask import Flask
from flask_restful import Api
from waitress import serve

app = Flask(__name__)
api = Api(app)

api.add_resource(Application, '/application')

serve(app, host='0.0.0.0', port='5000')