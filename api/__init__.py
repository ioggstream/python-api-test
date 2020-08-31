"""
Implement the API described by store.yaml OAS spec.




"""

def get_item(item: str):
    raise NotImplementedError


def get_items(limit: int = 10, cursor: str = None):
    raise NotImplementedError


def post_items(body: dict):
    raise NotImplementedError


def get_status():
    raise NotImplementedError
