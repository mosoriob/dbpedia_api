# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.hot_spring import HotSpring  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHotSpringController(BaseTestCase):
    """HotSpringController integration test stubs"""

    def test_hotsprings_get(self):
        """Test case for hotsprings_get

        List all instances of HotSpring
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/hotsprings',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hotsprings_id_get(self):
        """Test case for hotsprings_id_get

        Get a single HotSpring by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/hotsprings/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
