# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Bird(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, classis=None, sub_family=None, scientific_name=None, breeder=None, description=None, binomial_authority=None, type=None, sub_tribus=None, dam=None, sub_classis=None, taxon=None, id=None, tribus=None, order=None, foal_date=None, conservation_status=None, grandsire=None, super_family=None, binomial=None, label=None, conservation_status_system=None, kingdom=None, damsire=None, phylum=None, species=None, genus=None, domain=None, super_tribus=None, sire=None, family=None):  # noqa: E501
        """Bird - a model defined in OpenAPI

        :param classis: The classis of this Bird.  # noqa: E501
        :type classis: List[object]
        :param sub_family: The sub_family of this Bird.  # noqa: E501
        :type sub_family: List[object]
        :param scientific_name: The scientific_name of this Bird.  # noqa: E501
        :type scientific_name: List[str]
        :param breeder: The breeder of this Bird.  # noqa: E501
        :type breeder: List[object]
        :param description: The description of this Bird.  # noqa: E501
        :type description: List[str]
        :param binomial_authority: The binomial_authority of this Bird.  # noqa: E501
        :type binomial_authority: List[object]
        :param type: The type of this Bird.  # noqa: E501
        :type type: List[str]
        :param sub_tribus: The sub_tribus of this Bird.  # noqa: E501
        :type sub_tribus: List[object]
        :param dam: The dam of this Bird.  # noqa: E501
        :type dam: List[object]
        :param sub_classis: The sub_classis of this Bird.  # noqa: E501
        :type sub_classis: List[object]
        :param taxon: The taxon of this Bird.  # noqa: E501
        :type taxon: List[object]
        :param id: The id of this Bird.  # noqa: E501
        :type id: str
        :param tribus: The tribus of this Bird.  # noqa: E501
        :type tribus: List[object]
        :param order: The order of this Bird.  # noqa: E501
        :type order: List[object]
        :param foal_date: The foal_date of this Bird.  # noqa: E501
        :type foal_date: List[str]
        :param conservation_status: The conservation_status of this Bird.  # noqa: E501
        :type conservation_status: List[str]
        :param grandsire: The grandsire of this Bird.  # noqa: E501
        :type grandsire: List[object]
        :param super_family: The super_family of this Bird.  # noqa: E501
        :type super_family: List[object]
        :param binomial: The binomial of this Bird.  # noqa: E501
        :type binomial: List[object]
        :param label: The label of this Bird.  # noqa: E501
        :type label: List[str]
        :param conservation_status_system: The conservation_status_system of this Bird.  # noqa: E501
        :type conservation_status_system: List[str]
        :param kingdom: The kingdom of this Bird.  # noqa: E501
        :type kingdom: List[object]
        :param damsire: The damsire of this Bird.  # noqa: E501
        :type damsire: List[object]
        :param phylum: The phylum of this Bird.  # noqa: E501
        :type phylum: List[object]
        :param species: The species of this Bird.  # noqa: E501
        :type species: List[object]
        :param genus: The genus of this Bird.  # noqa: E501
        :type genus: List[object]
        :param domain: The domain of this Bird.  # noqa: E501
        :type domain: List[object]
        :param super_tribus: The super_tribus of this Bird.  # noqa: E501
        :type super_tribus: List[object]
        :param sire: The sire of this Bird.  # noqa: E501
        :type sire: List[object]
        :param family: The family of this Bird.  # noqa: E501
        :type family: List[object]
        """


        self.openapi_types = {
            'classis': List[object],
            'sub_family': List[object],
            'scientific_name': List[str],
            'breeder': List[object],
            'description': List[str],
            'binomial_authority': List[object],
            'type': List[str],
            'sub_tribus': List[object],
            'dam': List[object],
            'sub_classis': List[object],
            'taxon': List[object],
            'id': str,
            'tribus': List[object],
            'order': List[object],
            'foal_date': List[str],
            'conservation_status': List[str],
            'grandsire': List[object],
            'super_family': List[object],
            'binomial': List[object],
            'label': List[str],
            'conservation_status_system': List[str],
            'kingdom': List[object],
            'damsire': List[object],
            'phylum': List[object],
            'species': List[object],
            'genus': List[object],
            'domain': List[object],
            'super_tribus': List[object],
            'sire': List[object],
            'family': List[object]
        }

        self.attribute_map = {
            'classis': 'classis',
            'sub_family': 'subFamily',
            'scientific_name': 'scientificName',
            'breeder': 'breeder',
            'description': 'description',
            'binomial_authority': 'binomialAuthority',
            'type': 'type',
            'sub_tribus': 'subTribus',
            'dam': 'dam',
            'sub_classis': 'subClassis',
            'taxon': 'taxon',
            'id': 'id',
            'tribus': 'tribus',
            'order': 'order',
            'foal_date': 'foalDate',
            'conservation_status': 'conservationStatus',
            'grandsire': 'grandsire',
            'super_family': 'superFamily',
            'binomial': 'binomial',
            'label': 'label',
            'conservation_status_system': 'conservationStatusSystem',
            'kingdom': 'kingdom',
            'damsire': 'damsire',
            'phylum': 'phylum',
            'species': 'species',
            'genus': 'genus',
            'domain': 'domain',
            'super_tribus': 'superTribus',
            'sire': 'sire',
            'family': 'family'
        }

        self._classis = classis
        self._sub_family = sub_family
        self._scientific_name = scientific_name
        self._breeder = breeder
        self._description = description
        self._binomial_authority = binomial_authority
        self._type = type
        self._sub_tribus = sub_tribus
        self._dam = dam
        self._sub_classis = sub_classis
        self._taxon = taxon
        self._id = id
        self._tribus = tribus
        self._order = order
        self._foal_date = foal_date
        self._conservation_status = conservation_status
        self._grandsire = grandsire
        self._super_family = super_family
        self._binomial = binomial
        self._label = label
        self._conservation_status_system = conservation_status_system
        self._kingdom = kingdom
        self._damsire = damsire
        self._phylum = phylum
        self._species = species
        self._genus = genus
        self._domain = domain
        self._super_tribus = super_tribus
        self._sire = sire
        self._family = family

    @classmethod
    def from_dict(cls, dikt) -> 'Bird':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Bird of this Bird.  # noqa: E501
        :rtype: Bird
        """
        return util.deserialize_model(dikt, cls)

    @property
    def classis(self):
        """Gets the classis of this Bird.

        the living thing class (from the Latin \"classis\"), according to the biological taxonomy  # noqa: E501

        :return: The classis of this Bird.
        :rtype: List[object]
        """
        return self._classis

    @classis.setter
    def classis(self, classis):
        """Sets the classis of this Bird.

        the living thing class (from the Latin \"classis\"), according to the biological taxonomy  # noqa: E501

        :param classis: The classis of this Bird.
        :type classis: List[object]
        """

        self._classis = classis

    @property
    def sub_family(self):
        """Gets the sub_family of this Bird.

        Description not available  # noqa: E501

        :return: The sub_family of this Bird.
        :rtype: List[object]
        """
        return self._sub_family

    @sub_family.setter
    def sub_family(self, sub_family):
        """Sets the sub_family of this Bird.

        Description not available  # noqa: E501

        :param sub_family: The sub_family of this Bird.
        :type sub_family: List[object]
        """

        self._sub_family = sub_family

    @property
    def scientific_name(self):
        """Gets the scientific_name of this Bird.

        Description not available  # noqa: E501

        :return: The scientific_name of this Bird.
        :rtype: List[str]
        """
        return self._scientific_name

    @scientific_name.setter
    def scientific_name(self, scientific_name):
        """Sets the scientific_name of this Bird.

        Description not available  # noqa: E501

        :param scientific_name: The scientific_name of this Bird.
        :type scientific_name: List[str]
        """

        self._scientific_name = scientific_name

    @property
    def breeder(self):
        """Gets the breeder of this Bird.

        Description not available  # noqa: E501

        :return: The breeder of this Bird.
        :rtype: List[object]
        """
        return self._breeder

    @breeder.setter
    def breeder(self, breeder):
        """Sets the breeder of this Bird.

        Description not available  # noqa: E501

        :param breeder: The breeder of this Bird.
        :type breeder: List[object]
        """

        self._breeder = breeder

    @property
    def description(self):
        """Gets the description of this Bird.

        small description  # noqa: E501

        :return: The description of this Bird.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Bird.

        small description  # noqa: E501

        :param description: The description of this Bird.
        :type description: List[str]
        """

        self._description = description

    @property
    def binomial_authority(self):
        """Gets the binomial_authority of this Bird.

        Description not available  # noqa: E501

        :return: The binomial_authority of this Bird.
        :rtype: List[object]
        """
        return self._binomial_authority

    @binomial_authority.setter
    def binomial_authority(self, binomial_authority):
        """Sets the binomial_authority of this Bird.

        Description not available  # noqa: E501

        :param binomial_authority: The binomial_authority of this Bird.
        :type binomial_authority: List[object]
        """

        self._binomial_authority = binomial_authority

    @property
    def type(self):
        """Gets the type of this Bird.

        type of the resource  # noqa: E501

        :return: The type of this Bird.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Bird.

        type of the resource  # noqa: E501

        :param type: The type of this Bird.
        :type type: List[str]
        """

        self._type = type

    @property
    def sub_tribus(self):
        """Gets the sub_tribus of this Bird.

        Description not available  # noqa: E501

        :return: The sub_tribus of this Bird.
        :rtype: List[object]
        """
        return self._sub_tribus

    @sub_tribus.setter
    def sub_tribus(self, sub_tribus):
        """Sets the sub_tribus of this Bird.

        Description not available  # noqa: E501

        :param sub_tribus: The sub_tribus of this Bird.
        :type sub_tribus: List[object]
        """

        self._sub_tribus = sub_tribus

    @property
    def dam(self):
        """Gets the dam of this Bird.

        Description not available  # noqa: E501

        :return: The dam of this Bird.
        :rtype: List[object]
        """
        return self._dam

    @dam.setter
    def dam(self, dam):
        """Sets the dam of this Bird.

        Description not available  # noqa: E501

        :param dam: The dam of this Bird.
        :type dam: List[object]
        """

        self._dam = dam

    @property
    def sub_classis(self):
        """Gets the sub_classis of this Bird.

        a subdivision within a Species classis  # noqa: E501

        :return: The sub_classis of this Bird.
        :rtype: List[object]
        """
        return self._sub_classis

    @sub_classis.setter
    def sub_classis(self, sub_classis):
        """Sets the sub_classis of this Bird.

        a subdivision within a Species classis  # noqa: E501

        :param sub_classis: The sub_classis of this Bird.
        :type sub_classis: List[object]
        """

        self._sub_classis = sub_classis

    @property
    def taxon(self):
        """Gets the taxon of this Bird.

        Description not available  # noqa: E501

        :return: The taxon of this Bird.
        :rtype: List[object]
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this Bird.

        Description not available  # noqa: E501

        :param taxon: The taxon of this Bird.
        :type taxon: List[object]
        """

        self._taxon = taxon

    @property
    def id(self):
        """Gets the id of this Bird.

        identifier  # noqa: E501

        :return: The id of this Bird.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Bird.

        identifier  # noqa: E501

        :param id: The id of this Bird.
        :type id: str
        """

        self._id = id

    @property
    def tribus(self):
        """Gets the tribus of this Bird.

        Description not available  # noqa: E501

        :return: The tribus of this Bird.
        :rtype: List[object]
        """
        return self._tribus

    @tribus.setter
    def tribus(self, tribus):
        """Sets the tribus of this Bird.

        Description not available  # noqa: E501

        :param tribus: The tribus of this Bird.
        :type tribus: List[object]
        """

        self._tribus = tribus

    @property
    def order(self):
        """Gets the order of this Bird.

        Description not available  # noqa: E501

        :return: The order of this Bird.
        :rtype: List[object]
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Bird.

        Description not available  # noqa: E501

        :param order: The order of this Bird.
        :type order: List[object]
        """

        self._order = order

    @property
    def foal_date(self):
        """Gets the foal_date of this Bird.

        Description not available  # noqa: E501

        :return: The foal_date of this Bird.
        :rtype: List[str]
        """
        return self._foal_date

    @foal_date.setter
    def foal_date(self, foal_date):
        """Sets the foal_date of this Bird.

        Description not available  # noqa: E501

        :param foal_date: The foal_date of this Bird.
        :type foal_date: List[str]
        """

        self._foal_date = foal_date

    @property
    def conservation_status(self):
        """Gets the conservation_status of this Bird.

        Description not available  # noqa: E501

        :return: The conservation_status of this Bird.
        :rtype: List[str]
        """
        return self._conservation_status

    @conservation_status.setter
    def conservation_status(self, conservation_status):
        """Sets the conservation_status of this Bird.

        Description not available  # noqa: E501

        :param conservation_status: The conservation_status of this Bird.
        :type conservation_status: List[str]
        """

        self._conservation_status = conservation_status

    @property
    def grandsire(self):
        """Gets the grandsire of this Bird.

        Description not available  # noqa: E501

        :return: The grandsire of this Bird.
        :rtype: List[object]
        """
        return self._grandsire

    @grandsire.setter
    def grandsire(self, grandsire):
        """Sets the grandsire of this Bird.

        Description not available  # noqa: E501

        :param grandsire: The grandsire of this Bird.
        :type grandsire: List[object]
        """

        self._grandsire = grandsire

    @property
    def super_family(self):
        """Gets the super_family of this Bird.

        Description not available  # noqa: E501

        :return: The super_family of this Bird.
        :rtype: List[object]
        """
        return self._super_family

    @super_family.setter
    def super_family(self, super_family):
        """Sets the super_family of this Bird.

        Description not available  # noqa: E501

        :param super_family: The super_family of this Bird.
        :type super_family: List[object]
        """

        self._super_family = super_family

    @property
    def binomial(self):
        """Gets the binomial of this Bird.

        Description not available  # noqa: E501

        :return: The binomial of this Bird.
        :rtype: List[object]
        """
        return self._binomial

    @binomial.setter
    def binomial(self, binomial):
        """Sets the binomial of this Bird.

        Description not available  # noqa: E501

        :param binomial: The binomial of this Bird.
        :type binomial: List[object]
        """

        self._binomial = binomial

    @property
    def label(self):
        """Gets the label of this Bird.

        short description of the resource  # noqa: E501

        :return: The label of this Bird.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Bird.

        short description of the resource  # noqa: E501

        :param label: The label of this Bird.
        :type label: List[str]
        """

        self._label = label

    @property
    def conservation_status_system(self):
        """Gets the conservation_status_system of this Bird.

        Description not available  # noqa: E501

        :return: The conservation_status_system of this Bird.
        :rtype: List[str]
        """
        return self._conservation_status_system

    @conservation_status_system.setter
    def conservation_status_system(self, conservation_status_system):
        """Sets the conservation_status_system of this Bird.

        Description not available  # noqa: E501

        :param conservation_status_system: The conservation_status_system of this Bird.
        :type conservation_status_system: List[str]
        """

        self._conservation_status_system = conservation_status_system

    @property
    def kingdom(self):
        """Gets the kingdom of this Bird.

        In biology, kingdom (Latin: regnum, pl. regna) is a taxonomic rank, which is either the highest rank or in the more recent three-domain system, the rank below domain.  # noqa: E501

        :return: The kingdom of this Bird.
        :rtype: List[object]
        """
        return self._kingdom

    @kingdom.setter
    def kingdom(self, kingdom):
        """Sets the kingdom of this Bird.

        In biology, kingdom (Latin: regnum, pl. regna) is a taxonomic rank, which is either the highest rank or in the more recent three-domain system, the rank below domain.  # noqa: E501

        :param kingdom: The kingdom of this Bird.
        :type kingdom: List[object]
        """

        self._kingdom = kingdom

    @property
    def damsire(self):
        """Gets the damsire of this Bird.

        Description not available  # noqa: E501

        :return: The damsire of this Bird.
        :rtype: List[object]
        """
        return self._damsire

    @damsire.setter
    def damsire(self, damsire):
        """Sets the damsire of this Bird.

        Description not available  # noqa: E501

        :param damsire: The damsire of this Bird.
        :type damsire: List[object]
        """

        self._damsire = damsire

    @property
    def phylum(self):
        """Gets the phylum of this Bird.

        A rank in the classification of organisms, below kingdom and above class; also called a division, especially in describing plants; a taxon at that rank.  # noqa: E501

        :return: The phylum of this Bird.
        :rtype: List[object]
        """
        return self._phylum

    @phylum.setter
    def phylum(self, phylum):
        """Sets the phylum of this Bird.

        A rank in the classification of organisms, below kingdom and above class; also called a division, especially in describing plants; a taxon at that rank.  # noqa: E501

        :param phylum: The phylum of this Bird.
        :type phylum: List[object]
        """

        self._phylum = phylum

    @property
    def species(self):
        """Gets the species of this Bird.

        Description not available  # noqa: E501

        :return: The species of this Bird.
        :rtype: List[object]
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this Bird.

        Description not available  # noqa: E501

        :param species: The species of this Bird.
        :type species: List[object]
        """

        self._species = species

    @property
    def genus(self):
        """Gets the genus of this Bird.

        A rank in the classification of organisms, below family and above species; a taxon at that rank  # noqa: E501

        :return: The genus of this Bird.
        :rtype: List[object]
        """
        return self._genus

    @genus.setter
    def genus(self, genus):
        """Sets the genus of this Bird.

        A rank in the classification of organisms, below family and above species; a taxon at that rank  # noqa: E501

        :param genus: The genus of this Bird.
        :type genus: List[object]
        """

        self._genus = genus

    @property
    def domain(self):
        """Gets the domain of this Bird.

        Description not available  # noqa: E501

        :return: The domain of this Bird.
        :rtype: List[object]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Bird.

        Description not available  # noqa: E501

        :param domain: The domain of this Bird.
        :type domain: List[object]
        """

        self._domain = domain

    @property
    def super_tribus(self):
        """Gets the super_tribus of this Bird.

        Description not available  # noqa: E501

        :return: The super_tribus of this Bird.
        :rtype: List[object]
        """
        return self._super_tribus

    @super_tribus.setter
    def super_tribus(self, super_tribus):
        """Sets the super_tribus of this Bird.

        Description not available  # noqa: E501

        :param super_tribus: The super_tribus of this Bird.
        :type super_tribus: List[object]
        """

        self._super_tribus = super_tribus

    @property
    def sire(self):
        """Gets the sire of this Bird.

        Description not available  # noqa: E501

        :return: The sire of this Bird.
        :rtype: List[object]
        """
        return self._sire

    @sire.setter
    def sire(self, sire):
        """Sets the sire of this Bird.

        Description not available  # noqa: E501

        :param sire: The sire of this Bird.
        :type sire: List[object]
        """

        self._sire = sire

    @property
    def family(self):
        """Gets the family of this Bird.

        Description not available  # noqa: E501

        :return: The family of this Bird.
        :rtype: List[object]
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this Bird.

        Description not available  # noqa: E501

        :param family: The family of this Bird.
        :type family: List[object]
        """

        self._family = family
