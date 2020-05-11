# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.agglomeration import Agglomeration  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAgglomerationController(BaseTestCase):
    """AgglomerationController integration test stubs"""

    def test_agglomerations_get(self):
        """Test case for agglomerations_get

        List all instances of Agglomeration
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/agglomerations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_agglomerations_id_get(self):
        """Test case for agglomerations_id_get

        Get a single Agglomeration by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/agglomerations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
