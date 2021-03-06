# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Rocket(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mass=None, description=None, engine_type=None, rocket_stages=None, type=None, introduction_date=None, rocket_function=None, lower_earth_orbit_payload=None, diameter=None, design_company=None, discharge=None, assembly=None, id=None, rebuilder=None, _class=None, model_start_date=None, height=None, model_end_date=None, number_of_launches=None, model_end_year=None, maiden_flight=None, length=None, final_flight=None, weight=None, label=None, version=None, number_of_seats=None, model_start_year=None, width=None, discharge_average=None, number_of_crew=None, unknown_outcomes=None, country_origin=None, related_mean_of_transportation=None, comparable=None, power_type=None):  # noqa: E501
        """Rocket - a model defined in OpenAPI

        :param mass: The mass of this Rocket.  # noqa: E501
        :type mass: List[object]
        :param description: The description of this Rocket.  # noqa: E501
        :type description: List[str]
        :param engine_type: The engine_type of this Rocket.  # noqa: E501
        :type engine_type: List[object]
        :param rocket_stages: The rocket_stages of this Rocket.  # noqa: E501
        :type rocket_stages: List[int]
        :param type: The type of this Rocket.  # noqa: E501
        :type type: List[str]
        :param introduction_date: The introduction_date of this Rocket.  # noqa: E501
        :type introduction_date: List[str]
        :param rocket_function: The rocket_function of this Rocket.  # noqa: E501
        :type rocket_function: List[object]
        :param lower_earth_orbit_payload: The lower_earth_orbit_payload of this Rocket.  # noqa: E501
        :type lower_earth_orbit_payload: List[object]
        :param diameter: The diameter of this Rocket.  # noqa: E501
        :type diameter: List[object]
        :param design_company: The design_company of this Rocket.  # noqa: E501
        :type design_company: List[object]
        :param discharge: The discharge of this Rocket.  # noqa: E501
        :type discharge: List[float]
        :param assembly: The assembly of this Rocket.  # noqa: E501
        :type assembly: List[object]
        :param id: The id of this Rocket.  # noqa: E501
        :type id: str
        :param rebuilder: The rebuilder of this Rocket.  # noqa: E501
        :type rebuilder: List[object]
        :param _class: The _class of this Rocket.  # noqa: E501
        :type _class: List[object]
        :param model_start_date: The model_start_date of this Rocket.  # noqa: E501
        :type model_start_date: List[str]
        :param height: The height of this Rocket.  # noqa: E501
        :type height: List[object]
        :param model_end_date: The model_end_date of this Rocket.  # noqa: E501
        :type model_end_date: List[str]
        :param number_of_launches: The number_of_launches of this Rocket.  # noqa: E501
        :type number_of_launches: List[int]
        :param model_end_year: The model_end_year of this Rocket.  # noqa: E501
        :type model_end_year: List[str]
        :param maiden_flight: The maiden_flight of this Rocket.  # noqa: E501
        :type maiden_flight: List[str]
        :param length: The length of this Rocket.  # noqa: E501
        :type length: List[object]
        :param final_flight: The final_flight of this Rocket.  # noqa: E501
        :type final_flight: List[str]
        :param weight: The weight of this Rocket.  # noqa: E501
        :type weight: List[object]
        :param label: The label of this Rocket.  # noqa: E501
        :type label: List[str]
        :param version: The version of this Rocket.  # noqa: E501
        :type version: List[object]
        :param number_of_seats: The number_of_seats of this Rocket.  # noqa: E501
        :type number_of_seats: List[int]
        :param model_start_year: The model_start_year of this Rocket.  # noqa: E501
        :type model_start_year: List[str]
        :param width: The width of this Rocket.  # noqa: E501
        :type width: List[object]
        :param discharge_average: The discharge_average of this Rocket.  # noqa: E501
        :type discharge_average: List[float]
        :param number_of_crew: The number_of_crew of this Rocket.  # noqa: E501
        :type number_of_crew: List[int]
        :param unknown_outcomes: The unknown_outcomes of this Rocket.  # noqa: E501
        :type unknown_outcomes: List[int]
        :param country_origin: The country_origin of this Rocket.  # noqa: E501
        :type country_origin: List[object]
        :param related_mean_of_transportation: The related_mean_of_transportation of this Rocket.  # noqa: E501
        :type related_mean_of_transportation: List[object]
        :param comparable: The comparable of this Rocket.  # noqa: E501
        :type comparable: List[object]
        :param power_type: The power_type of this Rocket.  # noqa: E501
        :type power_type: List[object]
        """


        self.openapi_types = {
            'mass': List[object],
            'description': List[str],
            'engine_type': List[object],
            'rocket_stages': List[int],
            'type': List[str],
            'introduction_date': List[str],
            'rocket_function': List[object],
            'lower_earth_orbit_payload': List[object],
            'diameter': List[object],
            'design_company': List[object],
            'discharge': List[float],
            'assembly': List[object],
            'id': str,
            'rebuilder': List[object],
            '_class': List[object],
            'model_start_date': List[str],
            'height': List[object],
            'model_end_date': List[str],
            'number_of_launches': List[int],
            'model_end_year': List[str],
            'maiden_flight': List[str],
            'length': List[object],
            'final_flight': List[str],
            'weight': List[object],
            'label': List[str],
            'version': List[object],
            'number_of_seats': List[int],
            'model_start_year': List[str],
            'width': List[object],
            'discharge_average': List[float],
            'number_of_crew': List[int],
            'unknown_outcomes': List[int],
            'country_origin': List[object],
            'related_mean_of_transportation': List[object],
            'comparable': List[object],
            'power_type': List[object]
        }

        self.attribute_map = {
            'mass': 'mass',
            'description': 'description',
            'engine_type': 'engineType',
            'rocket_stages': 'rocketStages',
            'type': 'type',
            'introduction_date': 'introductionDate',
            'rocket_function': 'rocketFunction',
            'lower_earth_orbit_payload': 'lowerEarthOrbitPayload',
            'diameter': 'diameter',
            'design_company': 'designCompany',
            'discharge': 'discharge',
            'assembly': 'assembly',
            'id': 'id',
            'rebuilder': 'rebuilder',
            '_class': 'class',
            'model_start_date': 'modelStartDate',
            'height': 'height',
            'model_end_date': 'modelEndDate',
            'number_of_launches': 'numberOfLaunches',
            'model_end_year': 'modelEndYear',
            'maiden_flight': 'maidenFlight',
            'length': 'length',
            'final_flight': 'finalFlight',
            'weight': 'weight',
            'label': 'label',
            'version': 'version',
            'number_of_seats': 'numberOfSeats',
            'model_start_year': 'modelStartYear',
            'width': 'width',
            'discharge_average': 'dischargeAverage',
            'number_of_crew': 'numberOfCrew',
            'unknown_outcomes': 'unknownOutcomes',
            'country_origin': 'countryOrigin',
            'related_mean_of_transportation': 'relatedMeanOfTransportation',
            'comparable': 'comparable',
            'power_type': 'powerType'
        }

        self._mass = mass
        self._description = description
        self._engine_type = engine_type
        self._rocket_stages = rocket_stages
        self._type = type
        self._introduction_date = introduction_date
        self._rocket_function = rocket_function
        self._lower_earth_orbit_payload = lower_earth_orbit_payload
        self._diameter = diameter
        self._design_company = design_company
        self._discharge = discharge
        self._assembly = assembly
        self._id = id
        self._rebuilder = rebuilder
        self.__class = _class
        self._model_start_date = model_start_date
        self._height = height
        self._model_end_date = model_end_date
        self._number_of_launches = number_of_launches
        self._model_end_year = model_end_year
        self._maiden_flight = maiden_flight
        self._length = length
        self._final_flight = final_flight
        self._weight = weight
        self._label = label
        self._version = version
        self._number_of_seats = number_of_seats
        self._model_start_year = model_start_year
        self._width = width
        self._discharge_average = discharge_average
        self._number_of_crew = number_of_crew
        self._unknown_outcomes = unknown_outcomes
        self._country_origin = country_origin
        self._related_mean_of_transportation = related_mean_of_transportation
        self._comparable = comparable
        self._power_type = power_type

    @classmethod
    def from_dict(cls, dikt) -> 'Rocket':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Rocket of this Rocket.  # noqa: E501
        :rtype: Rocket
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mass(self):
        """Gets the mass of this Rocket.

        Description not available  # noqa: E501

        :return: The mass of this Rocket.
        :rtype: List[object]
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """Sets the mass of this Rocket.

        Description not available  # noqa: E501

        :param mass: The mass of this Rocket.
        :type mass: List[object]
        """

        self._mass = mass

    @property
    def description(self):
        """Gets the description of this Rocket.

        small description  # noqa: E501

        :return: The description of this Rocket.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rocket.

        small description  # noqa: E501

        :param description: The description of this Rocket.
        :type description: List[str]
        """

        self._description = description

    @property
    def engine_type(self):
        """Gets the engine_type of this Rocket.

        Description not available  # noqa: E501

        :return: The engine_type of this Rocket.
        :rtype: List[object]
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this Rocket.

        Description not available  # noqa: E501

        :param engine_type: The engine_type of this Rocket.
        :type engine_type: List[object]
        """

        self._engine_type = engine_type

    @property
    def rocket_stages(self):
        """Gets the rocket_stages of this Rocket.

        number of stages, not including boosters  # noqa: E501

        :return: The rocket_stages of this Rocket.
        :rtype: List[int]
        """
        return self._rocket_stages

    @rocket_stages.setter
    def rocket_stages(self, rocket_stages):
        """Sets the rocket_stages of this Rocket.

        number of stages, not including boosters  # noqa: E501

        :param rocket_stages: The rocket_stages of this Rocket.
        :type rocket_stages: List[int]
        """

        self._rocket_stages = rocket_stages

    @property
    def type(self):
        """Gets the type of this Rocket.

        type of the resource  # noqa: E501

        :return: The type of this Rocket.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Rocket.

        type of the resource  # noqa: E501

        :param type: The type of this Rocket.
        :type type: List[str]
        """

        self._type = type

    @property
    def introduction_date(self):
        """Gets the introduction_date of this Rocket.

        Description not available  # noqa: E501

        :return: The introduction_date of this Rocket.
        :rtype: List[str]
        """
        return self._introduction_date

    @introduction_date.setter
    def introduction_date(self, introduction_date):
        """Sets the introduction_date of this Rocket.

        Description not available  # noqa: E501

        :param introduction_date: The introduction_date of this Rocket.
        :type introduction_date: List[str]
        """

        self._introduction_date = introduction_date

    @property
    def rocket_function(self):
        """Gets the rocket_function of this Rocket.

        purpose of the rocket  # noqa: E501

        :return: The rocket_function of this Rocket.
        :rtype: List[object]
        """
        return self._rocket_function

    @rocket_function.setter
    def rocket_function(self, rocket_function):
        """Sets the rocket_function of this Rocket.

        purpose of the rocket  # noqa: E501

        :param rocket_function: The rocket_function of this Rocket.
        :type rocket_function: List[object]
        """

        self._rocket_function = rocket_function

    @property
    def lower_earth_orbit_payload(self):
        """Gets the lower_earth_orbit_payload of this Rocket.

        Payload mass in a typical Low Earth orbit  # noqa: E501

        :return: The lower_earth_orbit_payload of this Rocket.
        :rtype: List[object]
        """
        return self._lower_earth_orbit_payload

    @lower_earth_orbit_payload.setter
    def lower_earth_orbit_payload(self, lower_earth_orbit_payload):
        """Sets the lower_earth_orbit_payload of this Rocket.

        Payload mass in a typical Low Earth orbit  # noqa: E501

        :param lower_earth_orbit_payload: The lower_earth_orbit_payload of this Rocket.
        :type lower_earth_orbit_payload: List[object]
        """

        self._lower_earth_orbit_payload = lower_earth_orbit_payload

    @property
    def diameter(self):
        """Gets the diameter of this Rocket.

        Description not available  # noqa: E501

        :return: The diameter of this Rocket.
        :rtype: List[object]
        """
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        """Sets the diameter of this Rocket.

        Description not available  # noqa: E501

        :param diameter: The diameter of this Rocket.
        :type diameter: List[object]
        """

        self._diameter = diameter

    @property
    def design_company(self):
        """Gets the design_company of this Rocket.

        Description not available  # noqa: E501

        :return: The design_company of this Rocket.
        :rtype: List[object]
        """
        return self._design_company

    @design_company.setter
    def design_company(self, design_company):
        """Sets the design_company of this Rocket.

        Description not available  # noqa: E501

        :param design_company: The design_company of this Rocket.
        :type design_company: List[object]
        """

        self._design_company = design_company

    @property
    def discharge(self):
        """Gets the discharge of this Rocket.

        Description not available  # noqa: E501

        :return: The discharge of this Rocket.
        :rtype: List[float]
        """
        return self._discharge

    @discharge.setter
    def discharge(self, discharge):
        """Sets the discharge of this Rocket.

        Description not available  # noqa: E501

        :param discharge: The discharge of this Rocket.
        :type discharge: List[float]
        """

        self._discharge = discharge

    @property
    def assembly(self):
        """Gets the assembly of this Rocket.

        Description not available  # noqa: E501

        :return: The assembly of this Rocket.
        :rtype: List[object]
        """
        return self._assembly

    @assembly.setter
    def assembly(self, assembly):
        """Sets the assembly of this Rocket.

        Description not available  # noqa: E501

        :param assembly: The assembly of this Rocket.
        :type assembly: List[object]
        """

        self._assembly = assembly

    @property
    def id(self):
        """Gets the id of this Rocket.

        identifier  # noqa: E501

        :return: The id of this Rocket.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rocket.

        identifier  # noqa: E501

        :param id: The id of this Rocket.
        :type id: str
        """

        self._id = id

    @property
    def rebuilder(self):
        """Gets the rebuilder of this Rocket.

        Description not available  # noqa: E501

        :return: The rebuilder of this Rocket.
        :rtype: List[object]
        """
        return self._rebuilder

    @rebuilder.setter
    def rebuilder(self, rebuilder):
        """Sets the rebuilder of this Rocket.

        Description not available  # noqa: E501

        :param rebuilder: The rebuilder of this Rocket.
        :type rebuilder: List[object]
        """

        self._rebuilder = rebuilder

    @property
    def _class(self):
        """Gets the _class of this Rocket.

        Description not available  # noqa: E501

        :return: The _class of this Rocket.
        :rtype: List[object]
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Rocket.

        Description not available  # noqa: E501

        :param _class: The _class of this Rocket.
        :type _class: List[object]
        """

        self.__class = _class

    @property
    def model_start_date(self):
        """Gets the model_start_date of this Rocket.

        Description not available  # noqa: E501

        :return: The model_start_date of this Rocket.
        :rtype: List[str]
        """
        return self._model_start_date

    @model_start_date.setter
    def model_start_date(self, model_start_date):
        """Sets the model_start_date of this Rocket.

        Description not available  # noqa: E501

        :param model_start_date: The model_start_date of this Rocket.
        :type model_start_date: List[str]
        """

        self._model_start_date = model_start_date

    @property
    def height(self):
        """Gets the height of this Rocket.

        Description not available  # noqa: E501

        :return: The height of this Rocket.
        :rtype: List[object]
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Rocket.

        Description not available  # noqa: E501

        :param height: The height of this Rocket.
        :type height: List[object]
        """

        self._height = height

    @property
    def model_end_date(self):
        """Gets the model_end_date of this Rocket.

        Description not available  # noqa: E501

        :return: The model_end_date of this Rocket.
        :rtype: List[str]
        """
        return self._model_end_date

    @model_end_date.setter
    def model_end_date(self, model_end_date):
        """Sets the model_end_date of this Rocket.

        Description not available  # noqa: E501

        :param model_end_date: The model_end_date of this Rocket.
        :type model_end_date: List[str]
        """

        self._model_end_date = model_end_date

    @property
    def number_of_launches(self):
        """Gets the number_of_launches of this Rocket.

        Description not available  # noqa: E501

        :return: The number_of_launches of this Rocket.
        :rtype: List[int]
        """
        return self._number_of_launches

    @number_of_launches.setter
    def number_of_launches(self, number_of_launches):
        """Sets the number_of_launches of this Rocket.

        Description not available  # noqa: E501

        :param number_of_launches: The number_of_launches of this Rocket.
        :type number_of_launches: List[int]
        """

        self._number_of_launches = number_of_launches

    @property
    def model_end_year(self):
        """Gets the model_end_year of this Rocket.

        Description not available  # noqa: E501

        :return: The model_end_year of this Rocket.
        :rtype: List[str]
        """
        return self._model_end_year

    @model_end_year.setter
    def model_end_year(self, model_end_year):
        """Sets the model_end_year of this Rocket.

        Description not available  # noqa: E501

        :param model_end_year: The model_end_year of this Rocket.
        :type model_end_year: List[str]
        """

        self._model_end_year = model_end_year

    @property
    def maiden_flight(self):
        """Gets the maiden_flight of this Rocket.

        date of maiden flight  # noqa: E501

        :return: The maiden_flight of this Rocket.
        :rtype: List[str]
        """
        return self._maiden_flight

    @maiden_flight.setter
    def maiden_flight(self, maiden_flight):
        """Sets the maiden_flight of this Rocket.

        date of maiden flight  # noqa: E501

        :param maiden_flight: The maiden_flight of this Rocket.
        :type maiden_flight: List[str]
        """

        self._maiden_flight = maiden_flight

    @property
    def length(self):
        """Gets the length of this Rocket.

        Description not available  # noqa: E501

        :return: The length of this Rocket.
        :rtype: List[object]
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Rocket.

        Description not available  # noqa: E501

        :param length: The length of this Rocket.
        :type length: List[object]
        """

        self._length = length

    @property
    def final_flight(self):
        """Gets the final_flight of this Rocket.

        date of final flight  # noqa: E501

        :return: The final_flight of this Rocket.
        :rtype: List[str]
        """
        return self._final_flight

    @final_flight.setter
    def final_flight(self, final_flight):
        """Sets the final_flight of this Rocket.

        date of final flight  # noqa: E501

        :param final_flight: The final_flight of this Rocket.
        :type final_flight: List[str]
        """

        self._final_flight = final_flight

    @property
    def weight(self):
        """Gets the weight of this Rocket.

        Description not available  # noqa: E501

        :return: The weight of this Rocket.
        :rtype: List[object]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Rocket.

        Description not available  # noqa: E501

        :param weight: The weight of this Rocket.
        :type weight: List[object]
        """

        self._weight = weight

    @property
    def label(self):
        """Gets the label of this Rocket.

        short description of the resource  # noqa: E501

        :return: The label of this Rocket.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Rocket.

        short description of the resource  # noqa: E501

        :param label: The label of this Rocket.
        :type label: List[str]
        """

        self._label = label

    @property
    def version(self):
        """Gets the version of this Rocket.

        Description not available  # noqa: E501

        :return: The version of this Rocket.
        :rtype: List[object]
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Rocket.

        Description not available  # noqa: E501

        :param version: The version of this Rocket.
        :type version: List[object]
        """

        self._version = version

    @property
    def number_of_seats(self):
        """Gets the number_of_seats of this Rocket.

        Description not available  # noqa: E501

        :return: The number_of_seats of this Rocket.
        :rtype: List[int]
        """
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, number_of_seats):
        """Sets the number_of_seats of this Rocket.

        Description not available  # noqa: E501

        :param number_of_seats: The number_of_seats of this Rocket.
        :type number_of_seats: List[int]
        """

        self._number_of_seats = number_of_seats

    @property
    def model_start_year(self):
        """Gets the model_start_year of this Rocket.

        Description not available  # noqa: E501

        :return: The model_start_year of this Rocket.
        :rtype: List[str]
        """
        return self._model_start_year

    @model_start_year.setter
    def model_start_year(self, model_start_year):
        """Sets the model_start_year of this Rocket.

        Description not available  # noqa: E501

        :param model_start_year: The model_start_year of this Rocket.
        :type model_start_year: List[str]
        """

        self._model_start_year = model_start_year

    @property
    def width(self):
        """Gets the width of this Rocket.

        Description not available  # noqa: E501

        :return: The width of this Rocket.
        :rtype: List[object]
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Rocket.

        Description not available  # noqa: E501

        :param width: The width of this Rocket.
        :type width: List[object]
        """

        self._width = width

    @property
    def discharge_average(self):
        """Gets the discharge_average of this Rocket.

        Description not available  # noqa: E501

        :return: The discharge_average of this Rocket.
        :rtype: List[float]
        """
        return self._discharge_average

    @discharge_average.setter
    def discharge_average(self, discharge_average):
        """Sets the discharge_average of this Rocket.

        Description not available  # noqa: E501

        :param discharge_average: The discharge_average of this Rocket.
        :type discharge_average: List[float]
        """

        self._discharge_average = discharge_average

    @property
    def number_of_crew(self):
        """Gets the number_of_crew of this Rocket.

        Description not available  # noqa: E501

        :return: The number_of_crew of this Rocket.
        :rtype: List[int]
        """
        return self._number_of_crew

    @number_of_crew.setter
    def number_of_crew(self, number_of_crew):
        """Sets the number_of_crew of this Rocket.

        Description not available  # noqa: E501

        :param number_of_crew: The number_of_crew of this Rocket.
        :type number_of_crew: List[int]
        """

        self._number_of_crew = number_of_crew

    @property
    def unknown_outcomes(self):
        """Gets the unknown_outcomes of this Rocket.

        number of launches with unknown outcomes (or in progress)  # noqa: E501

        :return: The unknown_outcomes of this Rocket.
        :rtype: List[int]
        """
        return self._unknown_outcomes

    @unknown_outcomes.setter
    def unknown_outcomes(self, unknown_outcomes):
        """Sets the unknown_outcomes of this Rocket.

        number of launches with unknown outcomes (or in progress)  # noqa: E501

        :param unknown_outcomes: The unknown_outcomes of this Rocket.
        :type unknown_outcomes: List[int]
        """

        self._unknown_outcomes = unknown_outcomes

    @property
    def country_origin(self):
        """Gets the country_origin of this Rocket.

        Description not available  # noqa: E501

        :return: The country_origin of this Rocket.
        :rtype: List[object]
        """
        return self._country_origin

    @country_origin.setter
    def country_origin(self, country_origin):
        """Sets the country_origin of this Rocket.

        Description not available  # noqa: E501

        :param country_origin: The country_origin of this Rocket.
        :type country_origin: List[object]
        """

        self._country_origin = country_origin

    @property
    def related_mean_of_transportation(self):
        """Gets the related_mean_of_transportation of this Rocket.

        Description not available  # noqa: E501

        :return: The related_mean_of_transportation of this Rocket.
        :rtype: List[object]
        """
        return self._related_mean_of_transportation

    @related_mean_of_transportation.setter
    def related_mean_of_transportation(self, related_mean_of_transportation):
        """Sets the related_mean_of_transportation of this Rocket.

        Description not available  # noqa: E501

        :param related_mean_of_transportation: The related_mean_of_transportation of this Rocket.
        :type related_mean_of_transportation: List[object]
        """

        self._related_mean_of_transportation = related_mean_of_transportation

    @property
    def comparable(self):
        """Gets the comparable of this Rocket.

        similar, unrelated rockets  # noqa: E501

        :return: The comparable of this Rocket.
        :rtype: List[object]
        """
        return self._comparable

    @comparable.setter
    def comparable(self, comparable):
        """Sets the comparable of this Rocket.

        similar, unrelated rockets  # noqa: E501

        :param comparable: The comparable of this Rocket.
        :type comparable: List[object]
        """

        self._comparable = comparable

    @property
    def power_type(self):
        """Gets the power_type of this Rocket.

        Description not available  # noqa: E501

        :return: The power_type of this Rocket.
        :rtype: List[object]
        """
        return self._power_type

    @power_type.setter
    def power_type(self, power_type):
        """Sets the power_type of this Rocket.

        Description not available  # noqa: E501

        :param power_type: The power_type of this Rocket.
        :type power_type: List[object]
        """

        self._power_type = power_type
