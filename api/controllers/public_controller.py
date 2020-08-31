import datetime
from random import randint

from connexion import problem
from api.models.timestamps import Timestamps  # noqa: E501
from throttling_quota import throttle
from flask import after_this_request
from functools import wraps


@throttle
def get_echo():  # noqa: E501
    """Ritorna un timestamp in formato RFC5424.

    Ritorna un timestamp in formato RFC5424 prendendola dal server attuale.  # noqa: E501


    :rtype: Timestamps
    """
    return Timestamps(datetime.datetime.utcnow())
