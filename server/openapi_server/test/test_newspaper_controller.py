# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.newspaper import Newspaper  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNewspaperController(BaseTestCase):
    """NewspaperController integration test stubs"""

    def test_newspapers_get(self):
        """Test case for newspapers_get

        List all instances of Newspaper
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/newspapers',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_newspapers_id_get(self):
        """Test case for newspapers_id_get

        Get a single Newspaper by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/newspapers/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
