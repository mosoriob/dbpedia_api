# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.altitude import Altitude  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAltitudeController(BaseTestCase):
    """AltitudeController integration test stubs"""

    def test_altitudes_get(self):
        """Test case for altitudes_get

        List all instances of Altitude
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/altitudes',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_altitudes_id_get(self):
        """Test case for altitudes_id_get

        Get a single Altitude by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/altitudes/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
