# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Language(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, iso6392_code=None, number_of_speakers=None, language_family=None, sil_code=None, description=None, spoken_in=None, id=None, label=None, type=None, iso6391_code=None, language_code=None, iso6393_code=None):  # noqa: E501
        """Language - a model defined in OpenAPI

        :param iso6392_code: The iso6392_code of this Language.  # noqa: E501
        :type iso6392_code: List[object]
        :param number_of_speakers: The number_of_speakers of this Language.  # noqa: E501
        :type number_of_speakers: List[int]
        :param language_family: The language_family of this Language.  # noqa: E501
        :type language_family: List[object]
        :param sil_code: The sil_code of this Language.  # noqa: E501
        :type sil_code: List[object]
        :param description: The description of this Language.  # noqa: E501
        :type description: List[str]
        :param spoken_in: The spoken_in of this Language.  # noqa: E501
        :type spoken_in: List[object]
        :param id: The id of this Language.  # noqa: E501
        :type id: str
        :param label: The label of this Language.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Language.  # noqa: E501
        :type type: List[str]
        :param iso6391_code: The iso6391_code of this Language.  # noqa: E501
        :type iso6391_code: List[object]
        :param language_code: The language_code of this Language.  # noqa: E501
        :type language_code: List[object]
        :param iso6393_code: The iso6393_code of this Language.  # noqa: E501
        :type iso6393_code: List[object]
        """


        self.openapi_types = {
            'iso6392_code': List[object],
            'number_of_speakers': List[int],
            'language_family': List[object],
            'sil_code': List[object],
            'description': List[str],
            'spoken_in': List[object],
            'id': str,
            'label': List[str],
            'type': List[str],
            'iso6391_code': List[object],
            'language_code': List[object],
            'iso6393_code': List[object]
        }

        self.attribute_map = {
            'iso6392_code': 'iso6392Code',
            'number_of_speakers': 'numberOfSpeakers',
            'language_family': 'languageFamily',
            'sil_code': 'silCode',
            'description': 'description',
            'spoken_in': 'spokenIn',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'iso6391_code': 'iso6391Code',
            'language_code': 'languageCode',
            'iso6393_code': 'iso6393Code'
        }

        self._iso6392_code = iso6392_code
        self._number_of_speakers = number_of_speakers
        self._language_family = language_family
        self._sil_code = sil_code
        self._description = description
        self._spoken_in = spoken_in
        self._id = id
        self._label = label
        self._type = type
        self._iso6391_code = iso6391_code
        self._language_code = language_code
        self._iso6393_code = iso6393_code

    @classmethod
    def from_dict(cls, dikt) -> 'Language':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Language of this Language.  # noqa: E501
        :rtype: Language
        """
        return util.deserialize_model(dikt, cls)

    @property
    def iso6392_code(self):
        """Gets the iso6392_code of this Language.

        Description not available  # noqa: E501

        :return: The iso6392_code of this Language.
        :rtype: List[object]
        """
        return self._iso6392_code

    @iso6392_code.setter
    def iso6392_code(self, iso6392_code):
        """Sets the iso6392_code of this Language.

        Description not available  # noqa: E501

        :param iso6392_code: The iso6392_code of this Language.
        :type iso6392_code: List[object]
        """

        self._iso6392_code = iso6392_code

    @property
    def number_of_speakers(self):
        """Gets the number_of_speakers of this Language.

        Description not available  # noqa: E501

        :return: The number_of_speakers of this Language.
        :rtype: List[int]
        """
        return self._number_of_speakers

    @number_of_speakers.setter
    def number_of_speakers(self, number_of_speakers):
        """Sets the number_of_speakers of this Language.

        Description not available  # noqa: E501

        :param number_of_speakers: The number_of_speakers of this Language.
        :type number_of_speakers: List[int]
        """

        self._number_of_speakers = number_of_speakers

    @property
    def language_family(self):
        """Gets the language_family of this Language.

        Description not available  # noqa: E501

        :return: The language_family of this Language.
        :rtype: List[object]
        """
        return self._language_family

    @language_family.setter
    def language_family(self, language_family):
        """Sets the language_family of this Language.

        Description not available  # noqa: E501

        :param language_family: The language_family of this Language.
        :type language_family: List[object]
        """

        self._language_family = language_family

    @property
    def sil_code(self):
        """Gets the sil_code of this Language.

        Description not available  # noqa: E501

        :return: The sil_code of this Language.
        :rtype: List[object]
        """
        return self._sil_code

    @sil_code.setter
    def sil_code(self, sil_code):
        """Sets the sil_code of this Language.

        Description not available  # noqa: E501

        :param sil_code: The sil_code of this Language.
        :type sil_code: List[object]
        """

        self._sil_code = sil_code

    @property
    def description(self):
        """Gets the description of this Language.

        small description  # noqa: E501

        :return: The description of this Language.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Language.

        small description  # noqa: E501

        :param description: The description of this Language.
        :type description: List[str]
        """

        self._description = description

    @property
    def spoken_in(self):
        """Gets the spoken_in of this Language.

        Description not available  # noqa: E501

        :return: The spoken_in of this Language.
        :rtype: List[object]
        """
        return self._spoken_in

    @spoken_in.setter
    def spoken_in(self, spoken_in):
        """Sets the spoken_in of this Language.

        Description not available  # noqa: E501

        :param spoken_in: The spoken_in of this Language.
        :type spoken_in: List[object]
        """

        self._spoken_in = spoken_in

    @property
    def id(self):
        """Gets the id of this Language.

        identifier  # noqa: E501

        :return: The id of this Language.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Language.

        identifier  # noqa: E501

        :param id: The id of this Language.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Language.

        short description of the resource  # noqa: E501

        :return: The label of this Language.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Language.

        short description of the resource  # noqa: E501

        :param label: The label of this Language.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Language.

        type of the resource  # noqa: E501

        :return: The type of this Language.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Language.

        type of the resource  # noqa: E501

        :param type: The type of this Language.
        :type type: List[str]
        """

        self._type = type

    @property
    def iso6391_code(self):
        """Gets the iso6391_code of this Language.

        Description not available  # noqa: E501

        :return: The iso6391_code of this Language.
        :rtype: List[object]
        """
        return self._iso6391_code

    @iso6391_code.setter
    def iso6391_code(self, iso6391_code):
        """Sets the iso6391_code of this Language.

        Description not available  # noqa: E501

        :param iso6391_code: The iso6391_code of this Language.
        :type iso6391_code: List[object]
        """

        self._iso6391_code = iso6391_code

    @property
    def language_code(self):
        """Gets the language_code of this Language.

        Description not available  # noqa: E501

        :return: The language_code of this Language.
        :rtype: List[object]
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this Language.

        Description not available  # noqa: E501

        :param language_code: The language_code of this Language.
        :type language_code: List[object]
        """

        self._language_code = language_code

    @property
    def iso6393_code(self):
        """Gets the iso6393_code of this Language.

        Description not available  # noqa: E501

        :return: The iso6393_code of this Language.
        :rtype: List[object]
        """
        return self._iso6393_code

    @iso6393_code.setter
    def iso6393_code(self, iso6393_code):
        """Sets the iso6393_code of this Language.

        Description not available  # noqa: E501

        :param iso6393_code: The iso6393_code of this Language.
        :type iso6393_code: List[object]
        """

        self._iso6393_code = iso6393_code
