# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.field_hockey_league import FieldHockeyLeague  # noqa: E501
from openapi_server.test import BaseTestCase


class TestFieldHockeyLeagueController(BaseTestCase):
    """FieldHockeyLeagueController integration test stubs"""

    def test_fieldhockeyleagues_get(self):
        """Test case for fieldhockeyleagues_get

        List all instances of FieldHockeyLeague
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/fieldhockeyleagues',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fieldhockeyleagues_id_get(self):
        """Test case for fieldhockeyleagues_id_get

        Get a single FieldHockeyLeague by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/fieldhockeyleagues/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
