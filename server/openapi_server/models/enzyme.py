# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Enzyme(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entrezgene=None, symbol=None, description=None, label=None, type=None, ensembl=None, refseqprotein=None, omim=None, refseqmrna=None, hgncid=None, mgiid=None, ec_number=None, id=None, uniprot=None):  # noqa: E501
        """Enzyme - a model defined in OpenAPI

        :param entrezgene: The entrezgene of this Enzyme.  # noqa: E501
        :type entrezgene: List[str]
        :param symbol: The symbol of this Enzyme.  # noqa: E501
        :type symbol: List[str]
        :param description: The description of this Enzyme.  # noqa: E501
        :type description: List[str]
        :param label: The label of this Enzyme.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Enzyme.  # noqa: E501
        :type type: List[str]
        :param ensembl: The ensembl of this Enzyme.  # noqa: E501
        :type ensembl: List[str]
        :param refseqprotein: The refseqprotein of this Enzyme.  # noqa: E501
        :type refseqprotein: List[str]
        :param omim: The omim of this Enzyme.  # noqa: E501
        :type omim: List[int]
        :param refseqmrna: The refseqmrna of this Enzyme.  # noqa: E501
        :type refseqmrna: List[str]
        :param hgncid: The hgncid of this Enzyme.  # noqa: E501
        :type hgncid: List[str]
        :param mgiid: The mgiid of this Enzyme.  # noqa: E501
        :type mgiid: List[str]
        :param ec_number: The ec_number of this Enzyme.  # noqa: E501
        :type ec_number: List[str]
        :param id: The id of this Enzyme.  # noqa: E501
        :type id: str
        :param uniprot: The uniprot of this Enzyme.  # noqa: E501
        :type uniprot: List[str]
        """


        self.openapi_types = {
            'entrezgene': List[str],
            'symbol': List[str],
            'description': List[str],
            'label': List[str],
            'type': List[str],
            'ensembl': List[str],
            'refseqprotein': List[str],
            'omim': List[int],
            'refseqmrna': List[str],
            'hgncid': List[str],
            'mgiid': List[str],
            'ec_number': List[str],
            'id': str,
            'uniprot': List[str]
        }

        self.attribute_map = {
            'entrezgene': 'entrezgene',
            'symbol': 'symbol',
            'description': 'description',
            'label': 'label',
            'type': 'type',
            'ensembl': 'ensembl',
            'refseqprotein': 'refseqprotein',
            'omim': 'omim',
            'refseqmrna': 'refseqmrna',
            'hgncid': 'hgncid',
            'mgiid': 'mgiid',
            'ec_number': 'ecNumber',
            'id': 'id',
            'uniprot': 'uniprot'
        }

        self._entrezgene = entrezgene
        self._symbol = symbol
        self._description = description
        self._label = label
        self._type = type
        self._ensembl = ensembl
        self._refseqprotein = refseqprotein
        self._omim = omim
        self._refseqmrna = refseqmrna
        self._hgncid = hgncid
        self._mgiid = mgiid
        self._ec_number = ec_number
        self._id = id
        self._uniprot = uniprot

    @classmethod
    def from_dict(cls, dikt) -> 'Enzyme':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Enzyme of this Enzyme.  # noqa: E501
        :rtype: Enzyme
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entrezgene(self):
        """Gets the entrezgene of this Enzyme.

        Description not available  # noqa: E501

        :return: The entrezgene of this Enzyme.
        :rtype: List[str]
        """
        return self._entrezgene

    @entrezgene.setter
    def entrezgene(self, entrezgene):
        """Sets the entrezgene of this Enzyme.

        Description not available  # noqa: E501

        :param entrezgene: The entrezgene of this Enzyme.
        :type entrezgene: List[str]
        """

        self._entrezgene = entrezgene

    @property
    def symbol(self):
        """Gets the symbol of this Enzyme.

        HUGO Gene Symbol  # noqa: E501

        :return: The symbol of this Enzyme.
        :rtype: List[str]
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Enzyme.

        HUGO Gene Symbol  # noqa: E501

        :param symbol: The symbol of this Enzyme.
        :type symbol: List[str]
        """

        self._symbol = symbol

    @property
    def description(self):
        """Gets the description of this Enzyme.

        small description  # noqa: E501

        :return: The description of this Enzyme.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Enzyme.

        small description  # noqa: E501

        :param description: The description of this Enzyme.
        :type description: List[str]
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this Enzyme.

        short description of the resource  # noqa: E501

        :return: The label of this Enzyme.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Enzyme.

        short description of the resource  # noqa: E501

        :param label: The label of this Enzyme.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Enzyme.

        type of the resource  # noqa: E501

        :return: The type of this Enzyme.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Enzyme.

        type of the resource  # noqa: E501

        :param type: The type of this Enzyme.
        :type type: List[str]
        """

        self._type = type

    @property
    def ensembl(self):
        """Gets the ensembl of this Enzyme.

        Description not available  # noqa: E501

        :return: The ensembl of this Enzyme.
        :rtype: List[str]
        """
        return self._ensembl

    @ensembl.setter
    def ensembl(self, ensembl):
        """Sets the ensembl of this Enzyme.

        Description not available  # noqa: E501

        :param ensembl: The ensembl of this Enzyme.
        :type ensembl: List[str]
        """

        self._ensembl = ensembl

    @property
    def refseqprotein(self):
        """Gets the refseqprotein of this Enzyme.

        Description not available  # noqa: E501

        :return: The refseqprotein of this Enzyme.
        :rtype: List[str]
        """
        return self._refseqprotein

    @refseqprotein.setter
    def refseqprotein(self, refseqprotein):
        """Sets the refseqprotein of this Enzyme.

        Description not available  # noqa: E501

        :param refseqprotein: The refseqprotein of this Enzyme.
        :type refseqprotein: List[str]
        """

        self._refseqprotein = refseqprotein

    @property
    def omim(self):
        """Gets the omim of this Enzyme.

        Description not available  # noqa: E501

        :return: The omim of this Enzyme.
        :rtype: List[int]
        """
        return self._omim

    @omim.setter
    def omim(self, omim):
        """Sets the omim of this Enzyme.

        Description not available  # noqa: E501

        :param omim: The omim of this Enzyme.
        :type omim: List[int]
        """

        self._omim = omim

    @property
    def refseqmrna(self):
        """Gets the refseqmrna of this Enzyme.

        Description not available  # noqa: E501

        :return: The refseqmrna of this Enzyme.
        :rtype: List[str]
        """
        return self._refseqmrna

    @refseqmrna.setter
    def refseqmrna(self, refseqmrna):
        """Sets the refseqmrna of this Enzyme.

        Description not available  # noqa: E501

        :param refseqmrna: The refseqmrna of this Enzyme.
        :type refseqmrna: List[str]
        """

        self._refseqmrna = refseqmrna

    @property
    def hgncid(self):
        """Gets the hgncid of this Enzyme.

        Description not available  # noqa: E501

        :return: The hgncid of this Enzyme.
        :rtype: List[str]
        """
        return self._hgncid

    @hgncid.setter
    def hgncid(self, hgncid):
        """Sets the hgncid of this Enzyme.

        Description not available  # noqa: E501

        :param hgncid: The hgncid of this Enzyme.
        :type hgncid: List[str]
        """

        self._hgncid = hgncid

    @property
    def mgiid(self):
        """Gets the mgiid of this Enzyme.

        Mouse Genomic Informatics ID  # noqa: E501

        :return: The mgiid of this Enzyme.
        :rtype: List[str]
        """
        return self._mgiid

    @mgiid.setter
    def mgiid(self, mgiid):
        """Sets the mgiid of this Enzyme.

        Mouse Genomic Informatics ID  # noqa: E501

        :param mgiid: The mgiid of this Enzyme.
        :type mgiid: List[str]
        """

        self._mgiid = mgiid

    @property
    def ec_number(self):
        """Gets the ec_number of this Enzyme.

        Description not available  # noqa: E501

        :return: The ec_number of this Enzyme.
        :rtype: List[str]
        """
        return self._ec_number

    @ec_number.setter
    def ec_number(self, ec_number):
        """Sets the ec_number of this Enzyme.

        Description not available  # noqa: E501

        :param ec_number: The ec_number of this Enzyme.
        :type ec_number: List[str]
        """

        self._ec_number = ec_number

    @property
    def id(self):
        """Gets the id of this Enzyme.

        identifier  # noqa: E501

        :return: The id of this Enzyme.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Enzyme.

        identifier  # noqa: E501

        :param id: The id of this Enzyme.
        :type id: str
        """

        self._id = id

    @property
    def uniprot(self):
        """Gets the uniprot of this Enzyme.

        Description not available  # noqa: E501

        :return: The uniprot of this Enzyme.
        :rtype: List[str]
        """
        return self._uniprot

    @uniprot.setter
    def uniprot(self, uniprot):
        """Sets the uniprot of this Enzyme.

        Description not available  # noqa: E501

        :param uniprot: The uniprot of this Enzyme.
        :type uniprot: List[str]
        """

        self._uniprot = uniprot
