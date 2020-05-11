# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.handball_team import HandballTeam  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHandballTeamController(BaseTestCase):
    """HandballTeamController integration test stubs"""

    def test_handballteams_get(self):
        """Test case for handballteams_get

        List all instances of HandballTeam
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/handballteams',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_handballteams_id_get(self):
        """Test case for handballteams_id_get

        Get a single HandballTeam by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/handballteams/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
