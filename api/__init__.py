"""
Implement the API described by store.yaml OAS spec.




"""
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from connexion import problem
from flask import after_this_request, request
from flask import g, current_app


def get_item(uuid: str):
    return {
        "uuid": uuid,
        "status": "success",
        "item": {"a": 1, "b": "ciao"},
    }
    raise NotImplementedError


def get_items(limit: int = 10, cursor: str = ""):
    c = limit
    ret = []
    items = iter(x for x in sorted(g.store.items()) if x[0] >= cursor)
    for i in range(limit):
        try:
            k, v = next(items)
        except StopIteration:
            break
        ret.append(v)
        c -= 1
    try:
        cursor = next(items)[0]
    except StopIteration:
        cursor = None
    return dict(limit=limit, count=limit - c, items=ret, cursor=cursor)
    raise NotImplementedError


def post_items(body: dict):
    uuid = str(uuid4())
    ts = datetime.now().isoformat()
    g.store[uuid] = dict(id=uuid, timestamp=ts, item=body)
    return {
        "id": uuid,
        "timestamp": ts,
        "status": "success",
        "url": request.base_url + "/" + uuid,
        "debug": g.store,
    }
    raise NotImplementedError


def get_status():
    """Ritorna lo stato dell'applicazione.

    Ritorna lo stato dell'applicazione.  # noqa: E501


    :rtype: Problem
    """

    @after_this_request
    def cache_no_store(response):
        """Add the 'no-store' cache value to avoid clients and
           intermediaries to store this response.
        """
        response.headers["Cache-Control"] = "no-store"
        return response

    p = randint(0, 10)

    if p < 7:
        return problem(
            status=200,
            title="Success",
            detail="Il servizio funziona correttamente",
            ext={"result": "ok"},
        )
    if p < 9:
        return problem(
            status=503,
            title="Service Unavailable",
            detail="Questo errore viene ritornato randomicamente.",
            headers={"Retry-After": "1"},
        )

    return problem(
        status=429,
        title="Too Many Requests",
        detail="Questo errore viene ritornato randomicamente.",
    )
