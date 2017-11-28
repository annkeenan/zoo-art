import json


class _reset_controller(object):
    def __init__(self, db):
        self.db = db

    def reset_all(self):
        output = {'result': 'success'}
        try:
            self.db.reset_all()
            self.db.load_all()
        except Exception as e:
            output = {'result': 'error', 'message': str(e)}
        return json.dumps(output)
