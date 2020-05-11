# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SocietalEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, number_of_people_attending=None, end_date=None, description=None, caused_by=None, label=None, type=None, participant=None, duration=None, previous_event=None, next_event=None, id=None, following_event=None, start_date=None):  # noqa: E501
        """SocietalEvent - a model defined in OpenAPI

        :param number_of_people_attending: The number_of_people_attending of this SocietalEvent.  # noqa: E501
        :type number_of_people_attending: List[int]
        :param end_date: The end_date of this SocietalEvent.  # noqa: E501
        :type end_date: List[str]
        :param description: The description of this SocietalEvent.  # noqa: E501
        :type description: List[str]
        :param caused_by: The caused_by of this SocietalEvent.  # noqa: E501
        :type caused_by: List[object]
        :param label: The label of this SocietalEvent.  # noqa: E501
        :type label: List[str]
        :param type: The type of this SocietalEvent.  # noqa: E501
        :type type: List[str]
        :param participant: The participant of this SocietalEvent.  # noqa: E501
        :type participant: List[str]
        :param duration: The duration of this SocietalEvent.  # noqa: E501
        :type duration: List[float]
        :param previous_event: The previous_event of this SocietalEvent.  # noqa: E501
        :type previous_event: List[object]
        :param next_event: The next_event of this SocietalEvent.  # noqa: E501
        :type next_event: List[object]
        :param id: The id of this SocietalEvent.  # noqa: E501
        :type id: str
        :param following_event: The following_event of this SocietalEvent.  # noqa: E501
        :type following_event: List[object]
        :param start_date: The start_date of this SocietalEvent.  # noqa: E501
        :type start_date: List[str]
        """


        self.openapi_types = {
            'number_of_people_attending': List[int],
            'end_date': List[str],
            'description': List[str],
            'caused_by': List[object],
            'label': List[str],
            'type': List[str],
            'participant': List[str],
            'duration': List[float],
            'previous_event': List[object],
            'next_event': List[object],
            'id': str,
            'following_event': List[object],
            'start_date': List[str]
        }

        self.attribute_map = {
            'number_of_people_attending': 'numberOfPeopleAttending',
            'end_date': 'endDate',
            'description': 'description',
            'caused_by': 'causedBy',
            'label': 'label',
            'type': 'type',
            'participant': 'participant',
            'duration': 'duration',
            'previous_event': 'previousEvent',
            'next_event': 'nextEvent',
            'id': 'id',
            'following_event': 'followingEvent',
            'start_date': 'startDate'
        }

        self._number_of_people_attending = number_of_people_attending
        self._end_date = end_date
        self._description = description
        self._caused_by = caused_by
        self._label = label
        self._type = type
        self._participant = participant
        self._duration = duration
        self._previous_event = previous_event
        self._next_event = next_event
        self._id = id
        self._following_event = following_event
        self._start_date = start_date

    @classmethod
    def from_dict(cls, dikt) -> 'SocietalEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SocietalEvent of this SocietalEvent.  # noqa: E501
        :rtype: SocietalEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number_of_people_attending(self):
        """Gets the number_of_people_attending of this SocietalEvent.

        Description not available  # noqa: E501

        :return: The number_of_people_attending of this SocietalEvent.
        :rtype: List[int]
        """
        return self._number_of_people_attending

    @number_of_people_attending.setter
    def number_of_people_attending(self, number_of_people_attending):
        """Sets the number_of_people_attending of this SocietalEvent.

        Description not available  # noqa: E501

        :param number_of_people_attending: The number_of_people_attending of this SocietalEvent.
        :type number_of_people_attending: List[int]
        """

        self._number_of_people_attending = number_of_people_attending

    @property
    def end_date(self):
        """Gets the end_date of this SocietalEvent.

        The end date of the event.  # noqa: E501

        :return: The end_date of this SocietalEvent.
        :rtype: List[str]
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SocietalEvent.

        The end date of the event.  # noqa: E501

        :param end_date: The end_date of this SocietalEvent.
        :type end_date: List[str]
        """

        self._end_date = end_date

    @property
    def description(self):
        """Gets the description of this SocietalEvent.

        small description  # noqa: E501

        :return: The description of this SocietalEvent.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SocietalEvent.

        small description  # noqa: E501

        :param description: The description of this SocietalEvent.
        :type description: List[str]
        """

        self._description = description

    @property
    def caused_by(self):
        """Gets the caused_by of this SocietalEvent.

        Description not available  # noqa: E501

        :return: The caused_by of this SocietalEvent.
        :rtype: List[object]
        """
        return self._caused_by

    @caused_by.setter
    def caused_by(self, caused_by):
        """Sets the caused_by of this SocietalEvent.

        Description not available  # noqa: E501

        :param caused_by: The caused_by of this SocietalEvent.
        :type caused_by: List[object]
        """

        self._caused_by = caused_by

    @property
    def label(self):
        """Gets the label of this SocietalEvent.

        short description of the resource  # noqa: E501

        :return: The label of this SocietalEvent.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SocietalEvent.

        short description of the resource  # noqa: E501

        :param label: The label of this SocietalEvent.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SocietalEvent.

        type of the resource  # noqa: E501

        :return: The type of this SocietalEvent.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SocietalEvent.

        type of the resource  # noqa: E501

        :param type: The type of this SocietalEvent.
        :type type: List[str]
        """

        self._type = type

    @property
    def participant(self):
        """Gets the participant of this SocietalEvent.

        Description not available  # noqa: E501

        :return: The participant of this SocietalEvent.
        :rtype: List[str]
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this SocietalEvent.

        Description not available  # noqa: E501

        :param participant: The participant of this SocietalEvent.
        :type participant: List[str]
        """

        self._participant = participant

    @property
    def duration(self):
        """Gets the duration of this SocietalEvent.

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :return: The duration of this SocietalEvent.
        :rtype: List[float]
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SocietalEvent.

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :param duration: The duration of this SocietalEvent.
        :type duration: List[float]
        """

        self._duration = duration

    @property
    def previous_event(self):
        """Gets the previous_event of this SocietalEvent.

        Description not available  # noqa: E501

        :return: The previous_event of this SocietalEvent.
        :rtype: List[object]
        """
        return self._previous_event

    @previous_event.setter
    def previous_event(self, previous_event):
        """Sets the previous_event of this SocietalEvent.

        Description not available  # noqa: E501

        :param previous_event: The previous_event of this SocietalEvent.
        :type previous_event: List[object]
        """

        self._previous_event = previous_event

    @property
    def next_event(self):
        """Gets the next_event of this SocietalEvent.

        Description not available  # noqa: E501

        :return: The next_event of this SocietalEvent.
        :rtype: List[object]
        """
        return self._next_event

    @next_event.setter
    def next_event(self, next_event):
        """Sets the next_event of this SocietalEvent.

        Description not available  # noqa: E501

        :param next_event: The next_event of this SocietalEvent.
        :type next_event: List[object]
        """

        self._next_event = next_event

    @property
    def id(self):
        """Gets the id of this SocietalEvent.

        identifier  # noqa: E501

        :return: The id of this SocietalEvent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SocietalEvent.

        identifier  # noqa: E501

        :param id: The id of this SocietalEvent.
        :type id: str
        """

        self._id = id

    @property
    def following_event(self):
        """Gets the following_event of this SocietalEvent.

        Description not available  # noqa: E501

        :return: The following_event of this SocietalEvent.
        :rtype: List[object]
        """
        return self._following_event

    @following_event.setter
    def following_event(self, following_event):
        """Sets the following_event of this SocietalEvent.

        Description not available  # noqa: E501

        :param following_event: The following_event of this SocietalEvent.
        :type following_event: List[object]
        """

        self._following_event = following_event

    @property
    def start_date(self):
        """Gets the start_date of this SocietalEvent.

        The start date of the event.  # noqa: E501

        :return: The start_date of this SocietalEvent.
        :rtype: List[str]
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SocietalEvent.

        The start date of the event.  # noqa: E501

        :param start_date: The start_date of this SocietalEvent.
        :type start_date: List[str]
        """

        self._start_date = start_date
