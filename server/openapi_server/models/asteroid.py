# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Asteroid(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, periapsis=None, absolute_magnitude=None, orbital_eccentricity=None, description=None, label=None, type=None, max_absolute_magnitude=None, apoapsis=None, von_klitzing_constant=None, messier_name=None, max_apparent_magnitude=None, id=None, ngc_name=None):  # noqa: E501
        """Asteroid - a model defined in OpenAPI

        :param periapsis: The periapsis of this Asteroid.  # noqa: E501
        :type periapsis: List[float]
        :param absolute_magnitude: The absolute_magnitude of this Asteroid.  # noqa: E501
        :type absolute_magnitude: List[float]
        :param orbital_eccentricity: The orbital_eccentricity of this Asteroid.  # noqa: E501
        :type orbital_eccentricity: List[float]
        :param description: The description of this Asteroid.  # noqa: E501
        :type description: List[str]
        :param label: The label of this Asteroid.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Asteroid.  # noqa: E501
        :type type: List[str]
        :param max_absolute_magnitude: The max_absolute_magnitude of this Asteroid.  # noqa: E501
        :type max_absolute_magnitude: List[float]
        :param apoapsis: The apoapsis of this Asteroid.  # noqa: E501
        :type apoapsis: List[float]
        :param von_klitzing_constant: The von_klitzing_constant of this Asteroid.  # noqa: E501
        :type von_klitzing_constant: List[float]
        :param messier_name: The messier_name of this Asteroid.  # noqa: E501
        :type messier_name: List[str]
        :param max_apparent_magnitude: The max_apparent_magnitude of this Asteroid.  # noqa: E501
        :type max_apparent_magnitude: List[float]
        :param id: The id of this Asteroid.  # noqa: E501
        :type id: str
        :param ngc_name: The ngc_name of this Asteroid.  # noqa: E501
        :type ngc_name: List[str]
        """


        self.openapi_types = {
            'periapsis': List[float],
            'absolute_magnitude': List[float],
            'orbital_eccentricity': List[float],
            'description': List[str],
            'label': List[str],
            'type': List[str],
            'max_absolute_magnitude': List[float],
            'apoapsis': List[float],
            'von_klitzing_constant': List[float],
            'messier_name': List[str],
            'max_apparent_magnitude': List[float],
            'id': str,
            'ngc_name': List[str]
        }

        self.attribute_map = {
            'periapsis': 'periapsis',
            'absolute_magnitude': 'absoluteMagnitude',
            'orbital_eccentricity': 'orbitalEccentricity',
            'description': 'description',
            'label': 'label',
            'type': 'type',
            'max_absolute_magnitude': 'maxAbsoluteMagnitude',
            'apoapsis': 'apoapsis',
            'von_klitzing_constant': 'vonKlitzingConstant',
            'messier_name': 'messierName',
            'max_apparent_magnitude': 'maxApparentMagnitude',
            'id': 'id',
            'ngc_name': 'ngcName'
        }

        self._periapsis = periapsis
        self._absolute_magnitude = absolute_magnitude
        self._orbital_eccentricity = orbital_eccentricity
        self._description = description
        self._label = label
        self._type = type
        self._max_absolute_magnitude = max_absolute_magnitude
        self._apoapsis = apoapsis
        self._von_klitzing_constant = von_klitzing_constant
        self._messier_name = messier_name
        self._max_apparent_magnitude = max_apparent_magnitude
        self._id = id
        self._ngc_name = ngc_name

    @classmethod
    def from_dict(cls, dikt) -> 'Asteroid':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Asteroid of this Asteroid.  # noqa: E501
        :rtype: Asteroid
        """
        return util.deserialize_model(dikt, cls)

    @property
    def periapsis(self):
        """Gets the periapsis of this Asteroid.

        Description not available  # noqa: E501

        :return: The periapsis of this Asteroid.
        :rtype: List[float]
        """
        return self._periapsis

    @periapsis.setter
    def periapsis(self, periapsis):
        """Sets the periapsis of this Asteroid.

        Description not available  # noqa: E501

        :param periapsis: The periapsis of this Asteroid.
        :type periapsis: List[float]
        """

        self._periapsis = periapsis

    @property
    def absolute_magnitude(self):
        """Gets the absolute_magnitude of this Asteroid.

        Description not available  # noqa: E501

        :return: The absolute_magnitude of this Asteroid.
        :rtype: List[float]
        """
        return self._absolute_magnitude

    @absolute_magnitude.setter
    def absolute_magnitude(self, absolute_magnitude):
        """Sets the absolute_magnitude of this Asteroid.

        Description not available  # noqa: E501

        :param absolute_magnitude: The absolute_magnitude of this Asteroid.
        :type absolute_magnitude: List[float]
        """

        self._absolute_magnitude = absolute_magnitude

    @property
    def orbital_eccentricity(self):
        """Gets the orbital_eccentricity of this Asteroid.

        Description not available  # noqa: E501

        :return: The orbital_eccentricity of this Asteroid.
        :rtype: List[float]
        """
        return self._orbital_eccentricity

    @orbital_eccentricity.setter
    def orbital_eccentricity(self, orbital_eccentricity):
        """Sets the orbital_eccentricity of this Asteroid.

        Description not available  # noqa: E501

        :param orbital_eccentricity: The orbital_eccentricity of this Asteroid.
        :type orbital_eccentricity: List[float]
        """

        self._orbital_eccentricity = orbital_eccentricity

    @property
    def description(self):
        """Gets the description of this Asteroid.

        small description  # noqa: E501

        :return: The description of this Asteroid.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Asteroid.

        small description  # noqa: E501

        :param description: The description of this Asteroid.
        :type description: List[str]
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this Asteroid.

        short description of the resource  # noqa: E501

        :return: The label of this Asteroid.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Asteroid.

        short description of the resource  # noqa: E501

        :param label: The label of this Asteroid.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Asteroid.

        type of the resource  # noqa: E501

        :return: The type of this Asteroid.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Asteroid.

        type of the resource  # noqa: E501

        :param type: The type of this Asteroid.
        :type type: List[str]
        """

        self._type = type

    @property
    def max_absolute_magnitude(self):
        """Gets the max_absolute_magnitude of this Asteroid.

        Description not available  # noqa: E501

        :return: The max_absolute_magnitude of this Asteroid.
        :rtype: List[float]
        """
        return self._max_absolute_magnitude

    @max_absolute_magnitude.setter
    def max_absolute_magnitude(self, max_absolute_magnitude):
        """Sets the max_absolute_magnitude of this Asteroid.

        Description not available  # noqa: E501

        :param max_absolute_magnitude: The max_absolute_magnitude of this Asteroid.
        :type max_absolute_magnitude: List[float]
        """

        self._max_absolute_magnitude = max_absolute_magnitude

    @property
    def apoapsis(self):
        """Gets the apoapsis of this Asteroid.

        Description not available  # noqa: E501

        :return: The apoapsis of this Asteroid.
        :rtype: List[float]
        """
        return self._apoapsis

    @apoapsis.setter
    def apoapsis(self, apoapsis):
        """Sets the apoapsis of this Asteroid.

        Description not available  # noqa: E501

        :param apoapsis: The apoapsis of this Asteroid.
        :type apoapsis: List[float]
        """

        self._apoapsis = apoapsis

    @property
    def von_klitzing_constant(self):
        """Gets the von_klitzing_constant of this Asteroid.

        Description not available  # noqa: E501

        :return: The von_klitzing_constant of this Asteroid.
        :rtype: List[float]
        """
        return self._von_klitzing_constant

    @von_klitzing_constant.setter
    def von_klitzing_constant(self, von_klitzing_constant):
        """Sets the von_klitzing_constant of this Asteroid.

        Description not available  # noqa: E501

        :param von_klitzing_constant: The von_klitzing_constant of this Asteroid.
        :type von_klitzing_constant: List[float]
        """

        self._von_klitzing_constant = von_klitzing_constant

    @property
    def messier_name(self):
        """Gets the messier_name of this Asteroid.

        Name for Messier objects  # noqa: E501

        :return: The messier_name of this Asteroid.
        :rtype: List[str]
        """
        return self._messier_name

    @messier_name.setter
    def messier_name(self, messier_name):
        """Sets the messier_name of this Asteroid.

        Name for Messier objects  # noqa: E501

        :param messier_name: The messier_name of this Asteroid.
        :type messier_name: List[str]
        """

        self._messier_name = messier_name

    @property
    def max_apparent_magnitude(self):
        """Gets the max_apparent_magnitude of this Asteroid.

        Description not available  # noqa: E501

        :return: The max_apparent_magnitude of this Asteroid.
        :rtype: List[float]
        """
        return self._max_apparent_magnitude

    @max_apparent_magnitude.setter
    def max_apparent_magnitude(self, max_apparent_magnitude):
        """Sets the max_apparent_magnitude of this Asteroid.

        Description not available  # noqa: E501

        :param max_apparent_magnitude: The max_apparent_magnitude of this Asteroid.
        :type max_apparent_magnitude: List[float]
        """

        self._max_apparent_magnitude = max_apparent_magnitude

    @property
    def id(self):
        """Gets the id of this Asteroid.

        identifier  # noqa: E501

        :return: The id of this Asteroid.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Asteroid.

        identifier  # noqa: E501

        :param id: The id of this Asteroid.
        :type id: str
        """

        self._id = id

    @property
    def ngc_name(self):
        """Gets the ngc_name of this Asteroid.

        Name for NGC objects  # noqa: E501

        :return: The ngc_name of this Asteroid.
        :rtype: List[str]
        """
        return self._ngc_name

    @ngc_name.setter
    def ngc_name(self, ngc_name):
        """Sets the ngc_name of this Asteroid.

        Name for NGC objects  # noqa: E501

        :param ngc_name: The ngc_name of this Asteroid.
        :type ngc_name: List[str]
        """

        self._ngc_name = ngc_name
