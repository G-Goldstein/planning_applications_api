import application_planning_database
from flask_restful import Resource, reqparse

class Application(Resource):

	def get(self):
		limit, offset, search = self.get_args()
		return list(application_planning_database.applications_by_validated_date(limit, offset, search))

	def get_args(self):
		parser = reqparse.RequestParser()
		parser.add_argument('limit')
		parser.add_argument('offset')
		parser.add_argument('search')
		args = parser.parse_args()
		return args['limit'], args['offset'], args['search']