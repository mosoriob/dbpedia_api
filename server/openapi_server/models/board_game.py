# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class BoardGame(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, number_of_players=None, number_of_professionals=None, number_of_clubs=None, description=None, equipment=None, id=None, label=None, number_of_people_licensed=None, type=None):  # noqa: E501
        """BoardGame - a model defined in OpenAPI

        :param number_of_players: The number_of_players of this BoardGame.  # noqa: E501
        :type number_of_players: List[int]
        :param number_of_professionals: The number_of_professionals of this BoardGame.  # noqa: E501
        :type number_of_professionals: List[int]
        :param number_of_clubs: The number_of_clubs of this BoardGame.  # noqa: E501
        :type number_of_clubs: List[int]
        :param description: The description of this BoardGame.  # noqa: E501
        :type description: List[str]
        :param equipment: The equipment of this BoardGame.  # noqa: E501
        :type equipment: List[object]
        :param id: The id of this BoardGame.  # noqa: E501
        :type id: str
        :param label: The label of this BoardGame.  # noqa: E501
        :type label: List[str]
        :param number_of_people_licensed: The number_of_people_licensed of this BoardGame.  # noqa: E501
        :type number_of_people_licensed: List[int]
        :param type: The type of this BoardGame.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'number_of_players': List[int],
            'number_of_professionals': List[int],
            'number_of_clubs': List[int],
            'description': List[str],
            'equipment': List[object],
            'id': str,
            'label': List[str],
            'number_of_people_licensed': List[int],
            'type': List[str]
        }

        self.attribute_map = {
            'number_of_players': 'numberOfPlayers',
            'number_of_professionals': 'numberOfProfessionals',
            'number_of_clubs': 'numberOfClubs',
            'description': 'description',
            'equipment': 'equipment',
            'id': 'id',
            'label': 'label',
            'number_of_people_licensed': 'numberOfPeopleLicensed',
            'type': 'type'
        }

        self._number_of_players = number_of_players
        self._number_of_professionals = number_of_professionals
        self._number_of_clubs = number_of_clubs
        self._description = description
        self._equipment = equipment
        self._id = id
        self._label = label
        self._number_of_people_licensed = number_of_people_licensed
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'BoardGame':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BoardGame of this BoardGame.  # noqa: E501
        :rtype: BoardGame
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number_of_players(self):
        """Gets the number_of_players of this BoardGame.

        Description not available  # noqa: E501

        :return: The number_of_players of this BoardGame.
        :rtype: List[int]
        """
        return self._number_of_players

    @number_of_players.setter
    def number_of_players(self, number_of_players):
        """Sets the number_of_players of this BoardGame.

        Description not available  # noqa: E501

        :param number_of_players: The number_of_players of this BoardGame.
        :type number_of_players: List[int]
        """

        self._number_of_players = number_of_players

    @property
    def number_of_professionals(self):
        """Gets the number_of_professionals of this BoardGame.

        number of people who earns his living from a specified activity.  # noqa: E501

        :return: The number_of_professionals of this BoardGame.
        :rtype: List[int]
        """
        return self._number_of_professionals

    @number_of_professionals.setter
    def number_of_professionals(self, number_of_professionals):
        """Sets the number_of_professionals of this BoardGame.

        number of people who earns his living from a specified activity.  # noqa: E501

        :param number_of_professionals: The number_of_professionals of this BoardGame.
        :type number_of_professionals: List[int]
        """

        self._number_of_professionals = number_of_professionals

    @property
    def number_of_clubs(self):
        """Gets the number_of_clubs of this BoardGame.

        Description not available  # noqa: E501

        :return: The number_of_clubs of this BoardGame.
        :rtype: List[int]
        """
        return self._number_of_clubs

    @number_of_clubs.setter
    def number_of_clubs(self, number_of_clubs):
        """Sets the number_of_clubs of this BoardGame.

        Description not available  # noqa: E501

        :param number_of_clubs: The number_of_clubs of this BoardGame.
        :type number_of_clubs: List[int]
        """

        self._number_of_clubs = number_of_clubs

    @property
    def description(self):
        """Gets the description of this BoardGame.

        small description  # noqa: E501

        :return: The description of this BoardGame.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BoardGame.

        small description  # noqa: E501

        :param description: The description of this BoardGame.
        :type description: List[str]
        """

        self._description = description

    @property
    def equipment(self):
        """Gets the equipment of this BoardGame.

        Description not available  # noqa: E501

        :return: The equipment of this BoardGame.
        :rtype: List[object]
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this BoardGame.

        Description not available  # noqa: E501

        :param equipment: The equipment of this BoardGame.
        :type equipment: List[object]
        """

        self._equipment = equipment

    @property
    def id(self):
        """Gets the id of this BoardGame.

        identifier  # noqa: E501

        :return: The id of this BoardGame.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BoardGame.

        identifier  # noqa: E501

        :param id: The id of this BoardGame.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this BoardGame.

        short description of the resource  # noqa: E501

        :return: The label of this BoardGame.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this BoardGame.

        short description of the resource  # noqa: E501

        :param label: The label of this BoardGame.
        :type label: List[str]
        """

        self._label = label

    @property
    def number_of_people_licensed(self):
        """Gets the number_of_people_licensed of this BoardGame.

        nombre de personnes ayant une license pour pratiquer cette activité  # noqa: E501

        :return: The number_of_people_licensed of this BoardGame.
        :rtype: List[int]
        """
        return self._number_of_people_licensed

    @number_of_people_licensed.setter
    def number_of_people_licensed(self, number_of_people_licensed):
        """Sets the number_of_people_licensed of this BoardGame.

        nombre de personnes ayant une license pour pratiquer cette activité  # noqa: E501

        :param number_of_people_licensed: The number_of_people_licensed of this BoardGame.
        :type number_of_people_licensed: List[int]
        """

        self._number_of_people_licensed = number_of_people_licensed

    @property
    def type(self):
        """Gets the type of this BoardGame.

        type of the resource  # noqa: E501

        :return: The type of this BoardGame.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BoardGame.

        type of the resource  # noqa: E501

        :param type: The type of this BoardGame.
        :type type: List[str]
        """

        self._type = type
