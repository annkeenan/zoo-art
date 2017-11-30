import cherrypy
import json

class _status_controller(object):
    def __init__(self, db):
        self.db = db
        self.BASE_PATH = '/home/paradigms/'

    def get_statuses(self):
        output = {'result': 'success'}
        try:
            result = self.db.get_statuses()
            output['statuses'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)
    def get_status(self, status):
        output = {'result': 'success'}
        try:
            result = self.db.get_status(status)
            output['description'] = result
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)
