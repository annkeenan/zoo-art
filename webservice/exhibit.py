import cherrypy
import json


class _exhibit_controller(object):
    def __init__(self, db):
        self.db = db
        self.BASE_PATH = '/home/paradigms/'

    def get_exhibits(self, zoo, boolean):
        output = {'result': 'success'}
        
        try:
            if boolean == 'true':
                result = self.db.get_exhibited_zoo(zoo)
            elif boolean == 'false': 
                result = self.db.get_not_exhibited_zoo(zoo)
            output['species'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}

        if boolean != 'true' and boolean != 'false':
            output = {'result': 'error', 'message': 'second parameter is not true or false'}
        return json.dumps(output)

    def get_exhibits_species(self, species):
        output = {'result': 'success'}
        try:
            result = self.db.get_exhibits_species(species)
            output['zoos'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def post_exhibit(self, zoo):
        output = {'result': 'success'}
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl)).decode('utf-8')
        data = json.loads(rawbody)
        try:
            self.db.post_exhibit(zoo, data['species'])
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def delete_exhibit(self, zoo, species):
        output = {'result': 'success'}
        try:
            self.db.delete_exhibit(zoo, species)
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)
