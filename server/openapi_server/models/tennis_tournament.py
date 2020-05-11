# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TennisTournament(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, number_of_people_attending=None, end_date=None, description=None, type=None, silver_medalist=None, participant=None, duration=None, medalist=None, previous_event=None, champion_in_single_female=None, champion_in_double_male=None, id=None, following_event=None, champion_in_single_male=None, bronze_medalist=None, champion_in_mixed_double=None, caused_by=None, label=None, gold_medalist=None, champion_in_single=None, race_track=None, next_event=None, champion_in_double_female=None, champion_in_double=None, start_date=None, champion=None):  # noqa: E501
        """TennisTournament - a model defined in OpenAPI

        :param number_of_people_attending: The number_of_people_attending of this TennisTournament.  # noqa: E501
        :type number_of_people_attending: List[int]
        :param end_date: The end_date of this TennisTournament.  # noqa: E501
        :type end_date: List[str]
        :param description: The description of this TennisTournament.  # noqa: E501
        :type description: List[str]
        :param type: The type of this TennisTournament.  # noqa: E501
        :type type: List[str]
        :param silver_medalist: The silver_medalist of this TennisTournament.  # noqa: E501
        :type silver_medalist: List[object]
        :param participant: The participant of this TennisTournament.  # noqa: E501
        :type participant: List[str]
        :param duration: The duration of this TennisTournament.  # noqa: E501
        :type duration: List[float]
        :param medalist: The medalist of this TennisTournament.  # noqa: E501
        :type medalist: List[object]
        :param previous_event: The previous_event of this TennisTournament.  # noqa: E501
        :type previous_event: List[object]
        :param champion_in_single_female: The champion_in_single_female of this TennisTournament.  # noqa: E501
        :type champion_in_single_female: List[object]
        :param champion_in_double_male: The champion_in_double_male of this TennisTournament.  # noqa: E501
        :type champion_in_double_male: List[object]
        :param id: The id of this TennisTournament.  # noqa: E501
        :type id: str
        :param following_event: The following_event of this TennisTournament.  # noqa: E501
        :type following_event: List[object]
        :param champion_in_single_male: The champion_in_single_male of this TennisTournament.  # noqa: E501
        :type champion_in_single_male: List[object]
        :param bronze_medalist: The bronze_medalist of this TennisTournament.  # noqa: E501
        :type bronze_medalist: List[object]
        :param champion_in_mixed_double: The champion_in_mixed_double of this TennisTournament.  # noqa: E501
        :type champion_in_mixed_double: List[object]
        :param caused_by: The caused_by of this TennisTournament.  # noqa: E501
        :type caused_by: List[object]
        :param label: The label of this TennisTournament.  # noqa: E501
        :type label: List[str]
        :param gold_medalist: The gold_medalist of this TennisTournament.  # noqa: E501
        :type gold_medalist: List[object]
        :param champion_in_single: The champion_in_single of this TennisTournament.  # noqa: E501
        :type champion_in_single: List[object]
        :param race_track: The race_track of this TennisTournament.  # noqa: E501
        :type race_track: List[object]
        :param next_event: The next_event of this TennisTournament.  # noqa: E501
        :type next_event: List[object]
        :param champion_in_double_female: The champion_in_double_female of this TennisTournament.  # noqa: E501
        :type champion_in_double_female: List[object]
        :param champion_in_double: The champion_in_double of this TennisTournament.  # noqa: E501
        :type champion_in_double: List[object]
        :param start_date: The start_date of this TennisTournament.  # noqa: E501
        :type start_date: List[str]
        :param champion: The champion of this TennisTournament.  # noqa: E501
        :type champion: List[object]
        """


        self.openapi_types = {
            'number_of_people_attending': List[int],
            'end_date': List[str],
            'description': List[str],
            'type': List[str],
            'silver_medalist': List[object],
            'participant': List[str],
            'duration': List[float],
            'medalist': List[object],
            'previous_event': List[object],
            'champion_in_single_female': List[object],
            'champion_in_double_male': List[object],
            'id': str,
            'following_event': List[object],
            'champion_in_single_male': List[object],
            'bronze_medalist': List[object],
            'champion_in_mixed_double': List[object],
            'caused_by': List[object],
            'label': List[str],
            'gold_medalist': List[object],
            'champion_in_single': List[object],
            'race_track': List[object],
            'next_event': List[object],
            'champion_in_double_female': List[object],
            'champion_in_double': List[object],
            'start_date': List[str],
            'champion': List[object]
        }

        self.attribute_map = {
            'number_of_people_attending': 'numberOfPeopleAttending',
            'end_date': 'endDate',
            'description': 'description',
            'type': 'type',
            'silver_medalist': 'silverMedalist',
            'participant': 'participant',
            'duration': 'duration',
            'medalist': 'medalist',
            'previous_event': 'previousEvent',
            'champion_in_single_female': 'championInSingleFemale',
            'champion_in_double_male': 'championInDoubleMale',
            'id': 'id',
            'following_event': 'followingEvent',
            'champion_in_single_male': 'championInSingleMale',
            'bronze_medalist': 'bronzeMedalist',
            'champion_in_mixed_double': 'championInMixedDouble',
            'caused_by': 'causedBy',
            'label': 'label',
            'gold_medalist': 'goldMedalist',
            'champion_in_single': 'championInSingle',
            'race_track': 'raceTrack',
            'next_event': 'nextEvent',
            'champion_in_double_female': 'championInDoubleFemale',
            'champion_in_double': 'championInDouble',
            'start_date': 'startDate',
            'champion': 'champion'
        }

        self._number_of_people_attending = number_of_people_attending
        self._end_date = end_date
        self._description = description
        self._type = type
        self._silver_medalist = silver_medalist
        self._participant = participant
        self._duration = duration
        self._medalist = medalist
        self._previous_event = previous_event
        self._champion_in_single_female = champion_in_single_female
        self._champion_in_double_male = champion_in_double_male
        self._id = id
        self._following_event = following_event
        self._champion_in_single_male = champion_in_single_male
        self._bronze_medalist = bronze_medalist
        self._champion_in_mixed_double = champion_in_mixed_double
        self._caused_by = caused_by
        self._label = label
        self._gold_medalist = gold_medalist
        self._champion_in_single = champion_in_single
        self._race_track = race_track
        self._next_event = next_event
        self._champion_in_double_female = champion_in_double_female
        self._champion_in_double = champion_in_double
        self._start_date = start_date
        self._champion = champion

    @classmethod
    def from_dict(cls, dikt) -> 'TennisTournament':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TennisTournament of this TennisTournament.  # noqa: E501
        :rtype: TennisTournament
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number_of_people_attending(self):
        """Gets the number_of_people_attending of this TennisTournament.

        Description not available  # noqa: E501

        :return: The number_of_people_attending of this TennisTournament.
        :rtype: List[int]
        """
        return self._number_of_people_attending

    @number_of_people_attending.setter
    def number_of_people_attending(self, number_of_people_attending):
        """Sets the number_of_people_attending of this TennisTournament.

        Description not available  # noqa: E501

        :param number_of_people_attending: The number_of_people_attending of this TennisTournament.
        :type number_of_people_attending: List[int]
        """

        self._number_of_people_attending = number_of_people_attending

    @property
    def end_date(self):
        """Gets the end_date of this TennisTournament.

        The end date of the event.  # noqa: E501

        :return: The end_date of this TennisTournament.
        :rtype: List[str]
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TennisTournament.

        The end date of the event.  # noqa: E501

        :param end_date: The end_date of this TennisTournament.
        :type end_date: List[str]
        """

        self._end_date = end_date

    @property
    def description(self):
        """Gets the description of this TennisTournament.

        small description  # noqa: E501

        :return: The description of this TennisTournament.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TennisTournament.

        small description  # noqa: E501

        :param description: The description of this TennisTournament.
        :type description: List[str]
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this TennisTournament.

        type of the resource  # noqa: E501

        :return: The type of this TennisTournament.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TennisTournament.

        type of the resource  # noqa: E501

        :param type: The type of this TennisTournament.
        :type type: List[str]
        """

        self._type = type

    @property
    def silver_medalist(self):
        """Gets the silver_medalist of this TennisTournament.

        Description not available  # noqa: E501

        :return: The silver_medalist of this TennisTournament.
        :rtype: List[object]
        """
        return self._silver_medalist

    @silver_medalist.setter
    def silver_medalist(self, silver_medalist):
        """Sets the silver_medalist of this TennisTournament.

        Description not available  # noqa: E501

        :param silver_medalist: The silver_medalist of this TennisTournament.
        :type silver_medalist: List[object]
        """

        self._silver_medalist = silver_medalist

    @property
    def participant(self):
        """Gets the participant of this TennisTournament.

        Description not available  # noqa: E501

        :return: The participant of this TennisTournament.
        :rtype: List[str]
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this TennisTournament.

        Description not available  # noqa: E501

        :param participant: The participant of this TennisTournament.
        :type participant: List[str]
        """

        self._participant = participant

    @property
    def duration(self):
        """Gets the duration of this TennisTournament.

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :return: The duration of this TennisTournament.
        :rtype: List[float]
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TennisTournament.

        The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format  # noqa: E501

        :param duration: The duration of this TennisTournament.
        :type duration: List[float]
        """

        self._duration = duration

    @property
    def medalist(self):
        """Gets the medalist of this TennisTournament.

        Description not available  # noqa: E501

        :return: The medalist of this TennisTournament.
        :rtype: List[object]
        """
        return self._medalist

    @medalist.setter
    def medalist(self, medalist):
        """Sets the medalist of this TennisTournament.

        Description not available  # noqa: E501

        :param medalist: The medalist of this TennisTournament.
        :type medalist: List[object]
        """

        self._medalist = medalist

    @property
    def previous_event(self):
        """Gets the previous_event of this TennisTournament.

        Description not available  # noqa: E501

        :return: The previous_event of this TennisTournament.
        :rtype: List[object]
        """
        return self._previous_event

    @previous_event.setter
    def previous_event(self, previous_event):
        """Sets the previous_event of this TennisTournament.

        Description not available  # noqa: E501

        :param previous_event: The previous_event of this TennisTournament.
        :type previous_event: List[object]
        """

        self._previous_event = previous_event

    @property
    def champion_in_single_female(self):
        """Gets the champion_in_single_female of this TennisTournament.

        winner of a competition in the single female session, to distinguish from the double session (as in tennis)  # noqa: E501

        :return: The champion_in_single_female of this TennisTournament.
        :rtype: List[object]
        """
        return self._champion_in_single_female

    @champion_in_single_female.setter
    def champion_in_single_female(self, champion_in_single_female):
        """Sets the champion_in_single_female of this TennisTournament.

        winner of a competition in the single female session, to distinguish from the double session (as in tennis)  # noqa: E501

        :param champion_in_single_female: The champion_in_single_female of this TennisTournament.
        :type champion_in_single_female: List[object]
        """

        self._champion_in_single_female = champion_in_single_female

    @property
    def champion_in_double_male(self):
        """Gets the champion_in_double_male of this TennisTournament.

        winner of a competition in the male double session (as in tennis)  # noqa: E501

        :return: The champion_in_double_male of this TennisTournament.
        :rtype: List[object]
        """
        return self._champion_in_double_male

    @champion_in_double_male.setter
    def champion_in_double_male(self, champion_in_double_male):
        """Sets the champion_in_double_male of this TennisTournament.

        winner of a competition in the male double session (as in tennis)  # noqa: E501

        :param champion_in_double_male: The champion_in_double_male of this TennisTournament.
        :type champion_in_double_male: List[object]
        """

        self._champion_in_double_male = champion_in_double_male

    @property
    def id(self):
        """Gets the id of this TennisTournament.

        identifier  # noqa: E501

        :return: The id of this TennisTournament.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TennisTournament.

        identifier  # noqa: E501

        :param id: The id of this TennisTournament.
        :type id: str
        """

        self._id = id

    @property
    def following_event(self):
        """Gets the following_event of this TennisTournament.

        Description not available  # noqa: E501

        :return: The following_event of this TennisTournament.
        :rtype: List[object]
        """
        return self._following_event

    @following_event.setter
    def following_event(self, following_event):
        """Sets the following_event of this TennisTournament.

        Description not available  # noqa: E501

        :param following_event: The following_event of this TennisTournament.
        :type following_event: List[object]
        """

        self._following_event = following_event

    @property
    def champion_in_single_male(self):
        """Gets the champion_in_single_male of this TennisTournament.

        winner of a competition in the single male session, to distinguish from the double session (as in tennis)  # noqa: E501

        :return: The champion_in_single_male of this TennisTournament.
        :rtype: List[object]
        """
        return self._champion_in_single_male

    @champion_in_single_male.setter
    def champion_in_single_male(self, champion_in_single_male):
        """Sets the champion_in_single_male of this TennisTournament.

        winner of a competition in the single male session, to distinguish from the double session (as in tennis)  # noqa: E501

        :param champion_in_single_male: The champion_in_single_male of this TennisTournament.
        :type champion_in_single_male: List[object]
        """

        self._champion_in_single_male = champion_in_single_male

    @property
    def bronze_medalist(self):
        """Gets the bronze_medalist of this TennisTournament.

        Description not available  # noqa: E501

        :return: The bronze_medalist of this TennisTournament.
        :rtype: List[object]
        """
        return self._bronze_medalist

    @bronze_medalist.setter
    def bronze_medalist(self, bronze_medalist):
        """Sets the bronze_medalist of this TennisTournament.

        Description not available  # noqa: E501

        :param bronze_medalist: The bronze_medalist of this TennisTournament.
        :type bronze_medalist: List[object]
        """

        self._bronze_medalist = bronze_medalist

    @property
    def champion_in_mixed_double(self):
        """Gets the champion_in_mixed_double of this TennisTournament.

        winner of a competition in the mixed double session (as in tennis)  # noqa: E501

        :return: The champion_in_mixed_double of this TennisTournament.
        :rtype: List[object]
        """
        return self._champion_in_mixed_double

    @champion_in_mixed_double.setter
    def champion_in_mixed_double(self, champion_in_mixed_double):
        """Sets the champion_in_mixed_double of this TennisTournament.

        winner of a competition in the mixed double session (as in tennis)  # noqa: E501

        :param champion_in_mixed_double: The champion_in_mixed_double of this TennisTournament.
        :type champion_in_mixed_double: List[object]
        """

        self._champion_in_mixed_double = champion_in_mixed_double

    @property
    def caused_by(self):
        """Gets the caused_by of this TennisTournament.

        Description not available  # noqa: E501

        :return: The caused_by of this TennisTournament.
        :rtype: List[object]
        """
        return self._caused_by

    @caused_by.setter
    def caused_by(self, caused_by):
        """Sets the caused_by of this TennisTournament.

        Description not available  # noqa: E501

        :param caused_by: The caused_by of this TennisTournament.
        :type caused_by: List[object]
        """

        self._caused_by = caused_by

    @property
    def label(self):
        """Gets the label of this TennisTournament.

        short description of the resource  # noqa: E501

        :return: The label of this TennisTournament.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TennisTournament.

        short description of the resource  # noqa: E501

        :param label: The label of this TennisTournament.
        :type label: List[str]
        """

        self._label = label

    @property
    def gold_medalist(self):
        """Gets the gold_medalist of this TennisTournament.

        Description not available  # noqa: E501

        :return: The gold_medalist of this TennisTournament.
        :rtype: List[object]
        """
        return self._gold_medalist

    @gold_medalist.setter
    def gold_medalist(self, gold_medalist):
        """Sets the gold_medalist of this TennisTournament.

        Description not available  # noqa: E501

        :param gold_medalist: The gold_medalist of this TennisTournament.
        :type gold_medalist: List[object]
        """

        self._gold_medalist = gold_medalist

    @property
    def champion_in_single(self):
        """Gets the champion_in_single of this TennisTournament.

        winner of a competition in the single session, to distinguish from the double session (as in tennis)  # noqa: E501

        :return: The champion_in_single of this TennisTournament.
        :rtype: List[object]
        """
        return self._champion_in_single

    @champion_in_single.setter
    def champion_in_single(self, champion_in_single):
        """Sets the champion_in_single of this TennisTournament.

        winner of a competition in the single session, to distinguish from the double session (as in tennis)  # noqa: E501

        :param champion_in_single: The champion_in_single of this TennisTournament.
        :type champion_in_single: List[object]
        """

        self._champion_in_single = champion_in_single

    @property
    def race_track(self):
        """Gets the race_track of this TennisTournament.

        Description not available  # noqa: E501

        :return: The race_track of this TennisTournament.
        :rtype: List[object]
        """
        return self._race_track

    @race_track.setter
    def race_track(self, race_track):
        """Sets the race_track of this TennisTournament.

        Description not available  # noqa: E501

        :param race_track: The race_track of this TennisTournament.
        :type race_track: List[object]
        """

        self._race_track = race_track

    @property
    def next_event(self):
        """Gets the next_event of this TennisTournament.

        Description not available  # noqa: E501

        :return: The next_event of this TennisTournament.
        :rtype: List[object]
        """
        return self._next_event

    @next_event.setter
    def next_event(self, next_event):
        """Sets the next_event of this TennisTournament.

        Description not available  # noqa: E501

        :param next_event: The next_event of this TennisTournament.
        :type next_event: List[object]
        """

        self._next_event = next_event

    @property
    def champion_in_double_female(self):
        """Gets the champion_in_double_female of this TennisTournament.

        winner of a competition in the female double session (as in tennis)  # noqa: E501

        :return: The champion_in_double_female of this TennisTournament.
        :rtype: List[object]
        """
        return self._champion_in_double_female

    @champion_in_double_female.setter
    def champion_in_double_female(self, champion_in_double_female):
        """Sets the champion_in_double_female of this TennisTournament.

        winner of a competition in the female double session (as in tennis)  # noqa: E501

        :param champion_in_double_female: The champion_in_double_female of this TennisTournament.
        :type champion_in_double_female: List[object]
        """

        self._champion_in_double_female = champion_in_double_female

    @property
    def champion_in_double(self):
        """Gets the champion_in_double of this TennisTournament.

        winner of a competition in the double session (as in tennis)  # noqa: E501

        :return: The champion_in_double of this TennisTournament.
        :rtype: List[object]
        """
        return self._champion_in_double

    @champion_in_double.setter
    def champion_in_double(self, champion_in_double):
        """Sets the champion_in_double of this TennisTournament.

        winner of a competition in the double session (as in tennis)  # noqa: E501

        :param champion_in_double: The champion_in_double of this TennisTournament.
        :type champion_in_double: List[object]
        """

        self._champion_in_double = champion_in_double

    @property
    def start_date(self):
        """Gets the start_date of this TennisTournament.

        The start date of the event.  # noqa: E501

        :return: The start_date of this TennisTournament.
        :rtype: List[str]
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TennisTournament.

        The start date of the event.  # noqa: E501

        :param start_date: The start_date of this TennisTournament.
        :type start_date: List[str]
        """

        self._start_date = start_date

    @property
    def champion(self):
        """Gets the champion of this TennisTournament.

        winner of a competition  # noqa: E501

        :return: The champion of this TennisTournament.
        :rtype: List[object]
        """
        return self._champion

    @champion.setter
    def champion(self, champion):
        """Sets the champion of this TennisTournament.

        winner of a competition  # noqa: E501

        :param champion: The champion of this TennisTournament.
        :type champion: List[object]
        """

        self._champion = champion
