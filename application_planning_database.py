import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def cursor():
	conn = psycopg2.connect(DATABASE_URL)
	return conn.cursor()

def applications_by_validated_date(limit=25, offset=0, search=''):
	if limit == None:
		limit = 25
	if offset == None:
		offset = 0
	c = cursor()
	if search == None or search.strip() == '':
		search = ''
		c.execute(
		"""
			SELECT reference, title, link, address, TO_CHAR(received_date :: DATE, 'dd/mm/yyyy'), TO_CHAR(validated_date :: DATE, 'dd/mm/yyyy'), status
			FROM application
			ORDER BY validated_date DESC, received_date DESC, reference DESC
			LIMIT %s OFFSET %s
		""", [int(limit), int(offset)])
	else:
		search = ' & '.join(search.strip().split(' '))
		c.execute(
		"""
			SELECT reference, title, link, address, TO_CHAR(received_date :: DATE, 'dd/mm/yyyy'), TO_CHAR(validated_date :: DATE, 'dd/mm/yyyy'), status
			FROM application
			WHERE to_tsquery(%s) @@ to_tsvector(title)
			   OR to_tsquery(%s) @@ to_tsvector(address)
			ORDER BY validated_date DESC, received_date DESC, reference DESC
			LIMIT %s OFFSET %s
		""", [search, search, int(limit), int(offset)])
	for row in c.fetchmany(int(limit)):
		application = {
			'reference': row[0],
			'title': row[1],
			'link': row[2],
			'address': row[3],
			'received_date': row[4],
			'validated_date': row[5],
			'status': row[6]
		}
		yield application