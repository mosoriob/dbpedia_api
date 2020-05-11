# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.water_polo_player import WaterPoloPlayer  # noqa: E501
from openapi_server.test import BaseTestCase


class TestWaterPoloPlayerController(BaseTestCase):
    """WaterPoloPlayerController integration test stubs"""

    def test_waterpoloplayers_get(self):
        """Test case for waterpoloplayers_get

        List all instances of WaterPoloPlayer
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/waterpoloplayers',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_waterpoloplayers_id_get(self):
        """Test case for waterpoloplayers_id_get

        Get a single WaterPoloPlayer by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/waterpoloplayers/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
