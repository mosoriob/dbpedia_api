# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.radio_controlled_racing_league import RadioControlledRacingLeague  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRadioControlledRacingLeagueController(BaseTestCase):
    """RadioControlledRacingLeagueController integration test stubs"""

    def test_radiocontrolledracingleagues_get(self):
        """Test case for radiocontrolledracingleagues_get

        List all instances of RadioControlledRacingLeague
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/radiocontrolledracingleagues',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_radiocontrolledracingleagues_id_get(self):
        """Test case for radiocontrolledracingleagues_id_get

        Get a single RadioControlledRacingLeague by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v0.0.1/radiocontrolledracingleagues/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
