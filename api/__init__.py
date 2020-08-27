"""
Implement the API described by store.yaml OAS spec.




"""

def get_item(item: str):
    raise NotImplementedError


def get_items(limit: int = 10, cursor: str = None):
    raise NotImplementedError


def post_item(body: dict):
    raise NotImplementedError


def status():
    raise NotImplementedError
