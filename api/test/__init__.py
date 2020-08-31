import logging

import connexion
from flask_testing import TestCase
from flask import g

from api.throttling_quota import ThrottlingQuota


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../../openapi/")
        app.add_api("store.yaml")

        @app.app.before_first_request
        def create_store():
            g.store = {}

        return app.app
