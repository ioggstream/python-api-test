#!/usr/bin/env python3

from logging import basicConfig
from logging.config import dictConfig
from os import environ as env
from os.path import isfile

import connexion
import yaml
from flask import g

from api.store import MongoStore, Store


def configure_logger(log_config="logging.yaml"):
    """Configure the logging subsystem."""
    if not isfile(log_config):
        return basicConfig()

    with open(log_config) as fh:
        log_config = yaml.safe_load(fh)
        return dictConfig(log_config)


def main():
    configure_logger()

    app = connexion.App(__name__, specification_dir="../openapi/")
    app.add_api("store.yaml", arguments={"title": "Store items."})

    @app.app.before_first_request
    def create_store():
        print("add store stuff")
        if env.get("MONGO_HOST"):
            app.app.config["store"] = MongoStore(
                host=env["MONGO_HOST"], username="root", password="secret"
            )
            return
        app.app.config["store"] = Store()

    app.run(port=8443, ssl_context="adhoc", debug=True)


if __name__ == "__main__":
    main()
