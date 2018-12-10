from application import Application
from flask import Flask
from flask_restful import Api
from waitress import serve
from flask_restful import Resource
import os

app = Flask(__name__)
api = Api(app)

class Okay(Resource):
	def get(self):
		return 'Okay'

api.add_resource(Application, '/application')
api.add_resource(Okay, '/')

serve(app, host='0.0.0.0', port=os.environ['PORT'])
