# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class LegalCase(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attorney_general=None, description=None, legal_article=None, procedure=None, label=None, system_of_law=None, type=None, code_book=None, ruling=None, solicitor_general=None, developer=None, id=None, judge=None):  # noqa: E501
        """LegalCase - a model defined in OpenAPI

        :param attorney_general: The attorney_general of this LegalCase.  # noqa: E501
        :type attorney_general: List[object]
        :param description: The description of this LegalCase.  # noqa: E501
        :type description: List[str]
        :param legal_article: The legal_article of this LegalCase.  # noqa: E501
        :type legal_article: List[str]
        :param procedure: The procedure of this LegalCase.  # noqa: E501
        :type procedure: List[str]
        :param label: The label of this LegalCase.  # noqa: E501
        :type label: List[str]
        :param system_of_law: The system_of_law of this LegalCase.  # noqa: E501
        :type system_of_law: List[object]
        :param type: The type of this LegalCase.  # noqa: E501
        :type type: List[str]
        :param code_book: The code_book of this LegalCase.  # noqa: E501
        :type code_book: List[str]
        :param ruling: The ruling of this LegalCase.  # noqa: E501
        :type ruling: List[str]
        :param solicitor_general: The solicitor_general of this LegalCase.  # noqa: E501
        :type solicitor_general: List[object]
        :param developer: The developer of this LegalCase.  # noqa: E501
        :type developer: List[object]
        :param id: The id of this LegalCase.  # noqa: E501
        :type id: str
        :param judge: The judge of this LegalCase.  # noqa: E501
        :type judge: List[object]
        """


        self.openapi_types = {
            'attorney_general': List[object],
            'description': List[str],
            'legal_article': List[str],
            'procedure': List[str],
            'label': List[str],
            'system_of_law': List[object],
            'type': List[str],
            'code_book': List[str],
            'ruling': List[str],
            'solicitor_general': List[object],
            'developer': List[object],
            'id': str,
            'judge': List[object]
        }

        self.attribute_map = {
            'attorney_general': 'attorneyGeneral',
            'description': 'description',
            'legal_article': 'legalArticle',
            'procedure': 'procedure',
            'label': 'label',
            'system_of_law': 'systemOfLaw',
            'type': 'type',
            'code_book': 'codeBook',
            'ruling': 'ruling',
            'solicitor_general': 'solicitorGeneral',
            'developer': 'developer',
            'id': 'id',
            'judge': 'judge'
        }

        self._attorney_general = attorney_general
        self._description = description
        self._legal_article = legal_article
        self._procedure = procedure
        self._label = label
        self._system_of_law = system_of_law
        self._type = type
        self._code_book = code_book
        self._ruling = ruling
        self._solicitor_general = solicitor_general
        self._developer = developer
        self._id = id
        self._judge = judge

    @classmethod
    def from_dict(cls, dikt) -> 'LegalCase':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LegalCase of this LegalCase.  # noqa: E501
        :rtype: LegalCase
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attorney_general(self):
        """Gets the attorney_general of this LegalCase.

        Public attorney  # noqa: E501

        :return: The attorney_general of this LegalCase.
        :rtype: List[object]
        """
        return self._attorney_general

    @attorney_general.setter
    def attorney_general(self, attorney_general):
        """Sets the attorney_general of this LegalCase.

        Public attorney  # noqa: E501

        :param attorney_general: The attorney_general of this LegalCase.
        :type attorney_general: List[object]
        """

        self._attorney_general = attorney_general

    @property
    def description(self):
        """Gets the description of this LegalCase.

        small description  # noqa: E501

        :return: The description of this LegalCase.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LegalCase.

        small description  # noqa: E501

        :param description: The description of this LegalCase.
        :type description: List[str]
        """

        self._description = description

    @property
    def legal_article(self):
        """Gets the legal_article of this LegalCase.

        article in code book or statute book referred to in this legal case  # noqa: E501

        :return: The legal_article of this LegalCase.
        :rtype: List[str]
        """
        return self._legal_article

    @legal_article.setter
    def legal_article(self, legal_article):
        """Sets the legal_article of this LegalCase.

        article in code book or statute book referred to in this legal case  # noqa: E501

        :param legal_article: The legal_article of this LegalCase.
        :type legal_article: List[str]
        """

        self._legal_article = legal_article

    @property
    def procedure(self):
        """Gets the procedure of this LegalCase.

        The name designating a formal collection of steps to be taken to complete the case  # noqa: E501

        :return: The procedure of this LegalCase.
        :rtype: List[str]
        """
        return self._procedure

    @procedure.setter
    def procedure(self, procedure):
        """Sets the procedure of this LegalCase.

        The name designating a formal collection of steps to be taken to complete the case  # noqa: E501

        :param procedure: The procedure of this LegalCase.
        :type procedure: List[str]
        """

        self._procedure = procedure

    @property
    def label(self):
        """Gets the label of this LegalCase.

        short description of the resource  # noqa: E501

        :return: The label of this LegalCase.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LegalCase.

        short description of the resource  # noqa: E501

        :param label: The label of this LegalCase.
        :type label: List[str]
        """

        self._label = label

    @property
    def system_of_law(self):
        """Gets the system_of_law of this LegalCase.

        A referral to the relevant system of law  # noqa: E501

        :return: The system_of_law of this LegalCase.
        :rtype: List[object]
        """
        return self._system_of_law

    @system_of_law.setter
    def system_of_law(self, system_of_law):
        """Sets the system_of_law of this LegalCase.

        A referral to the relevant system of law  # noqa: E501

        :param system_of_law: The system_of_law of this LegalCase.
        :type system_of_law: List[object]
        """

        self._system_of_law = system_of_law

    @property
    def type(self):
        """Gets the type of this LegalCase.

        type of the resource  # noqa: E501

        :return: The type of this LegalCase.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LegalCase.

        type of the resource  # noqa: E501

        :param type: The type of this LegalCase.
        :type type: List[str]
        """

        self._type = type

    @property
    def code_book(self):
        """Gets the code_book of this LegalCase.

        code book or statute book referred to in this legal case  # noqa: E501

        :return: The code_book of this LegalCase.
        :rtype: List[str]
        """
        return self._code_book

    @code_book.setter
    def code_book(self, code_book):
        """Sets the code_book of this LegalCase.

        code book or statute book referred to in this legal case  # noqa: E501

        :param code_book: The code_book of this LegalCase.
        :type code_book: List[str]
        """

        self._code_book = code_book

    @property
    def ruling(self):
        """Gets the ruling of this LegalCase.

        Ruling referred to in this legal case  # noqa: E501

        :return: The ruling of this LegalCase.
        :rtype: List[str]
        """
        return self._ruling

    @ruling.setter
    def ruling(self, ruling):
        """Sets the ruling of this LegalCase.

        Ruling referred to in this legal case  # noqa: E501

        :param ruling: The ruling of this LegalCase.
        :type ruling: List[str]
        """

        self._ruling = ruling

    @property
    def solicitor_general(self):
        """Gets the solicitor_general of this LegalCase.

        high-ranking solicitor  # noqa: E501

        :return: The solicitor_general of this LegalCase.
        :rtype: List[object]
        """
        return self._solicitor_general

    @solicitor_general.setter
    def solicitor_general(self, solicitor_general):
        """Sets the solicitor_general of this LegalCase.

        high-ranking solicitor  # noqa: E501

        :param solicitor_general: The solicitor_general of this LegalCase.
        :type solicitor_general: List[object]
        """

        self._solicitor_general = solicitor_general

    @property
    def developer(self):
        """Gets the developer of this LegalCase.

        Description not available  # noqa: E501

        :return: The developer of this LegalCase.
        :rtype: List[object]
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this LegalCase.

        Description not available  # noqa: E501

        :param developer: The developer of this LegalCase.
        :type developer: List[object]
        """

        self._developer = developer

    @property
    def id(self):
        """Gets the id of this LegalCase.

        identifier  # noqa: E501

        :return: The id of this LegalCase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LegalCase.

        identifier  # noqa: E501

        :param id: The id of this LegalCase.
        :type id: str
        """

        self._id = id

    @property
    def judge(self):
        """Gets the judge of this LegalCase.

        leading judge  # noqa: E501

        :return: The judge of this LegalCase.
        :rtype: List[object]
        """
        return self._judge

    @judge.setter
    def judge(self, judge):
        """Sets the judge of this LegalCase.

        leading judge  # noqa: E501

        :param judge: The judge of this LegalCase.
        :type judge: List[object]
        """

        self._judge = judge
