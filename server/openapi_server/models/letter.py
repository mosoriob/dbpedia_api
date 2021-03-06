# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Letter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, unicode=None, description=None, id=None, label=None, type=None):  # noqa: E501
        """Letter - a model defined in OpenAPI

        :param unicode: The unicode of this Letter.  # noqa: E501
        :type unicode: List[str]
        :param description: The description of this Letter.  # noqa: E501
        :type description: List[str]
        :param id: The id of this Letter.  # noqa: E501
        :type id: str
        :param label: The label of this Letter.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Letter.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'unicode': List[str],
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'unicode': 'unicode',
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._unicode = unicode
        self._description = description
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Letter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Letter of this Letter.  # noqa: E501
        :rtype: Letter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def unicode(self):
        """Gets the unicode of this Letter.

        το διεθνές πρότυπο Unicode στοχεύει στην κωδικοποίηση όλων των συστημάτων γραφής που χρησιμοποιούνται στον πλανήτη.  # noqa: E501

        :return: The unicode of this Letter.
        :rtype: List[str]
        """
        return self._unicode

    @unicode.setter
    def unicode(self, unicode):
        """Sets the unicode of this Letter.

        το διεθνές πρότυπο Unicode στοχεύει στην κωδικοποίηση όλων των συστημάτων γραφής που χρησιμοποιούνται στον πλανήτη.  # noqa: E501

        :param unicode: The unicode of this Letter.
        :type unicode: List[str]
        """

        self._unicode = unicode

    @property
    def description(self):
        """Gets the description of this Letter.

        small description  # noqa: E501

        :return: The description of this Letter.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Letter.

        small description  # noqa: E501

        :param description: The description of this Letter.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Letter.

        identifier  # noqa: E501

        :return: The id of this Letter.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Letter.

        identifier  # noqa: E501

        :param id: The id of this Letter.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Letter.

        short description of the resource  # noqa: E501

        :return: The label of this Letter.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Letter.

        short description of the resource  # noqa: E501

        :param label: The label of this Letter.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Letter.

        type of the resource  # noqa: E501

        :return: The type of this Letter.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Letter.

        type of the resource  # noqa: E501

        :param type: The type of this Letter.
        :type type: List[str]
        """

        self._type = type
