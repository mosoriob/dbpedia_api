# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ControlledDesignationOfOriginWine(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, approximate_calories=None, ingredient=None, taste=None, description=None, type_of_yeast=None, discontinued=None, label=None, type=None, percentage_alcohol=None, creator_of_dish=None, serving_temperature=None, introduced=None, type_of_storage=None, id=None, type_of_grain=None):  # noqa: E501
        """ControlledDesignationOfOriginWine - a model defined in OpenAPI

        :param approximate_calories: The approximate_calories of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type approximate_calories: List[float]
        :param ingredient: The ingredient of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type ingredient: List[object]
        :param taste: The taste of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type taste: List[str]
        :param description: The description of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type description: List[str]
        :param type_of_yeast: The type_of_yeast of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type type_of_yeast: List[str]
        :param discontinued: The discontinued of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type discontinued: List[str]
        :param label: The label of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type label: List[str]
        :param type: The type of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type type: List[str]
        :param percentage_alcohol: The percentage_alcohol of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type percentage_alcohol: List[int]
        :param creator_of_dish: The creator_of_dish of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type creator_of_dish: List[object]
        :param serving_temperature: The serving_temperature of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type serving_temperature: List[str]
        :param introduced: The introduced of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type introduced: List[str]
        :param type_of_storage: The type_of_storage of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type type_of_storage: List[str]
        :param id: The id of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type id: str
        :param type_of_grain: The type_of_grain of this ControlledDesignationOfOriginWine.  # noqa: E501
        :type type_of_grain: List[str]
        """


        self.openapi_types = {
            'approximate_calories': List[float],
            'ingredient': List[object],
            'taste': List[str],
            'description': List[str],
            'type_of_yeast': List[str],
            'discontinued': List[str],
            'label': List[str],
            'type': List[str],
            'percentage_alcohol': List[int],
            'creator_of_dish': List[object],
            'serving_temperature': List[str],
            'introduced': List[str],
            'type_of_storage': List[str],
            'id': str,
            'type_of_grain': List[str]
        }

        self.attribute_map = {
            'approximate_calories': 'approximateCalories',
            'ingredient': 'ingredient',
            'taste': 'taste',
            'description': 'description',
            'type_of_yeast': 'typeOfYeast',
            'discontinued': 'discontinued',
            'label': 'label',
            'type': 'type',
            'percentage_alcohol': 'percentageAlcohol',
            'creator_of_dish': 'creatorOfDish',
            'serving_temperature': 'servingTemperature',
            'introduced': 'introduced',
            'type_of_storage': 'typeOfStorage',
            'id': 'id',
            'type_of_grain': 'typeOfGrain'
        }

        self._approximate_calories = approximate_calories
        self._ingredient = ingredient
        self._taste = taste
        self._description = description
        self._type_of_yeast = type_of_yeast
        self._discontinued = discontinued
        self._label = label
        self._type = type
        self._percentage_alcohol = percentage_alcohol
        self._creator_of_dish = creator_of_dish
        self._serving_temperature = serving_temperature
        self._introduced = introduced
        self._type_of_storage = type_of_storage
        self._id = id
        self._type_of_grain = type_of_grain

    @classmethod
    def from_dict(cls, dikt) -> 'ControlledDesignationOfOriginWine':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ControlledDesignationOfOriginWine of this ControlledDesignationOfOriginWine.  # noqa: E501
        :rtype: ControlledDesignationOfOriginWine
        """
        return util.deserialize_model(dikt, cls)

    @property
    def approximate_calories(self):
        """Gets the approximate_calories of this ControlledDesignationOfOriginWine.

        Approximate calories per serving.  # noqa: E501

        :return: The approximate_calories of this ControlledDesignationOfOriginWine.
        :rtype: List[float]
        """
        return self._approximate_calories

    @approximate_calories.setter
    def approximate_calories(self, approximate_calories):
        """Sets the approximate_calories of this ControlledDesignationOfOriginWine.

        Approximate calories per serving.  # noqa: E501

        :param approximate_calories: The approximate_calories of this ControlledDesignationOfOriginWine.
        :type approximate_calories: List[float]
        """

        self._approximate_calories = approximate_calories

    @property
    def ingredient(self):
        """Gets the ingredient of this ControlledDesignationOfOriginWine.

        An ingredient is a substance that forms part of a mixture (in a general sense). Here it is used in the context of recipes that specify which ingredients are used to prepare a specific dish or drink.  # noqa: E501

        :return: The ingredient of this ControlledDesignationOfOriginWine.
        :rtype: List[object]
        """
        return self._ingredient

    @ingredient.setter
    def ingredient(self, ingredient):
        """Sets the ingredient of this ControlledDesignationOfOriginWine.

        An ingredient is a substance that forms part of a mixture (in a general sense). Here it is used in the context of recipes that specify which ingredients are used to prepare a specific dish or drink.  # noqa: E501

        :param ingredient: The ingredient of this ControlledDesignationOfOriginWine.
        :type ingredient: List[object]
        """

        self._ingredient = ingredient

    @property
    def taste(self):
        """Gets the taste of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :return: The taste of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._taste

    @taste.setter
    def taste(self, taste):
        """Sets the taste of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param taste: The taste of this ControlledDesignationOfOriginWine.
        :type taste: List[str]
        """

        self._taste = taste

    @property
    def description(self):
        """Gets the description of this ControlledDesignationOfOriginWine.

        small description  # noqa: E501

        :return: The description of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ControlledDesignationOfOriginWine.

        small description  # noqa: E501

        :param description: The description of this ControlledDesignationOfOriginWine.
        :type description: List[str]
        """

        self._description = description

    @property
    def type_of_yeast(self):
        """Gets the type_of_yeast of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :return: The type_of_yeast of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._type_of_yeast

    @type_of_yeast.setter
    def type_of_yeast(self, type_of_yeast):
        """Sets the type_of_yeast of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param type_of_yeast: The type_of_yeast of this ControlledDesignationOfOriginWine.
        :type type_of_yeast: List[str]
        """

        self._type_of_yeast = type_of_yeast

    @property
    def discontinued(self):
        """Gets the discontinued of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :return: The discontinued of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._discontinued

    @discontinued.setter
    def discontinued(self, discontinued):
        """Sets the discontinued of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param discontinued: The discontinued of this ControlledDesignationOfOriginWine.
        :type discontinued: List[str]
        """

        self._discontinued = discontinued

    @property
    def label(self):
        """Gets the label of this ControlledDesignationOfOriginWine.

        short description of the resource  # noqa: E501

        :return: The label of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ControlledDesignationOfOriginWine.

        short description of the resource  # noqa: E501

        :param label: The label of this ControlledDesignationOfOriginWine.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this ControlledDesignationOfOriginWine.

        type of the resource  # noqa: E501

        :return: The type of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ControlledDesignationOfOriginWine.

        type of the resource  # noqa: E501

        :param type: The type of this ControlledDesignationOfOriginWine.
        :type type: List[str]
        """

        self._type = type

    @property
    def percentage_alcohol(self):
        """Gets the percentage_alcohol of this ControlledDesignationOfOriginWine.

        percentage of alcohol present in a beverage  # noqa: E501

        :return: The percentage_alcohol of this ControlledDesignationOfOriginWine.
        :rtype: List[int]
        """
        return self._percentage_alcohol

    @percentage_alcohol.setter
    def percentage_alcohol(self, percentage_alcohol):
        """Sets the percentage_alcohol of this ControlledDesignationOfOriginWine.

        percentage of alcohol present in a beverage  # noqa: E501

        :param percentage_alcohol: The percentage_alcohol of this ControlledDesignationOfOriginWine.
        :type percentage_alcohol: List[int]
        """

        self._percentage_alcohol = percentage_alcohol

    @property
    def creator_of_dish(self):
        """Gets the creator_of_dish of this ControlledDesignationOfOriginWine.

        The person that creates (invents) the food (eg. Caesar Cardini is the creator of the Caesar salad).  # noqa: E501

        :return: The creator_of_dish of this ControlledDesignationOfOriginWine.
        :rtype: List[object]
        """
        return self._creator_of_dish

    @creator_of_dish.setter
    def creator_of_dish(self, creator_of_dish):
        """Sets the creator_of_dish of this ControlledDesignationOfOriginWine.

        The person that creates (invents) the food (eg. Caesar Cardini is the creator of the Caesar salad).  # noqa: E501

        :param creator_of_dish: The creator_of_dish of this ControlledDesignationOfOriginWine.
        :type creator_of_dish: List[object]
        """

        self._creator_of_dish = creator_of_dish

    @property
    def serving_temperature(self):
        """Gets the serving_temperature of this ControlledDesignationOfOriginWine.

        Serving temperature for the food (e.g.: hot, cold, warm or room temperature).  # noqa: E501

        :return: The serving_temperature of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._serving_temperature

    @serving_temperature.setter
    def serving_temperature(self, serving_temperature):
        """Sets the serving_temperature of this ControlledDesignationOfOriginWine.

        Serving temperature for the food (e.g.: hot, cold, warm or room temperature).  # noqa: E501

        :param serving_temperature: The serving_temperature of this ControlledDesignationOfOriginWine.
        :type serving_temperature: List[str]
        """

        self._serving_temperature = serving_temperature

    @property
    def introduced(self):
        """Gets the introduced of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :return: The introduced of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._introduced

    @introduced.setter
    def introduced(self, introduced):
        """Sets the introduced of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param introduced: The introduced of this ControlledDesignationOfOriginWine.
        :type introduced: List[str]
        """

        self._introduced = introduced

    @property
    def type_of_storage(self):
        """Gets the type_of_storage of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :return: The type_of_storage of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._type_of_storage

    @type_of_storage.setter
    def type_of_storage(self, type_of_storage):
        """Sets the type_of_storage of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param type_of_storage: The type_of_storage of this ControlledDesignationOfOriginWine.
        :type type_of_storage: List[str]
        """

        self._type_of_storage = type_of_storage

    @property
    def id(self):
        """Gets the id of this ControlledDesignationOfOriginWine.

        identifier  # noqa: E501

        :return: The id of this ControlledDesignationOfOriginWine.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ControlledDesignationOfOriginWine.

        identifier  # noqa: E501

        :param id: The id of this ControlledDesignationOfOriginWine.
        :type id: str
        """

        self._id = id

    @property
    def type_of_grain(self):
        """Gets the type_of_grain of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :return: The type_of_grain of this ControlledDesignationOfOriginWine.
        :rtype: List[str]
        """
        return self._type_of_grain

    @type_of_grain.setter
    def type_of_grain(self, type_of_grain):
        """Sets the type_of_grain of this ControlledDesignationOfOriginWine.

        Description not available  # noqa: E501

        :param type_of_grain: The type_of_grain of this ControlledDesignationOfOriginWine.
        :type type_of_grain: List[str]
        """

        self._type_of_grain = type_of_grain
