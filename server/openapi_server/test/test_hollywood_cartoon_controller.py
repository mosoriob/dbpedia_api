# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.hollywood_cartoon import HollywoodCartoon  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHollywoodCartoonController(BaseTestCase):
    """HollywoodCartoonController integration test stubs"""

    def test_hollywoodcartoons_get(self):
        """Test case for hollywoodcartoons_get

        List all instances of HollywoodCartoon
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/hollywoodcartoons',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hollywoodcartoons_id_get(self):
        """Test case for hollywoodcartoons_id_get

        Get a single HollywoodCartoon by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/hollywoodcartoons/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
