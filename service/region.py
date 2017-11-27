import cherrypy
import json


class _region_controller(object):
    def __init__(self, db):
        self.db = db
        self.BASE_PATH = '/home/paradigms/'

    def get_regions(self):
        output = {'result': 'success'}
        try:
            result = self.db.get_regions()
            output.update(result)
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def get_region(self, region):
        output = {'result': 'success'}
        try:
            result = self.db.get_region(region)
            output.update(result)
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)

    def post_region(self):
        output = {'result': 'success'}
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        data = json.loads(rawbody)
        try:
            result = self.db.post_region(data['region'], data['desc'])
            output.update(result)
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)
