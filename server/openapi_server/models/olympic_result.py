# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class OlympicResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, other_appearances=None, number_of_officials=None, description=None, competition=None, summer_appearances=None, label=None, type=None, winter_appearances=None, number_of_gold_medals_won=None, number_of_competitors=None, number_of_bronze_medals_won=None, games=None, number_of_silver_medals_won=None, oldcode=None, id=None, national_olympic_committee=None, rank_in_final_medal_count=None, flag_bearer=None):  # noqa: E501
        """OlympicResult - a model defined in OpenAPI

        :param other_appearances: The other_appearances of this OlympicResult.  # noqa: E501
        :type other_appearances: List[object]
        :param number_of_officials: The number_of_officials of this OlympicResult.  # noqa: E501
        :type number_of_officials: List[int]
        :param description: The description of this OlympicResult.  # noqa: E501
        :type description: List[str]
        :param competition: The competition of this OlympicResult.  # noqa: E501
        :type competition: List[object]
        :param summer_appearances: The summer_appearances of this OlympicResult.  # noqa: E501
        :type summer_appearances: List[object]
        :param label: The label of this OlympicResult.  # noqa: E501
        :type label: List[str]
        :param type: The type of this OlympicResult.  # noqa: E501
        :type type: List[str]
        :param winter_appearances: The winter_appearances of this OlympicResult.  # noqa: E501
        :type winter_appearances: List[object]
        :param number_of_gold_medals_won: The number_of_gold_medals_won of this OlympicResult.  # noqa: E501
        :type number_of_gold_medals_won: List[int]
        :param number_of_competitors: The number_of_competitors of this OlympicResult.  # noqa: E501
        :type number_of_competitors: List[int]
        :param number_of_bronze_medals_won: The number_of_bronze_medals_won of this OlympicResult.  # noqa: E501
        :type number_of_bronze_medals_won: List[int]
        :param games: The games of this OlympicResult.  # noqa: E501
        :type games: List[str]
        :param number_of_silver_medals_won: The number_of_silver_medals_won of this OlympicResult.  # noqa: E501
        :type number_of_silver_medals_won: List[int]
        :param oldcode: The oldcode of this OlympicResult.  # noqa: E501
        :type oldcode: List[str]
        :param id: The id of this OlympicResult.  # noqa: E501
        :type id: str
        :param national_olympic_committee: The national_olympic_committee of this OlympicResult.  # noqa: E501
        :type national_olympic_committee: List[object]
        :param rank_in_final_medal_count: The rank_in_final_medal_count of this OlympicResult.  # noqa: E501
        :type rank_in_final_medal_count: List[int]
        :param flag_bearer: The flag_bearer of this OlympicResult.  # noqa: E501
        :type flag_bearer: List[object]
        """


        self.openapi_types = {
            'other_appearances': List[object],
            'number_of_officials': List[int],
            'description': List[str],
            'competition': List[object],
            'summer_appearances': List[object],
            'label': List[str],
            'type': List[str],
            'winter_appearances': List[object],
            'number_of_gold_medals_won': List[int],
            'number_of_competitors': List[int],
            'number_of_bronze_medals_won': List[int],
            'games': List[str],
            'number_of_silver_medals_won': List[int],
            'oldcode': List[str],
            'id': str,
            'national_olympic_committee': List[object],
            'rank_in_final_medal_count': List[int],
            'flag_bearer': List[object]
        }

        self.attribute_map = {
            'other_appearances': 'otherAppearances',
            'number_of_officials': 'numberOfOfficials',
            'description': 'description',
            'competition': 'competition',
            'summer_appearances': 'summerAppearances',
            'label': 'label',
            'type': 'type',
            'winter_appearances': 'winterAppearances',
            'number_of_gold_medals_won': 'numberOfGoldMedalsWon',
            'number_of_competitors': 'numberOfCompetitors',
            'number_of_bronze_medals_won': 'numberOfBronzeMedalsWon',
            'games': 'games',
            'number_of_silver_medals_won': 'numberOfSilverMedalsWon',
            'oldcode': 'oldcode',
            'id': 'id',
            'national_olympic_committee': 'nationalOlympicCommittee',
            'rank_in_final_medal_count': 'rankInFinalMedalCount',
            'flag_bearer': 'flagBearer'
        }

        self._other_appearances = other_appearances
        self._number_of_officials = number_of_officials
        self._description = description
        self._competition = competition
        self._summer_appearances = summer_appearances
        self._label = label
        self._type = type
        self._winter_appearances = winter_appearances
        self._number_of_gold_medals_won = number_of_gold_medals_won
        self._number_of_competitors = number_of_competitors
        self._number_of_bronze_medals_won = number_of_bronze_medals_won
        self._games = games
        self._number_of_silver_medals_won = number_of_silver_medals_won
        self._oldcode = oldcode
        self._id = id
        self._national_olympic_committee = national_olympic_committee
        self._rank_in_final_medal_count = rank_in_final_medal_count
        self._flag_bearer = flag_bearer

    @classmethod
    def from_dict(cls, dikt) -> 'OlympicResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OlympicResult of this OlympicResult.  # noqa: E501
        :rtype: OlympicResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def other_appearances(self):
        """Gets the other_appearances of this OlympicResult.

        Description not available  # noqa: E501

        :return: The other_appearances of this OlympicResult.
        :rtype: List[object]
        """
        return self._other_appearances

    @other_appearances.setter
    def other_appearances(self, other_appearances):
        """Sets the other_appearances of this OlympicResult.

        Description not available  # noqa: E501

        :param other_appearances: The other_appearances of this OlympicResult.
        :type other_appearances: List[object]
        """

        self._other_appearances = other_appearances

    @property
    def number_of_officials(self):
        """Gets the number_of_officials of this OlympicResult.

        Description not available  # noqa: E501

        :return: The number_of_officials of this OlympicResult.
        :rtype: List[int]
        """
        return self._number_of_officials

    @number_of_officials.setter
    def number_of_officials(self, number_of_officials):
        """Sets the number_of_officials of this OlympicResult.

        Description not available  # noqa: E501

        :param number_of_officials: The number_of_officials of this OlympicResult.
        :type number_of_officials: List[int]
        """

        self._number_of_officials = number_of_officials

    @property
    def description(self):
        """Gets the description of this OlympicResult.

        small description  # noqa: E501

        :return: The description of this OlympicResult.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OlympicResult.

        small description  # noqa: E501

        :param description: The description of this OlympicResult.
        :type description: List[str]
        """

        self._description = description

    @property
    def competition(self):
        """Gets the competition of this OlympicResult.

        Description not available  # noqa: E501

        :return: The competition of this OlympicResult.
        :rtype: List[object]
        """
        return self._competition

    @competition.setter
    def competition(self, competition):
        """Sets the competition of this OlympicResult.

        Description not available  # noqa: E501

        :param competition: The competition of this OlympicResult.
        :type competition: List[object]
        """

        self._competition = competition

    @property
    def summer_appearances(self):
        """Gets the summer_appearances of this OlympicResult.

        Description not available  # noqa: E501

        :return: The summer_appearances of this OlympicResult.
        :rtype: List[object]
        """
        return self._summer_appearances

    @summer_appearances.setter
    def summer_appearances(self, summer_appearances):
        """Sets the summer_appearances of this OlympicResult.

        Description not available  # noqa: E501

        :param summer_appearances: The summer_appearances of this OlympicResult.
        :type summer_appearances: List[object]
        """

        self._summer_appearances = summer_appearances

    @property
    def label(self):
        """Gets the label of this OlympicResult.

        short description of the resource  # noqa: E501

        :return: The label of this OlympicResult.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this OlympicResult.

        short description of the resource  # noqa: E501

        :param label: The label of this OlympicResult.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this OlympicResult.

        type of the resource  # noqa: E501

        :return: The type of this OlympicResult.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OlympicResult.

        type of the resource  # noqa: E501

        :param type: The type of this OlympicResult.
        :type type: List[str]
        """

        self._type = type

    @property
    def winter_appearances(self):
        """Gets the winter_appearances of this OlympicResult.

        Description not available  # noqa: E501

        :return: The winter_appearances of this OlympicResult.
        :rtype: List[object]
        """
        return self._winter_appearances

    @winter_appearances.setter
    def winter_appearances(self, winter_appearances):
        """Sets the winter_appearances of this OlympicResult.

        Description not available  # noqa: E501

        :param winter_appearances: The winter_appearances of this OlympicResult.
        :type winter_appearances: List[object]
        """

        self._winter_appearances = winter_appearances

    @property
    def number_of_gold_medals_won(self):
        """Gets the number_of_gold_medals_won of this OlympicResult.

        Description not available  # noqa: E501

        :return: The number_of_gold_medals_won of this OlympicResult.
        :rtype: List[int]
        """
        return self._number_of_gold_medals_won

    @number_of_gold_medals_won.setter
    def number_of_gold_medals_won(self, number_of_gold_medals_won):
        """Sets the number_of_gold_medals_won of this OlympicResult.

        Description not available  # noqa: E501

        :param number_of_gold_medals_won: The number_of_gold_medals_won of this OlympicResult.
        :type number_of_gold_medals_won: List[int]
        """

        self._number_of_gold_medals_won = number_of_gold_medals_won

    @property
    def number_of_competitors(self):
        """Gets the number_of_competitors of this OlympicResult.

        Description not available  # noqa: E501

        :return: The number_of_competitors of this OlympicResult.
        :rtype: List[int]
        """
        return self._number_of_competitors

    @number_of_competitors.setter
    def number_of_competitors(self, number_of_competitors):
        """Sets the number_of_competitors of this OlympicResult.

        Description not available  # noqa: E501

        :param number_of_competitors: The number_of_competitors of this OlympicResult.
        :type number_of_competitors: List[int]
        """

        self._number_of_competitors = number_of_competitors

    @property
    def number_of_bronze_medals_won(self):
        """Gets the number_of_bronze_medals_won of this OlympicResult.

        Description not available  # noqa: E501

        :return: The number_of_bronze_medals_won of this OlympicResult.
        :rtype: List[int]
        """
        return self._number_of_bronze_medals_won

    @number_of_bronze_medals_won.setter
    def number_of_bronze_medals_won(self, number_of_bronze_medals_won):
        """Sets the number_of_bronze_medals_won of this OlympicResult.

        Description not available  # noqa: E501

        :param number_of_bronze_medals_won: The number_of_bronze_medals_won of this OlympicResult.
        :type number_of_bronze_medals_won: List[int]
        """

        self._number_of_bronze_medals_won = number_of_bronze_medals_won

    @property
    def games(self):
        """Gets the games of this OlympicResult.

        Description not available  # noqa: E501

        :return: The games of this OlympicResult.
        :rtype: List[str]
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this OlympicResult.

        Description not available  # noqa: E501

        :param games: The games of this OlympicResult.
        :type games: List[str]
        """

        self._games = games

    @property
    def number_of_silver_medals_won(self):
        """Gets the number_of_silver_medals_won of this OlympicResult.

        Description not available  # noqa: E501

        :return: The number_of_silver_medals_won of this OlympicResult.
        :rtype: List[int]
        """
        return self._number_of_silver_medals_won

    @number_of_silver_medals_won.setter
    def number_of_silver_medals_won(self, number_of_silver_medals_won):
        """Sets the number_of_silver_medals_won of this OlympicResult.

        Description not available  # noqa: E501

        :param number_of_silver_medals_won: The number_of_silver_medals_won of this OlympicResult.
        :type number_of_silver_medals_won: List[int]
        """

        self._number_of_silver_medals_won = number_of_silver_medals_won

    @property
    def oldcode(self):
        """Gets the oldcode of this OlympicResult.

        Description not available  # noqa: E501

        :return: The oldcode of this OlympicResult.
        :rtype: List[str]
        """
        return self._oldcode

    @oldcode.setter
    def oldcode(self, oldcode):
        """Sets the oldcode of this OlympicResult.

        Description not available  # noqa: E501

        :param oldcode: The oldcode of this OlympicResult.
        :type oldcode: List[str]
        """

        self._oldcode = oldcode

    @property
    def id(self):
        """Gets the id of this OlympicResult.

        identifier  # noqa: E501

        :return: The id of this OlympicResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OlympicResult.

        identifier  # noqa: E501

        :param id: The id of this OlympicResult.
        :type id: str
        """

        self._id = id

    @property
    def national_olympic_committee(self):
        """Gets the national_olympic_committee of this OlympicResult.

        Description not available  # noqa: E501

        :return: The national_olympic_committee of this OlympicResult.
        :rtype: List[object]
        """
        return self._national_olympic_committee

    @national_olympic_committee.setter
    def national_olympic_committee(self, national_olympic_committee):
        """Sets the national_olympic_committee of this OlympicResult.

        Description not available  # noqa: E501

        :param national_olympic_committee: The national_olympic_committee of this OlympicResult.
        :type national_olympic_committee: List[object]
        """

        self._national_olympic_committee = national_olympic_committee

    @property
    def rank_in_final_medal_count(self):
        """Gets the rank_in_final_medal_count of this OlympicResult.

        Description not available  # noqa: E501

        :return: The rank_in_final_medal_count of this OlympicResult.
        :rtype: List[int]
        """
        return self._rank_in_final_medal_count

    @rank_in_final_medal_count.setter
    def rank_in_final_medal_count(self, rank_in_final_medal_count):
        """Sets the rank_in_final_medal_count of this OlympicResult.

        Description not available  # noqa: E501

        :param rank_in_final_medal_count: The rank_in_final_medal_count of this OlympicResult.
        :type rank_in_final_medal_count: List[int]
        """

        self._rank_in_final_medal_count = rank_in_final_medal_count

    @property
    def flag_bearer(self):
        """Gets the flag_bearer of this OlympicResult.

        Description not available  # noqa: E501

        :return: The flag_bearer of this OlympicResult.
        :rtype: List[object]
        """
        return self._flag_bearer

    @flag_bearer.setter
    def flag_bearer(self, flag_bearer):
        """Sets the flag_bearer of this OlympicResult.

        Description not available  # noqa: E501

        :param flag_bearer: The flag_bearer of this OlympicResult.
        :type flag_bearer: List[object]
        """

        self._flag_bearer = flag_bearer
