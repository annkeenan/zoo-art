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
            result['common_name'] = sorted(list(result['common_name']))
            result['region'] = sorted(list(result['region']))
            result['habitat'] = sorted(list(result['habitat']))
            output['species'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def put_species(self, species):
        output = {'result': 'success'}
        # Get the post data
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl)).decode('utf-8')
        data = json.loads(rawbody)
        try:
            # Loop through columns to update each for species
            for column, value in data.items():
                self.db.put_species(species, column, value)
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def post_species(self):
        output = {'result': 'success'}
        # Get the post data
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl)).decode('utf-8')
        data = json.loads(rawbody)
        try:
            self.db.post_species(data['species'], data['info'])
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)
