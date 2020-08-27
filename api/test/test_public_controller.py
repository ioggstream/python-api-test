# coding: utf-8

from __future__ import absolute_import

from flask import json

from api.test import BaseTestCase


class TestPublicController(BaseTestCase):
    """PublicController integration test stubs"""

    def test_post_item(self):
        """Test case for post_item

        Inserisce un oggetto nello store.
        """
        response = self.client.open("/store/v1/echo", method="POST", json={})
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))
        assert "x-ratelimit-limit" in response.headers

    def test_get_items(self):
        """Test case for get_echo

        Recupera un elenco di oggetti dallo store.
        """
        response = self.client.open("/store/v1/items", method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))
        assert "x-ratelimit-limit" in response.headers

    def test_get_item(self):
        """Test case for get_echo

        Recupera un oggetto dallo store.
        """
        response = self.client.open("/store/v1/echo", method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))
        assert "x-ratelimit-limit" in response.headers

    def test_get_status(self):
        """Test case for get_status

        Ritorna lo stato dell'applicazione.
        """
        response = self.client.open("/store/v1/status", method="GET")
        if response.status_code == 200:
            self.assert200(
                response, "Response body is : " + response.data.decode("utf-8")
            )
        elif response.status_code == 503:
            self.assertTrue("random" in response.data.decode("utf-8"))

        assert 'no-store' == response.headers.get('cache-control')


if __name__ == "__main__":
    import unittest

    unittest.main()
