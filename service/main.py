import cherrypy
import context  # Add the parent directory to the path

from api import _zoo_database
from reset import _reset_controller


class _options_controller(object):
    def OPTIONS(self, *args, **kargs):
        return ""


def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"


def start_service():
    db = _zoo_database()
    options_controller = _options_controller()
    reset_controller = _reset_controller(db)

    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    # preflight options
    dispatcher.connect(name='preflight_reset_all', route='/reset/', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))

    # reset
    dispatcher.connect(name='reset_all', route='/reset/', controller=reset_controller, action='reset_all', conditions=dict(method=['PUT']))

    conf = {
        'global': {
            'server.socket_host': 'student04.cse.nd.edu',
            'server.socket_port': 51042,
        },
        '/': {
            'request.dispatch': dispatcher,
            'tools.CORS.on': True
        }
    }
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
