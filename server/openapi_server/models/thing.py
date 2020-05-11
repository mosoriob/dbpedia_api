# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Thing(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, institution=None, id=None, label=None, type=None):  # noqa: E501
        """Thing - a model defined in OpenAPI

        :param description: The description of this Thing.  # noqa: E501
        :type description: List[str]
        :param institution: The institution of this Thing.  # noqa: E501
        :type institution: List[object]
        :param id: The id of this Thing.  # noqa: E501
        :type id: str
        :param label: The label of this Thing.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Thing.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'description': List[str],
            'institution': List[object],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'institution': 'institution',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._description = description
        self._institution = institution
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Thing':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Thing of this Thing.  # noqa: E501
        :rtype: Thing
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Thing.

        small description  # noqa: E501

        :return: The description of this Thing.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Thing.

        small description  # noqa: E501

        :param description: The description of this Thing.
        :type description: List[str]
        """

        self._description = description

    @property
    def institution(self):
        """Gets the institution of this Thing.

        Description not available  # noqa: E501

        :return: The institution of this Thing.
        :rtype: List[object]
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this Thing.

        Description not available  # noqa: E501

        :param institution: The institution of this Thing.
        :type institution: List[object]
        """

        self._institution = institution

    @property
    def id(self):
        """Gets the id of this Thing.

        identifier  # noqa: E501

        :return: The id of this Thing.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Thing.

        identifier  # noqa: E501

        :param id: The id of this Thing.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Thing.

        short description of the resource  # noqa: E501

        :return: The label of this Thing.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Thing.

        short description of the resource  # noqa: E501

        :param label: The label of this Thing.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Thing.

        type of the resource  # noqa: E501

        :return: The type of this Thing.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Thing.

        type of the resource  # noqa: E501

        :param type: The type of this Thing.
        :type type: List[str]
        """

        self._type = type
