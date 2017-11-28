import cherrypy
import context  # Add the parent directory to the path

from ooapi import _zoo_database
from classification import _classification_controller
# from exhibit import _exhibit_controller
from habitat import _habitat_controller
from region import _region_controller
from reset import _reset_controller
# from species import _species_controller
# from state import _state_controller
# from status import _status_controller
# from zoo import _zoo_controller


class _options_controller(object):
    def OPTIONS(self, *args, **kargs):
        return ""


def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"


def start_service():
    zdb = _zoo_database._zoo_database()

## Controllers
    options_controller = _options_controller()
    classification_controller = _classification_controller(zdb)
    # exhibit_controller = _exhibit_controller(zdb)
    habitat_controller = _habitat_controller(zdb)
    region_controller = _region_controller(zdb)
    reset_controller = _reset_controller(zdb)
    # species_controller = _species_controller(zdb)
    # state_controller = _state_controller(zdb)
    # status_controller = _status_controller(zdb)
    # zoo_controller = _zoo_controller(zdb)

    dispatcher = cherrypy.dispatch.RoutesDispatcher()

## Preflight options
    # Classification
    dispatcher.connect(name='preflight_get_families', route='/classification/', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='preflight_get_classification', route='/classification/:family', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='preflight_post_classification', route='/classification/:family', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    # Exhibit
    # Habitat
    dispatcher.connect(name='preflight_get_habitats', route='/habitat/', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='preflight_get_habitat', route='/habitat/:habitat', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='preflight_post_habitat', route='/habitat/', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    # Region
    dispatcher.connect(name='preflight_get_regions', route='/region/', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='preflight_get_region', route='/region/:region', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='preflight_post_region', route='/region/', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    # Reset
    dispatcher.connect(name='preflight_reset_all', route='/reset/', controller=options_controller, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    # Species
    # State
    # Status
    # Zoo

## Options
    # Classification
    dispatcher.connect(name='get_families', route='/classification/', controller=classification_controller, action='get_families', conditions=dict(method=['GET']))
    dispatcher.connect(name='get_classification', route='/classification/:family', controller=classification_controller, action='get_classification', conditions=dict(method=['GET']))
    dispatcher.connect(name='post_classification', route='/classification/', controller=classification_controller, action='post_classification', conditions=dict(method=['POST']))
    # Exhibit
    # Habitat
    dispatcher.connect(name='get_habitats', route='/habitat/', controller=habitat_controller, action='get_habitats', conditions=dict(method=['GET']))
    dispatcher.connect(name='get_habitat', route='/habitat/:habitat', controller=habitat_controller, action='get_habitat', conditions=dict(method=['GET']))
    dispatcher.connect(name='post_habitat', route='/habitat/', controller=habitat_controller, action='post_habitat', conditions=dict(method=['POST']))
    # Region
    dispatcher.connect(name='get_regions', route='/region/', controller=region_controller, action='get_regions', conditions=dict(method=['GET']))
    dispatcher.connect(name='get_region', route='/region/:region', controller=region_controller, action='get_region', conditions=dict(method=['GET']))
    dispatcher.connect(name='post_region', route='/region/', controller=region_controller, action='post_region', conditions=dict(method=['POST']))
    # Reset
    dispatcher.connect(name='reset_all', route='/reset/', controller=reset_controller, action='reset_all', conditions=dict(method=['PUT']))
    # Species
    # State
    # Status
    # Zoo

## Configuration
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

## Launch
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()