import os
import connexion
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.CouchProvider import CouchProvider
from gevent.pywsgi import WSGIServer

from injector import Binder
from flask_cors import CORS
def configure(binder: Binder) -> Binder:
    binder.bind(
        CouchProvider
    )


def basic_auth(username, password, required_scopes=None):
    if username == 'lsantagata' and password == 'qawsed.123':
        return {'sub': 'lsantagata'}

    # optional: raise exception for custom error response
    return None


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs
    CORS(app.app)
    app.add_api('couch-service-docs.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
     # Debug/Development
    #app.run(port=int(os.environ.get('PORT', 2020))) # os.environ is handy if you intend to launch on heroku
    http_server = WSGIServer(('0.0.0.0', 2020), app)
    http_server.serve_forever()
