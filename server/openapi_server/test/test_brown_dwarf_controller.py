# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.brown_dwarf import BrownDwarf  # noqa: E501
from openapi_server.test import BaseTestCase


class TestBrownDwarfController(BaseTestCase):
    """BrownDwarfController integration test stubs"""

    def test_browndwarfs_get(self):
        """Test case for browndwarfs_get

        List all instances of BrownDwarf
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/browndwarfs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_browndwarfs_id_get(self):
        """Test case for browndwarfs_id_get

        Get a single BrownDwarf by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/browndwarfs/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
