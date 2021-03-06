# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class BoxingStyle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, number_of_players=None, number_of_professionals=None, number_of_clubs=None, current_world_champion=None, first_olympic_event=None, footedness=None, description=None, equipment=None, id=None, label=None, number_of_people_licensed=None, type=None):  # noqa: E501
        """BoxingStyle - a model defined in OpenAPI

        :param number_of_players: The number_of_players of this BoxingStyle.  # noqa: E501
        :type number_of_players: List[int]
        :param number_of_professionals: The number_of_professionals of this BoxingStyle.  # noqa: E501
        :type number_of_professionals: List[int]
        :param number_of_clubs: The number_of_clubs of this BoxingStyle.  # noqa: E501
        :type number_of_clubs: List[int]
        :param current_world_champion: The current_world_champion of this BoxingStyle.  # noqa: E501
        :type current_world_champion: List[object]
        :param first_olympic_event: The first_olympic_event of this BoxingStyle.  # noqa: E501
        :type first_olympic_event: List[object]
        :param footedness: The footedness of this BoxingStyle.  # noqa: E501
        :type footedness: List[object]
        :param description: The description of this BoxingStyle.  # noqa: E501
        :type description: List[str]
        :param equipment: The equipment of this BoxingStyle.  # noqa: E501
        :type equipment: List[object]
        :param id: The id of this BoxingStyle.  # noqa: E501
        :type id: str
        :param label: The label of this BoxingStyle.  # noqa: E501
        :type label: List[str]
        :param number_of_people_licensed: The number_of_people_licensed of this BoxingStyle.  # noqa: E501
        :type number_of_people_licensed: List[int]
        :param type: The type of this BoxingStyle.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'number_of_players': List[int],
            'number_of_professionals': List[int],
            'number_of_clubs': List[int],
            'current_world_champion': List[object],
            'first_olympic_event': List[object],
            'footedness': List[object],
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
            'current_world_champion': 'currentWorldChampion',
            'first_olympic_event': 'firstOlympicEvent',
            'footedness': 'footedness',
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
        self._current_world_champion = current_world_champion
        self._first_olympic_event = first_olympic_event
        self._footedness = footedness
        self._description = description
        self._equipment = equipment
        self._id = id
        self._label = label
        self._number_of_people_licensed = number_of_people_licensed
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'BoxingStyle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BoxingStyle of this BoxingStyle.  # noqa: E501
        :rtype: BoxingStyle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number_of_players(self):
        """Gets the number_of_players of this BoxingStyle.

        Description not available  # noqa: E501

        :return: The number_of_players of this BoxingStyle.
        :rtype: List[int]
        """
        return self._number_of_players

    @number_of_players.setter
    def number_of_players(self, number_of_players):
        """Sets the number_of_players of this BoxingStyle.

        Description not available  # noqa: E501

        :param number_of_players: The number_of_players of this BoxingStyle.
        :type number_of_players: List[int]
        """

        self._number_of_players = number_of_players

    @property
    def number_of_professionals(self):
        """Gets the number_of_professionals of this BoxingStyle.

        number of people who earns his living from a specified activity.  # noqa: E501

        :return: The number_of_professionals of this BoxingStyle.
        :rtype: List[int]
        """
        return self._number_of_professionals

    @number_of_professionals.setter
    def number_of_professionals(self, number_of_professionals):
        """Sets the number_of_professionals of this BoxingStyle.

        number of people who earns his living from a specified activity.  # noqa: E501

        :param number_of_professionals: The number_of_professionals of this BoxingStyle.
        :type number_of_professionals: List[int]
        """

        self._number_of_professionals = number_of_professionals

    @property
    def number_of_clubs(self):
        """Gets the number_of_clubs of this BoxingStyle.

        Description not available  # noqa: E501

        :return: The number_of_clubs of this BoxingStyle.
        :rtype: List[int]
        """
        return self._number_of_clubs

    @number_of_clubs.setter
    def number_of_clubs(self, number_of_clubs):
        """Sets the number_of_clubs of this BoxingStyle.

        Description not available  # noqa: E501

        :param number_of_clubs: The number_of_clubs of this BoxingStyle.
        :type number_of_clubs: List[int]
        """

        self._number_of_clubs = number_of_clubs

    @property
    def current_world_champion(self):
        """Gets the current_world_champion of this BoxingStyle.

        Description not available  # noqa: E501

        :return: The current_world_champion of this BoxingStyle.
        :rtype: List[object]
        """
        return self._current_world_champion

    @current_world_champion.setter
    def current_world_champion(self, current_world_champion):
        """Sets the current_world_champion of this BoxingStyle.

        Description not available  # noqa: E501

        :param current_world_champion: The current_world_champion of this BoxingStyle.
        :type current_world_champion: List[object]
        """

        self._current_world_champion = current_world_champion

    @property
    def first_olympic_event(self):
        """Gets the first_olympic_event of this BoxingStyle.

        Description not available  # noqa: E501

        :return: The first_olympic_event of this BoxingStyle.
        :rtype: List[object]
        """
        return self._first_olympic_event

    @first_olympic_event.setter
    def first_olympic_event(self, first_olympic_event):
        """Sets the first_olympic_event of this BoxingStyle.

        Description not available  # noqa: E501

        :param first_olympic_event: The first_olympic_event of this BoxingStyle.
        :type first_olympic_event: List[object]
        """

        self._first_olympic_event = first_olympic_event

    @property
    def footedness(self):
        """Gets the footedness of this BoxingStyle.

        a preference to put one's left or right foot forward in surfing, wakeboarding, skateboarding, wakeskating, snowboarding and mountainboarding. The term is sometimes applied to the foot a footballer uses to kick.  # noqa: E501

        :return: The footedness of this BoxingStyle.
        :rtype: List[object]
        """
        return self._footedness

    @footedness.setter
    def footedness(self, footedness):
        """Sets the footedness of this BoxingStyle.

        a preference to put one's left or right foot forward in surfing, wakeboarding, skateboarding, wakeskating, snowboarding and mountainboarding. The term is sometimes applied to the foot a footballer uses to kick.  # noqa: E501

        :param footedness: The footedness of this BoxingStyle.
        :type footedness: List[object]
        """

        self._footedness = footedness

    @property
    def description(self):
        """Gets the description of this BoxingStyle.

        small description  # noqa: E501

        :return: The description of this BoxingStyle.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BoxingStyle.

        small description  # noqa: E501

        :param description: The description of this BoxingStyle.
        :type description: List[str]
        """

        self._description = description

    @property
    def equipment(self):
        """Gets the equipment of this BoxingStyle.

        Description not available  # noqa: E501

        :return: The equipment of this BoxingStyle.
        :rtype: List[object]
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this BoxingStyle.

        Description not available  # noqa: E501

        :param equipment: The equipment of this BoxingStyle.
        :type equipment: List[object]
        """

        self._equipment = equipment

    @property
    def id(self):
        """Gets the id of this BoxingStyle.

        identifier  # noqa: E501

        :return: The id of this BoxingStyle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BoxingStyle.

        identifier  # noqa: E501

        :param id: The id of this BoxingStyle.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this BoxingStyle.

        short description of the resource  # noqa: E501

        :return: The label of this BoxingStyle.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this BoxingStyle.

        short description of the resource  # noqa: E501

        :param label: The label of this BoxingStyle.
        :type label: List[str]
        """

        self._label = label

    @property
    def number_of_people_licensed(self):
        """Gets the number_of_people_licensed of this BoxingStyle.

        nombre de personnes ayant une license pour pratiquer cette activité  # noqa: E501

        :return: The number_of_people_licensed of this BoxingStyle.
        :rtype: List[int]
        """
        return self._number_of_people_licensed

    @number_of_people_licensed.setter
    def number_of_people_licensed(self, number_of_people_licensed):
        """Sets the number_of_people_licensed of this BoxingStyle.

        nombre de personnes ayant une license pour pratiquer cette activité  # noqa: E501

        :param number_of_people_licensed: The number_of_people_licensed of this BoxingStyle.
        :type number_of_people_licensed: List[int]
        """

        self._number_of_people_licensed = number_of_people_licensed

    @property
    def type(self):
        """Gets the type of this BoxingStyle.

        type of the resource  # noqa: E501

        :return: The type of this BoxingStyle.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BoxingStyle.

        type of the resource  # noqa: E501

        :param type: The type of this BoxingStyle.
        :type type: List[str]
        """

        self._type = type
