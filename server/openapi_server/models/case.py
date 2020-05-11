# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Case(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, developer=None, procedure=None, id=None, label=None, type=None):  # noqa: E501
        """Case - a model defined in OpenAPI

        :param description: The description of this Case.  # noqa: E501
        :type description: List[str]
        :param developer: The developer of this Case.  # noqa: E501
        :type developer: List[object]
        :param procedure: The procedure of this Case.  # noqa: E501
        :type procedure: List[str]
        :param id: The id of this Case.  # noqa: E501
        :type id: str
        :param label: The label of this Case.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Case.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'description': List[str],
            'developer': List[object],
            'procedure': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'developer': 'developer',
            'procedure': 'procedure',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._description = description
        self._developer = developer
        self._procedure = procedure
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Case':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Case of this Case.  # noqa: E501
        :rtype: Case
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Case.

        small description  # noqa: E501

        :return: The description of this Case.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Case.

        small description  # noqa: E501

        :param description: The description of this Case.
        :type description: List[str]
        """

        self._description = description

    @property
    def developer(self):
        """Gets the developer of this Case.

        Description not available  # noqa: E501

        :return: The developer of this Case.
        :rtype: List[object]
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this Case.

        Description not available  # noqa: E501

        :param developer: The developer of this Case.
        :type developer: List[object]
        """

        self._developer = developer

    @property
    def procedure(self):
        """Gets the procedure of this Case.

        The name designating a formal collection of steps to be taken to complete the case  # noqa: E501

        :return: The procedure of this Case.
        :rtype: List[str]
        """
        return self._procedure

    @procedure.setter
    def procedure(self, procedure):
        """Sets the procedure of this Case.

        The name designating a formal collection of steps to be taken to complete the case  # noqa: E501

        :param procedure: The procedure of this Case.
        :type procedure: List[str]
        """

        self._procedure = procedure

    @property
    def id(self):
        """Gets the id of this Case.

        identifier  # noqa: E501

        :return: The id of this Case.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Case.

        identifier  # noqa: E501

        :param id: The id of this Case.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Case.

        short description of the resource  # noqa: E501

        :return: The label of this Case.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Case.

        short description of the resource  # noqa: E501

        :param label: The label of this Case.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Case.

        type of the resource  # noqa: E501

        :return: The type of this Case.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Case.

        type of the resource  # noqa: E501

        :param type: The type of this Case.
        :type type: List[str]
        """

        self._type = type
