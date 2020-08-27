import logging

import connexion
from flask_testing import TestCase

from api.encoder import JSONEncoder

from throttling_quota import ThrottlingQuota


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../openspi/")
        app.app.json_encoder = JSONEncoder
        app.add_api("swagger.yaml")

        return app.app
