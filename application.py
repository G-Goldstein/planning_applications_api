import application_planning_database, psycopg2, os
from flask_restful import Resource, reqparse

DATABASE_URL = os.environ['DATABASE_URL']

class Application(Resource):
	def __init__(self):
		self.conn = psycopg2.connect(DATABASE_URL)

	def get(self):
		limit, offset, search = self.get_args()
		return list(application_planning_database.applications_by_validated_date(limit, offset))

	def get_args(self):
		parser = reqparse.RequestParser()
		parser.add_argument('limit')
		parser.add_argument('offset')
		parser.add_argument('search')
		args = parser.parse_args()
		return args['limit'], args['offset'], args['search']