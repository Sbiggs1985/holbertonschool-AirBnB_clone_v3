#!/usr/bin/python3
"""
Creating files for an api
"""
from flask import Flask
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)

"""Allow CORS for all routes on 0.0.0.0"""
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(self):
    """Closes the storage on teardown"""
    from models import storage
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return {"error": "Not found"}, 404


def start_flask():
    """ start flask """
    from os import getenv as env
    app.run(host=env('HBNB_API_HOST', default='localhost'),
            port=env('HBNB_API_PORT'),
            threaded=True)


if __name__ == "__main__":
    start_flask()
