import cherrypy
import json


class _species_controller(object):
	def __init__(self, db):
		self.db = db
		self.BASE_PATH = '/home/paradigms/'

	def get_all_species(self):
		output = {'result': 'success'}
		try:
			result = self.db.get_all_species()
			output['species'] = result
		except Exception as e:
			output = {'result': 'error', 'message': str(e)}
		return json.dumps(output)

	def get_species(self, species):
		output = {'result': 'success'}	
		try:
			result = self.db.get_species(species)
			# sets converted to list for json output
			result['common name'] = sorted(list(result['common name'])) 
			result['region'] = sorted(list(result['region']))
			result['habitat'] = sorted(list(result['habitat']))
			output[species] = result
		except Exception as e:
			output = {'result': 'error', 'message': str(e)}
		return json.dumps(output)

	def put_species(self, species):
		output = {'result': 'success'}
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read()
		data = json.loads(rawbody)
		try:
			# loop through columns to update each for species
			for column in data:
				self.db.put_species(species, column, data[column])
		except Exception as e:
			output = {'result': 'error', 'message': str(e)}
		return json.dumps(output)

	def post_species(self):
		output = {'result': 'success'}
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read()
		data = json.loads(rawbody)
		try:
			self.db.post_species(data['species'], data['info'])	 
		except Exception as e:
			output = {'result': 'error', 'message': str(e)}
		return json.dumps(output)
