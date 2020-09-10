import logging

import connexion
from flask import g
from flask_testing import TestCase

from api.store import MongoStore, Store


class BaseTestCase(TestCase):
    def create_app(self):
        """
        This method sets up the class automatically.
        """
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../openapi/")
        app.add_api("store.yaml")

        @app.app.before_first_request
        def create_store():
            """
            Which DBMS are we using to run our tests?
            Can you fix that?
            :return:
            """
            app.app.config["store"] = MongoStore(
                host="mongo", username="root", password="secret"
            )

        return app.app
