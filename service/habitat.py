import cherrypy
import json


class _habitat_controller(object):
    def __init__(self, db):
        self.db = db
        self.BASE_PATH = '/home/paradigms/'

    def get_habitats(self):
        output = {'result': 'success'}
        try:
            result = self.db.get_habitats()
            output['habitats'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def get_habitat(self, habitat):
        output = {'result': 'success'}
        try:
            result = self.db.get_habitat(habitat)
            output['habitat'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def post_habitat(self):
        output = {'result': 'success'}
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        data = json.loads(rawbody)
        try:
            self.db.post_habitat(data['habitat'], data['desc'])
        except Exception as e:
            output = {'result': 'error', 'messsage': str(e)}
        return json.dumps(output)
