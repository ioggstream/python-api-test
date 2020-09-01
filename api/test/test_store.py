from api.store import MongoStore, Store


class TestStore(object):
    def setup(self):
        self.store = Store()
        self.store.add("1", {"1": 1})
        self.store.add("r", {"r": "r"})

    def test_add(self):
        i = {"2": 2}
        self.store.add("2", i)
        assert self.store.get("2") == i

    def test_remove(self):
        self.store.remove("r")
        assert self.store.get("r") == None

    def test_get(self):
        assert self.store.get("1") == {"1": 1}
        assert self.store.get("missing") == None

    def test_list(self):
        assert "1" in self.store.list()


class TestMongoStore(TestStore):
    """
    This class repeats all the tests in TestStore on the other driver.

    I'm not using fixture because the audience may not know pytest.
    """

    def setup(self):
        self.store = MongoStore(host="192.168.32.2", username="root", password="secret")
        self.store.add("1", {"1": 1})
        self.store.add("r", {"r": "r"})
