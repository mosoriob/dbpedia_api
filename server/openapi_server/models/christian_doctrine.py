# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ChristianDoctrine(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, established=None, primate=None, believers=None, description=None, establishment=None, theology=None, id=None, label=None, type=None):  # noqa: E501
        """ChristianDoctrine - a model defined in OpenAPI

        :param established: The established of this ChristianDoctrine.  # noqa: E501
        :type established: List[str]
        :param primate: The primate of this ChristianDoctrine.  # noqa: E501
        :type primate: List[str]
        :param believers: The believers of this ChristianDoctrine.  # noqa: E501
        :type believers: List[str]
        :param description: The description of this ChristianDoctrine.  # noqa: E501
        :type description: List[str]
        :param establishment: The establishment of this ChristianDoctrine.  # noqa: E501
        :type establishment: List[int]
        :param theology: The theology of this ChristianDoctrine.  # noqa: E501
        :type theology: List[str]
        :param id: The id of this ChristianDoctrine.  # noqa: E501
        :type id: str
        :param label: The label of this ChristianDoctrine.  # noqa: E501
        :type label: List[str]
        :param type: The type of this ChristianDoctrine.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'established': List[str],
            'primate': List[str],
            'believers': List[str],
            'description': List[str],
            'establishment': List[int],
            'theology': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'established': 'established',
            'primate': 'primate',
            'believers': 'believers',
            'description': 'description',
            'establishment': 'establishment',
            'theology': 'theology',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._established = established
        self._primate = primate
        self._believers = believers
        self._description = description
        self._establishment = establishment
        self._theology = theology
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'ChristianDoctrine':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChristianDoctrine of this ChristianDoctrine.  # noqa: E501
        :rtype: ChristianDoctrine
        """
        return util.deserialize_model(dikt, cls)

    @property
    def established(self):
        """Gets the established of this ChristianDoctrine.

        Description not available  # noqa: E501

        :return: The established of this ChristianDoctrine.
        :rtype: List[str]
        """
        return self._established

    @established.setter
    def established(self, established):
        """Sets the established of this ChristianDoctrine.

        Description not available  # noqa: E501

        :param established: The established of this ChristianDoctrine.
        :type established: List[str]
        """

        self._established = established

    @property
    def primate(self):
        """Gets the primate of this ChristianDoctrine.

        Description not available  # noqa: E501

        :return: The primate of this ChristianDoctrine.
        :rtype: List[str]
        """
        return self._primate

    @primate.setter
    def primate(self, primate):
        """Sets the primate of this ChristianDoctrine.

        Description not available  # noqa: E501

        :param primate: The primate of this ChristianDoctrine.
        :type primate: List[str]
        """

        self._primate = primate

    @property
    def believers(self):
        """Gets the believers of this ChristianDoctrine.

        Description not available  # noqa: E501

        :return: The believers of this ChristianDoctrine.
        :rtype: List[str]
        """
        return self._believers

    @believers.setter
    def believers(self, believers):
        """Sets the believers of this ChristianDoctrine.

        Description not available  # noqa: E501

        :param believers: The believers of this ChristianDoctrine.
        :type believers: List[str]
        """

        self._believers = believers

    @property
    def description(self):
        """Gets the description of this ChristianDoctrine.

        small description  # noqa: E501

        :return: The description of this ChristianDoctrine.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChristianDoctrine.

        small description  # noqa: E501

        :param description: The description of this ChristianDoctrine.
        :type description: List[str]
        """

        self._description = description

    @property
    def establishment(self):
        """Gets the establishment of this ChristianDoctrine.

        Description not available  # noqa: E501

        :return: The establishment of this ChristianDoctrine.
        :rtype: List[int]
        """
        return self._establishment

    @establishment.setter
    def establishment(self, establishment):
        """Sets the establishment of this ChristianDoctrine.

        Description not available  # noqa: E501

        :param establishment: The establishment of this ChristianDoctrine.
        :type establishment: List[int]
        """

        self._establishment = establishment

    @property
    def theology(self):
        """Gets the theology of this ChristianDoctrine.

        Description not available  # noqa: E501

        :return: The theology of this ChristianDoctrine.
        :rtype: List[str]
        """
        return self._theology

    @theology.setter
    def theology(self, theology):
        """Sets the theology of this ChristianDoctrine.

        Description not available  # noqa: E501

        :param theology: The theology of this ChristianDoctrine.
        :type theology: List[str]
        """

        self._theology = theology

    @property
    def id(self):
        """Gets the id of this ChristianDoctrine.

        identifier  # noqa: E501

        :return: The id of this ChristianDoctrine.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChristianDoctrine.

        identifier  # noqa: E501

        :param id: The id of this ChristianDoctrine.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this ChristianDoctrine.

        short description of the resource  # noqa: E501

        :return: The label of this ChristianDoctrine.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ChristianDoctrine.

        short description of the resource  # noqa: E501

        :param label: The label of this ChristianDoctrine.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this ChristianDoctrine.

        type of the resource  # noqa: E501

        :return: The type of this ChristianDoctrine.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChristianDoctrine.

        type of the resource  # noqa: E501

        :param type: The type of this ChristianDoctrine.
        :type type: List[str]
        """

        self._type = type
