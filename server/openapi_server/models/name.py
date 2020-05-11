# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Name(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, id=None, label=None, type=None):  # noqa: E501
        """Name - a model defined in OpenAPI

        :param description: The description of this Name.  # noqa: E501
        :type description: List[str]
        :param id: The id of this Name.  # noqa: E501
        :type id: str
        :param label: The label of this Name.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Name.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._description = description
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Name':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Name of this Name.  # noqa: E501
        :rtype: Name
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Name.

        small description  # noqa: E501

        :return: The description of this Name.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Name.

        small description  # noqa: E501

        :param description: The description of this Name.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Name.

        identifier  # noqa: E501

        :return: The id of this Name.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Name.

        identifier  # noqa: E501

        :param id: The id of this Name.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Name.

        short description of the resource  # noqa: E501

        :return: The label of this Name.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Name.

        short description of the resource  # noqa: E501

        :param label: The label of this Name.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Name.

        type of the resource  # noqa: E501

        :return: The type of this Name.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Name.

        type of the resource  # noqa: E501

        :param type: The type of this Name.
        :type type: List[str]
        """

        self._type = type
