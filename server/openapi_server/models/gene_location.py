# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class GeneLocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, gene_location_end=None, gene_location_start=None, genome_db=None, description=None, on_chromosome=None, id=None, label=None, type=None):  # noqa: E501
        """GeneLocation - a model defined in OpenAPI

        :param gene_location_end: The gene_location_end of this GeneLocation.  # noqa: E501
        :type gene_location_end: List[int]
        :param gene_location_start: The gene_location_start of this GeneLocation.  # noqa: E501
        :type gene_location_start: List[int]
        :param genome_db: The genome_db of this GeneLocation.  # noqa: E501
        :type genome_db: List[str]
        :param description: The description of this GeneLocation.  # noqa: E501
        :type description: List[str]
        :param on_chromosome: The on_chromosome of this GeneLocation.  # noqa: E501
        :type on_chromosome: List[int]
        :param id: The id of this GeneLocation.  # noqa: E501
        :type id: str
        :param label: The label of this GeneLocation.  # noqa: E501
        :type label: List[str]
        :param type: The type of this GeneLocation.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'gene_location_end': List[int],
            'gene_location_start': List[int],
            'genome_db': List[str],
            'description': List[str],
            'on_chromosome': List[int],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'gene_location_end': 'geneLocationEnd',
            'gene_location_start': 'geneLocationStart',
            'genome_db': 'genomeDB',
            'description': 'description',
            'on_chromosome': 'onChromosome',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._gene_location_end = gene_location_end
        self._gene_location_start = gene_location_start
        self._genome_db = genome_db
        self._description = description
        self._on_chromosome = on_chromosome
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'GeneLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GeneLocation of this GeneLocation.  # noqa: E501
        :rtype: GeneLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gene_location_end(self):
        """Gets the gene_location_end of this GeneLocation.

        the end of the gene  # noqa: E501

        :return: The gene_location_end of this GeneLocation.
        :rtype: List[int]
        """
        return self._gene_location_end

    @gene_location_end.setter
    def gene_location_end(self, gene_location_end):
        """Sets the gene_location_end of this GeneLocation.

        the end of the gene  # noqa: E501

        :param gene_location_end: The gene_location_end of this GeneLocation.
        :type gene_location_end: List[int]
        """

        self._gene_location_end = gene_location_end

    @property
    def gene_location_start(self):
        """Gets the gene_location_start of this GeneLocation.

        the start of the gene coordinates  # noqa: E501

        :return: The gene_location_start of this GeneLocation.
        :rtype: List[int]
        """
        return self._gene_location_start

    @gene_location_start.setter
    def gene_location_start(self, gene_location_start):
        """Sets the gene_location_start of this GeneLocation.

        the start of the gene coordinates  # noqa: E501

        :param gene_location_start: The gene_location_start of this GeneLocation.
        :type gene_location_start: List[int]
        """

        self._gene_location_start = gene_location_start

    @property
    def genome_db(self):
        """Gets the genome_db of this GeneLocation.

        the edition of the database used (i.e. hg19)  # noqa: E501

        :return: The genome_db of this GeneLocation.
        :rtype: List[str]
        """
        return self._genome_db

    @genome_db.setter
    def genome_db(self, genome_db):
        """Sets the genome_db of this GeneLocation.

        the edition of the database used (i.e. hg19)  # noqa: E501

        :param genome_db: The genome_db of this GeneLocation.
        :type genome_db: List[str]
        """

        self._genome_db = genome_db

    @property
    def description(self):
        """Gets the description of this GeneLocation.

        small description  # noqa: E501

        :return: The description of this GeneLocation.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GeneLocation.

        small description  # noqa: E501

        :param description: The description of this GeneLocation.
        :type description: List[str]
        """

        self._description = description

    @property
    def on_chromosome(self):
        """Gets the on_chromosome of this GeneLocation.

        the number corresponding to the chromosome on which the gene is located  # noqa: E501

        :return: The on_chromosome of this GeneLocation.
        :rtype: List[int]
        """
        return self._on_chromosome

    @on_chromosome.setter
    def on_chromosome(self, on_chromosome):
        """Sets the on_chromosome of this GeneLocation.

        the number corresponding to the chromosome on which the gene is located  # noqa: E501

        :param on_chromosome: The on_chromosome of this GeneLocation.
        :type on_chromosome: List[int]
        """

        self._on_chromosome = on_chromosome

    @property
    def id(self):
        """Gets the id of this GeneLocation.

        identifier  # noqa: E501

        :return: The id of this GeneLocation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeneLocation.

        identifier  # noqa: E501

        :param id: The id of this GeneLocation.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this GeneLocation.

        short description of the resource  # noqa: E501

        :return: The label of this GeneLocation.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GeneLocation.

        short description of the resource  # noqa: E501

        :param label: The label of this GeneLocation.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this GeneLocation.

        type of the resource  # noqa: E501

        :return: The type of this GeneLocation.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GeneLocation.

        type of the resource  # noqa: E501

        :param type: The type of this GeneLocation.
        :type type: List[str]
        """

        self._type = type
