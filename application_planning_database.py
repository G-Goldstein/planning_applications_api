import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def cursor():
	conn = psycopg2.connect(DATABASE_URL)
	return conn.cursor()

def applications_by_validated_date(limit=25, offset=0, search=''):
	c = cursor()
	c.execute(
		"""
			SELECT reference, title, link, address, received_date, validated_date, status
			FROM application
			ORDER BY validated_date DESC
			LIMIT %s OFFSET %s
		""", [limit, offset])
	yield from c.fetchmany(limit)