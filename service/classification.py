import cherrypy
import json


class _classification_controller(object):
    def __init__(self, db):
        self.db = db
        self.BASE_PATH = '/home/paradigms/'

    def get_families(self):
        output = {'result': 'success'}
        try:
            result = self.db.get_families()
            output.update(result)
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def get_classification(self, family):
        output = {'result': 'success'}
        try:
            result = self.db.get_classication(family)
            output.update(result)
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def post_classification(self):
        output = {'result': 'success'}
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        data = json.loads(rawbody)
        try:
            result = self.db.post_classication(data['family'], data['info'])
            output.update(result)
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)
