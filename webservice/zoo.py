import cherrypy
import json

class _zoo_controller(object):
    def __init__(self, db):
        self.db = db
        self.BASE_PATH = '/home/paradigms/'

    def get_zoos(self):
        output = {'result': 'success'}
        try:
            result = self.db.get_zoos()
            output['zoos'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)
    def get_zoo(self, zoo):
        output = {'result': 'success'}
        try:
            result = self.db.get_zoo(zoo)
            output['zoo'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)
    def post_zoo(self):
        output = {'result': 'success'}
        #Get the post data
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl)).decode('utf-8')
        data = json.loads(rawbody)
        # Call the database function
        try:
            self.db.post_zoo(data['zoo'], data['info'])
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        # Return status
        return json.dumps(output)
    def put_zoo(self, zoo, column, info):
        #NOT DONE YET
        output = {'result': 'success'}
        #Get the put data
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl)).decode('utf-8')
        data = json.loads(rawbody)
        # Call the database function
        try:
            self.db.put_zoo(data['zoo'], data['info'])
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        # Return status
        return json.dumps(output)
