import cherrypy
import json


class _state_controller(object):
	def __init__(self, db):
		self.db = db
		self.BASE_PATH = '/home/paradigms/'

	def get_states(self):
		output = {'result': 'success'}
		try:
			result = self.db.get_states()
			output['states'] = result
		except Exception as e:
			output = {'result': 'error', 'message': str(e)}
		return json.dumps(output)

	def get_state(self, abbrev):
		output = {'result': 'success'}
		try:
			result = self.db.get_state(abbrev)
			output['state'] = result
		except Exception as e:
			output = {'result': 'error', 'message': str(e)}
		return json.dumps(output)
