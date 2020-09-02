import logging

import connexion
from flask import g
from flask_testing import TestCase

from api.store import MongoStore, Store




class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../../openapi/")
        app.add_api("store.yaml")

        @app.app.before_first_request
        def create_store():
            g.store = MongoStore(
                host="192.168.32.2", username="root", password="secret"
            )

        return app.app
