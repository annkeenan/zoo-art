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
            output['families'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def get_classification(self, family):
        output = {'result': 'success'}
        try:
            result = self.db.get_classication(family)
            result['desc'] = list(result['desc'])
            output['classification'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def post_classification(self):
        output = {'result': 'success'}
        # Get the post data
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl)).decode('utf-8')
        data = json.loads(rawbody)
        # Call the database function
        try:
            self.db.post_classification(data['family'], data['info'])
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        # Return status
        return json.dumps(output)
