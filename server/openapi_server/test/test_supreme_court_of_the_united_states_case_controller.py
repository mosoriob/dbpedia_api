# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.supreme_court_of_the_united_states_case import SupremeCourtOfTheUnitedStatesCase  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSupremeCourtOfTheUnitedStatesCaseController(BaseTestCase):
    """SupremeCourtOfTheUnitedStatesCaseController integration test stubs"""

    def test_supremecourtoftheunitedstatescases_get(self):
        """Test case for supremecourtoftheunitedstatescases_get

        List all instances of SupremeCourtOfTheUnitedStatesCase
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/supremecourtoftheunitedstatescases',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_supremecourtoftheunitedstatescases_id_get(self):
        """Test case for supremecourtoftheunitedstatescases_id_get

        Get a single SupremeCourtOfTheUnitedStatesCase by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/supremecourtoftheunitedstatescases/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
