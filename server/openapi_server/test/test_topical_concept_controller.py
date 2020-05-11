# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.topical_concept import TopicalConcept  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTopicalConceptController(BaseTestCase):
    """TopicalConceptController integration test stubs"""

    def test_topicalconcepts_get(self):
        """Test case for topicalconcepts_get

        List all instances of TopicalConcept
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/topicalconcepts',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_topicalconcepts_id_get(self):
        """Test case for topicalconcepts_id_get

        Get a single TopicalConcept by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/topicalconcepts/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
