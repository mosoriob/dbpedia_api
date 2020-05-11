# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.lacrosse_league import LacrosseLeague  # noqa: E501
from openapi_server.test import BaseTestCase


class TestLacrosseLeagueController(BaseTestCase):
    """LacrosseLeagueController integration test stubs"""

    def test_lacrosseleagues_get(self):
        """Test case for lacrosseleagues_get

        List all instances of LacrosseLeague
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/lacrosseleagues',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_lacrosseleagues_id_get(self):
        """Test case for lacrosseleagues_id_get

        Get a single LacrosseLeague by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/lacrosseleagues/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
