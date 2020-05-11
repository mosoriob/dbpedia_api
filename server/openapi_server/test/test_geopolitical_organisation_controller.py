# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.geopolitical_organisation import GeopoliticalOrganisation  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGeopoliticalOrganisationController(BaseTestCase):
    """GeopoliticalOrganisationController integration test stubs"""

    def test_geopoliticalorganisations_get(self):
        """Test case for geopoliticalorganisations_get

        List all instances of GeopoliticalOrganisation
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/geopoliticalorganisations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_geopoliticalorganisations_id_get(self):
        """Test case for geopoliticalorganisations_id_get

        Get a single GeopoliticalOrganisation by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/geopoliticalorganisations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
