# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.baseball_team import BaseballTeam  # noqa: E501
from openapi_server.test import BaseTestCase


class TestBaseballTeamController(BaseTestCase):
    """BaseballTeamController integration test stubs"""

    def test_baseballteams_get(self):
        """Test case for baseballteams_get

        List all instances of BaseballTeam
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/baseballteams',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_baseballteams_id_get(self):
        """Test case for baseballteams_id_get

        Get a single BaseballTeam by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/baseballteams/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
