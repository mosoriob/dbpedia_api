# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Statistic(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, statistic=None, id=None, label=None, type=None):  # noqa: E501
        """Statistic - a model defined in OpenAPI

        :param description: The description of this Statistic.  # noqa: E501
        :type description: List[str]
        :param statistic: The statistic of this Statistic.  # noqa: E501
        :type statistic: List[object]
        :param id: The id of this Statistic.  # noqa: E501
        :type id: str
        :param label: The label of this Statistic.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Statistic.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'description': List[str],
            'statistic': List[object],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'statistic': 'statistic',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._description = description
        self._statistic = statistic
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Statistic':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Statistic of this Statistic.  # noqa: E501
        :rtype: Statistic
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Statistic.

        small description  # noqa: E501

        :return: The description of this Statistic.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Statistic.

        small description  # noqa: E501

        :param description: The description of this Statistic.
        :type description: List[str]
        """

        self._description = description

    @property
    def statistic(self):
        """Gets the statistic of this Statistic.

        Description not available  # noqa: E501

        :return: The statistic of this Statistic.
        :rtype: List[object]
        """
        return self._statistic

    @statistic.setter
    def statistic(self, statistic):
        """Sets the statistic of this Statistic.

        Description not available  # noqa: E501

        :param statistic: The statistic of this Statistic.
        :type statistic: List[object]
        """

        self._statistic = statistic

    @property
    def id(self):
        """Gets the id of this Statistic.

        identifier  # noqa: E501

        :return: The id of this Statistic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Statistic.

        identifier  # noqa: E501

        :param id: The id of this Statistic.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Statistic.

        short description of the resource  # noqa: E501

        :return: The label of this Statistic.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Statistic.

        short description of the resource  # noqa: E501

        :param label: The label of this Statistic.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Statistic.

        type of the resource  # noqa: E501

        :return: The type of this Statistic.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Statistic.

        type of the resource  # noqa: E501

        :param type: The type of this Statistic.
        :type type: List[str]
        """

        self._type = type
