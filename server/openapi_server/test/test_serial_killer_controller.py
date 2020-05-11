# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.serial_killer import SerialKiller  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSerialKillerController(BaseTestCase):
    """SerialKillerController integration test stubs"""

    def test_serialkillers_get(self):
        """Test case for serialkillers_get

        List all instances of SerialKiller
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/serialkillers',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_serialkillers_id_get(self):
        """Test case for serialkillers_id_get

        Get a single SerialKiller by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/serialkillers/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
