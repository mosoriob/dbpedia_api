# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class HungarySettlement(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sign_name=None, neighbourhood=None, description=None, comitat=None, id=None, label=None, type=None, mayor_title=None):  # noqa: E501
        """HungarySettlement - a model defined in OpenAPI

        :param sign_name: The sign_name of this HungarySettlement.  # noqa: E501
        :type sign_name: List[str]
        :param neighbourhood: The neighbourhood of this HungarySettlement.  # noqa: E501
        :type neighbourhood: List[str]
        :param description: The description of this HungarySettlement.  # noqa: E501
        :type description: List[str]
        :param comitat: The comitat of this HungarySettlement.  # noqa: E501
        :type comitat: List[str]
        :param id: The id of this HungarySettlement.  # noqa: E501
        :type id: str
        :param label: The label of this HungarySettlement.  # noqa: E501
        :type label: List[str]
        :param type: The type of this HungarySettlement.  # noqa: E501
        :type type: List[str]
        :param mayor_title: The mayor_title of this HungarySettlement.  # noqa: E501
        :type mayor_title: List[str]
        """


        self.openapi_types = {
            'sign_name': List[str],
            'neighbourhood': List[str],
            'description': List[str],
            'comitat': List[str],
            'id': str,
            'label': List[str],
            'type': List[str],
            'mayor_title': List[str]
        }

        self.attribute_map = {
            'sign_name': 'signName',
            'neighbourhood': 'neighbourhood',
            'description': 'description',
            'comitat': 'comitat',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'mayor_title': 'mayorTitle'
        }

        self._sign_name = sign_name
        self._neighbourhood = neighbourhood
        self._description = description
        self._comitat = comitat
        self._id = id
        self._label = label
        self._type = type
        self._mayor_title = mayor_title

    @classmethod
    def from_dict(cls, dikt) -> 'HungarySettlement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HungarySettlement of this HungarySettlement.  # noqa: E501
        :rtype: HungarySettlement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sign_name(self):
        """Gets the sign_name of this HungarySettlement.

        Description not available  # noqa: E501

        :return: The sign_name of this HungarySettlement.
        :rtype: List[str]
        """
        return self._sign_name

    @sign_name.setter
    def sign_name(self, sign_name):
        """Sets the sign_name of this HungarySettlement.

        Description not available  # noqa: E501

        :param sign_name: The sign_name of this HungarySettlement.
        :type sign_name: List[str]
        """

        self._sign_name = sign_name

    @property
    def neighbourhood(self):
        """Gets the neighbourhood of this HungarySettlement.

        Description not available  # noqa: E501

        :return: The neighbourhood of this HungarySettlement.
        :rtype: List[str]
        """
        return self._neighbourhood

    @neighbourhood.setter
    def neighbourhood(self, neighbourhood):
        """Sets the neighbourhood of this HungarySettlement.

        Description not available  # noqa: E501

        :param neighbourhood: The neighbourhood of this HungarySettlement.
        :type neighbourhood: List[str]
        """

        self._neighbourhood = neighbourhood

    @property
    def description(self):
        """Gets the description of this HungarySettlement.

        small description  # noqa: E501

        :return: The description of this HungarySettlement.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HungarySettlement.

        small description  # noqa: E501

        :param description: The description of this HungarySettlement.
        :type description: List[str]
        """

        self._description = description

    @property
    def comitat(self):
        """Gets the comitat of this HungarySettlement.

        Description not available  # noqa: E501

        :return: The comitat of this HungarySettlement.
        :rtype: List[str]
        """
        return self._comitat

    @comitat.setter
    def comitat(self, comitat):
        """Sets the comitat of this HungarySettlement.

        Description not available  # noqa: E501

        :param comitat: The comitat of this HungarySettlement.
        :type comitat: List[str]
        """

        self._comitat = comitat

    @property
    def id(self):
        """Gets the id of this HungarySettlement.

        identifier  # noqa: E501

        :return: The id of this HungarySettlement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HungarySettlement.

        identifier  # noqa: E501

        :param id: The id of this HungarySettlement.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this HungarySettlement.

        short description of the resource  # noqa: E501

        :return: The label of this HungarySettlement.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this HungarySettlement.

        short description of the resource  # noqa: E501

        :param label: The label of this HungarySettlement.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this HungarySettlement.

        type of the resource  # noqa: E501

        :return: The type of this HungarySettlement.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HungarySettlement.

        type of the resource  # noqa: E501

        :param type: The type of this HungarySettlement.
        :type type: List[str]
        """

        self._type = type

    @property
    def mayor_title(self):
        """Gets the mayor_title of this HungarySettlement.

        Description not available  # noqa: E501

        :return: The mayor_title of this HungarySettlement.
        :rtype: List[str]
        """
        return self._mayor_title

    @mayor_title.setter
    def mayor_title(self, mayor_title):
        """Sets the mayor_title of this HungarySettlement.

        Description not available  # noqa: E501

        :param mayor_title: The mayor_title of this HungarySettlement.
        :type mayor_title: List[str]
        """

        self._mayor_title = mayor_title
