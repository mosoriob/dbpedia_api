# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NationalAnthem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, previous_work=None, artist=None, translator=None, alternative_title=None, description=None, subsequent_work=None, chief_editor=None, music_composer=None, type=None, main_character=None, record_date=None, id=None, based_on=None, recorded_in=None, release_date=None, composer=None, author=None, runtime=None, production_company=None, label=None, original_language=None, license=None, subject_term=None, musical_key=None, original_title=None, producer=None, starring=None, completion_date=None, writer=None, music_type=None):  # noqa: E501
        """NationalAnthem - a model defined in OpenAPI

        :param previous_work: The previous_work of this NationalAnthem.  # noqa: E501
        :type previous_work: List[object]
        :param artist: The artist of this NationalAnthem.  # noqa: E501
        :type artist: List[object]
        :param translator: The translator of this NationalAnthem.  # noqa: E501
        :type translator: List[object]
        :param alternative_title: The alternative_title of this NationalAnthem.  # noqa: E501
        :type alternative_title: List[str]
        :param description: The description of this NationalAnthem.  # noqa: E501
        :type description: List[str]
        :param subsequent_work: The subsequent_work of this NationalAnthem.  # noqa: E501
        :type subsequent_work: List[object]
        :param chief_editor: The chief_editor of this NationalAnthem.  # noqa: E501
        :type chief_editor: List[object]
        :param music_composer: The music_composer of this NationalAnthem.  # noqa: E501
        :type music_composer: List[object]
        :param type: The type of this NationalAnthem.  # noqa: E501
        :type type: List[str]
        :param main_character: The main_character of this NationalAnthem.  # noqa: E501
        :type main_character: List[object]
        :param record_date: The record_date of this NationalAnthem.  # noqa: E501
        :type record_date: List[str]
        :param id: The id of this NationalAnthem.  # noqa: E501
        :type id: str
        :param based_on: The based_on of this NationalAnthem.  # noqa: E501
        :type based_on: List[object]
        :param recorded_in: The recorded_in of this NationalAnthem.  # noqa: E501
        :type recorded_in: List[object]
        :param release_date: The release_date of this NationalAnthem.  # noqa: E501
        :type release_date: List[str]
        :param composer: The composer of this NationalAnthem.  # noqa: E501
        :type composer: List[object]
        :param author: The author of this NationalAnthem.  # noqa: E501
        :type author: List[object]
        :param runtime: The runtime of this NationalAnthem.  # noqa: E501
        :type runtime: List[object]
        :param production_company: The production_company of this NationalAnthem.  # noqa: E501
        :type production_company: List[object]
        :param label: The label of this NationalAnthem.  # noqa: E501
        :type label: List[str]
        :param original_language: The original_language of this NationalAnthem.  # noqa: E501
        :type original_language: List[object]
        :param license: The license of this NationalAnthem.  # noqa: E501
        :type license: List[object]
        :param subject_term: The subject_term of this NationalAnthem.  # noqa: E501
        :type subject_term: List[str]
        :param musical_key: The musical_key of this NationalAnthem.  # noqa: E501
        :type musical_key: List[str]
        :param original_title: The original_title of this NationalAnthem.  # noqa: E501
        :type original_title: List[str]
        :param producer: The producer of this NationalAnthem.  # noqa: E501
        :type producer: List[object]
        :param starring: The starring of this NationalAnthem.  # noqa: E501
        :type starring: List[object]
        :param completion_date: The completion_date of this NationalAnthem.  # noqa: E501
        :type completion_date: List[str]
        :param writer: The writer of this NationalAnthem.  # noqa: E501
        :type writer: List[object]
        :param music_type: The music_type of this NationalAnthem.  # noqa: E501
        :type music_type: List[object]
        """


        self.openapi_types = {
            'previous_work': List[object],
            'artist': List[object],
            'translator': List[object],
            'alternative_title': List[str],
            'description': List[str],
            'subsequent_work': List[object],
            'chief_editor': List[object],
            'music_composer': List[object],
            'type': List[str],
            'main_character': List[object],
            'record_date': List[str],
            'id': str,
            'based_on': List[object],
            'recorded_in': List[object],
            'release_date': List[str],
            'composer': List[object],
            'author': List[object],
            'runtime': List[object],
            'production_company': List[object],
            'label': List[str],
            'original_language': List[object],
            'license': List[object],
            'subject_term': List[str],
            'musical_key': List[str],
            'original_title': List[str],
            'producer': List[object],
            'starring': List[object],
            'completion_date': List[str],
            'writer': List[object],
            'music_type': List[object]
        }

        self.attribute_map = {
            'previous_work': 'previousWork',
            'artist': 'artist',
            'translator': 'translator',
            'alternative_title': 'alternativeTitle',
            'description': 'description',
            'subsequent_work': 'subsequentWork',
            'chief_editor': 'chiefEditor',
            'music_composer': 'musicComposer',
            'type': 'type',
            'main_character': 'mainCharacter',
            'record_date': 'recordDate',
            'id': 'id',
            'based_on': 'basedOn',
            'recorded_in': 'recordedIn',
            'release_date': 'releaseDate',
            'composer': 'composer',
            'author': 'author',
            'runtime': 'runtime',
            'production_company': 'productionCompany',
            'label': 'label',
            'original_language': 'originalLanguage',
            'license': 'license',
            'subject_term': 'subjectTerm',
            'musical_key': 'musicalKey',
            'original_title': 'originalTitle',
            'producer': 'producer',
            'starring': 'starring',
            'completion_date': 'completionDate',
            'writer': 'writer',
            'music_type': 'musicType'
        }

        self._previous_work = previous_work
        self._artist = artist
        self._translator = translator
        self._alternative_title = alternative_title
        self._description = description
        self._subsequent_work = subsequent_work
        self._chief_editor = chief_editor
        self._music_composer = music_composer
        self._type = type
        self._main_character = main_character
        self._record_date = record_date
        self._id = id
        self._based_on = based_on
        self._recorded_in = recorded_in
        self._release_date = release_date
        self._composer = composer
        self._author = author
        self._runtime = runtime
        self._production_company = production_company
        self._label = label
        self._original_language = original_language
        self._license = license
        self._subject_term = subject_term
        self._musical_key = musical_key
        self._original_title = original_title
        self._producer = producer
        self._starring = starring
        self._completion_date = completion_date
        self._writer = writer
        self._music_type = music_type

    @classmethod
    def from_dict(cls, dikt) -> 'NationalAnthem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NationalAnthem of this NationalAnthem.  # noqa: E501
        :rtype: NationalAnthem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def previous_work(self):
        """Gets the previous_work of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The previous_work of this NationalAnthem.
        :rtype: List[object]
        """
        return self._previous_work

    @previous_work.setter
    def previous_work(self, previous_work):
        """Sets the previous_work of this NationalAnthem.

        Description not available  # noqa: E501

        :param previous_work: The previous_work of this NationalAnthem.
        :type previous_work: List[object]
        """

        self._previous_work = previous_work

    @property
    def artist(self):
        """Gets the artist of this NationalAnthem.

        The performer or creator of the musical work.  # noqa: E501

        :return: The artist of this NationalAnthem.
        :rtype: List[object]
        """
        return self._artist

    @artist.setter
    def artist(self, artist):
        """Sets the artist of this NationalAnthem.

        The performer or creator of the musical work.  # noqa: E501

        :param artist: The artist of this NationalAnthem.
        :type artist: List[object]
        """

        self._artist = artist

    @property
    def translator(self):
        """Gets the translator of this NationalAnthem.

        Translator(s), if original not in English  # noqa: E501

        :return: The translator of this NationalAnthem.
        :rtype: List[object]
        """
        return self._translator

    @translator.setter
    def translator(self, translator):
        """Sets the translator of this NationalAnthem.

        Translator(s), if original not in English  # noqa: E501

        :param translator: The translator of this NationalAnthem.
        :type translator: List[object]
        """

        self._translator = translator

    @property
    def alternative_title(self):
        """Gets the alternative_title of this NationalAnthem.

        The alternative title attributed to a work  # noqa: E501

        :return: The alternative_title of this NationalAnthem.
        :rtype: List[str]
        """
        return self._alternative_title

    @alternative_title.setter
    def alternative_title(self, alternative_title):
        """Sets the alternative_title of this NationalAnthem.

        The alternative title attributed to a work  # noqa: E501

        :param alternative_title: The alternative_title of this NationalAnthem.
        :type alternative_title: List[str]
        """

        self._alternative_title = alternative_title

    @property
    def description(self):
        """Gets the description of this NationalAnthem.

        small description  # noqa: E501

        :return: The description of this NationalAnthem.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NationalAnthem.

        small description  # noqa: E501

        :param description: The description of this NationalAnthem.
        :type description: List[str]
        """

        self._description = description

    @property
    def subsequent_work(self):
        """Gets the subsequent_work of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The subsequent_work of this NationalAnthem.
        :rtype: List[object]
        """
        return self._subsequent_work

    @subsequent_work.setter
    def subsequent_work(self, subsequent_work):
        """Sets the subsequent_work of this NationalAnthem.

        Description not available  # noqa: E501

        :param subsequent_work: The subsequent_work of this NationalAnthem.
        :type subsequent_work: List[object]
        """

        self._subsequent_work = subsequent_work

    @property
    def chief_editor(self):
        """Gets the chief_editor of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The chief_editor of this NationalAnthem.
        :rtype: List[object]
        """
        return self._chief_editor

    @chief_editor.setter
    def chief_editor(self, chief_editor):
        """Sets the chief_editor of this NationalAnthem.

        Description not available  # noqa: E501

        :param chief_editor: The chief_editor of this NationalAnthem.
        :type chief_editor: List[object]
        """

        self._chief_editor = chief_editor

    @property
    def music_composer(self):
        """Gets the music_composer of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The music_composer of this NationalAnthem.
        :rtype: List[object]
        """
        return self._music_composer

    @music_composer.setter
    def music_composer(self, music_composer):
        """Sets the music_composer of this NationalAnthem.

        Description not available  # noqa: E501

        :param music_composer: The music_composer of this NationalAnthem.
        :type music_composer: List[object]
        """

        self._music_composer = music_composer

    @property
    def type(self):
        """Gets the type of this NationalAnthem.

        type of the resource  # noqa: E501

        :return: The type of this NationalAnthem.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NationalAnthem.

        type of the resource  # noqa: E501

        :param type: The type of this NationalAnthem.
        :type type: List[str]
        """

        self._type = type

    @property
    def main_character(self):
        """Gets the main_character of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The main_character of this NationalAnthem.
        :rtype: List[object]
        """
        return self._main_character

    @main_character.setter
    def main_character(self, main_character):
        """Sets the main_character of this NationalAnthem.

        Description not available  # noqa: E501

        :param main_character: The main_character of this NationalAnthem.
        :type main_character: List[object]
        """

        self._main_character = main_character

    @property
    def record_date(self):
        """Gets the record_date of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The record_date of this NationalAnthem.
        :rtype: List[str]
        """
        return self._record_date

    @record_date.setter
    def record_date(self, record_date):
        """Sets the record_date of this NationalAnthem.

        Description not available  # noqa: E501

        :param record_date: The record_date of this NationalAnthem.
        :type record_date: List[str]
        """

        self._record_date = record_date

    @property
    def id(self):
        """Gets the id of this NationalAnthem.

        identifier  # noqa: E501

        :return: The id of this NationalAnthem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NationalAnthem.

        identifier  # noqa: E501

        :param id: The id of this NationalAnthem.
        :type id: str
        """

        self._id = id

    @property
    def based_on(self):
        """Gets the based_on of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The based_on of this NationalAnthem.
        :rtype: List[object]
        """
        return self._based_on

    @based_on.setter
    def based_on(self, based_on):
        """Sets the based_on of this NationalAnthem.

        Description not available  # noqa: E501

        :param based_on: The based_on of this NationalAnthem.
        :type based_on: List[object]
        """

        self._based_on = based_on

    @property
    def recorded_in(self):
        """Gets the recorded_in of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The recorded_in of this NationalAnthem.
        :rtype: List[object]
        """
        return self._recorded_in

    @recorded_in.setter
    def recorded_in(self, recorded_in):
        """Sets the recorded_in of this NationalAnthem.

        Description not available  # noqa: E501

        :param recorded_in: The recorded_in of this NationalAnthem.
        :type recorded_in: List[object]
        """

        self._recorded_in = recorded_in

    @property
    def release_date(self):
        """Gets the release_date of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The release_date of this NationalAnthem.
        :rtype: List[str]
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this NationalAnthem.

        Description not available  # noqa: E501

        :param release_date: The release_date of this NationalAnthem.
        :type release_date: List[str]
        """

        self._release_date = release_date

    @property
    def composer(self):
        """Gets the composer of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The composer of this NationalAnthem.
        :rtype: List[object]
        """
        return self._composer

    @composer.setter
    def composer(self, composer):
        """Sets the composer of this NationalAnthem.

        Description not available  # noqa: E501

        :param composer: The composer of this NationalAnthem.
        :type composer: List[object]
        """

        self._composer = composer

    @property
    def author(self):
        """Gets the author of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The author of this NationalAnthem.
        :rtype: List[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this NationalAnthem.

        Description not available  # noqa: E501

        :param author: The author of this NationalAnthem.
        :type author: List[object]
        """

        self._author = author

    @property
    def runtime(self):
        """Gets the runtime of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The runtime of this NationalAnthem.
        :rtype: List[object]
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this NationalAnthem.

        Description not available  # noqa: E501

        :param runtime: The runtime of this NationalAnthem.
        :type runtime: List[object]
        """

        self._runtime = runtime

    @property
    def production_company(self):
        """Gets the production_company of this NationalAnthem.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :return: The production_company of this NationalAnthem.
        :rtype: List[object]
        """
        return self._production_company

    @production_company.setter
    def production_company(self, production_company):
        """Sets the production_company of this NationalAnthem.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :param production_company: The production_company of this NationalAnthem.
        :type production_company: List[object]
        """

        self._production_company = production_company

    @property
    def label(self):
        """Gets the label of this NationalAnthem.

        short description of the resource  # noqa: E501

        :return: The label of this NationalAnthem.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this NationalAnthem.

        short description of the resource  # noqa: E501

        :param label: The label of this NationalAnthem.
        :type label: List[str]
        """

        self._label = label

    @property
    def original_language(self):
        """Gets the original_language of this NationalAnthem.

        The original language of the work.  # noqa: E501

        :return: The original_language of this NationalAnthem.
        :rtype: List[object]
        """
        return self._original_language

    @original_language.setter
    def original_language(self, original_language):
        """Sets the original_language of this NationalAnthem.

        The original language of the work.  # noqa: E501

        :param original_language: The original_language of this NationalAnthem.
        :type original_language: List[object]
        """

        self._original_language = original_language

    @property
    def license(self):
        """Gets the license of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The license of this NationalAnthem.
        :rtype: List[object]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this NationalAnthem.

        Description not available  # noqa: E501

        :param license: The license of this NationalAnthem.
        :type license: List[object]
        """

        self._license = license

    @property
    def subject_term(self):
        """Gets the subject_term of this NationalAnthem.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :return: The subject_term of this NationalAnthem.
        :rtype: List[str]
        """
        return self._subject_term

    @subject_term.setter
    def subject_term(self, subject_term):
        """Sets the subject_term of this NationalAnthem.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :param subject_term: The subject_term of this NationalAnthem.
        :type subject_term: List[str]
        """

        self._subject_term = subject_term

    @property
    def musical_key(self):
        """Gets the musical_key of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The musical_key of this NationalAnthem.
        :rtype: List[str]
        """
        return self._musical_key

    @musical_key.setter
    def musical_key(self, musical_key):
        """Sets the musical_key of this NationalAnthem.

        Description not available  # noqa: E501

        :param musical_key: The musical_key of this NationalAnthem.
        :type musical_key: List[str]
        """

        self._musical_key = musical_key

    @property
    def original_title(self):
        """Gets the original_title of this NationalAnthem.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :return: The original_title of this NationalAnthem.
        :rtype: List[str]
        """
        return self._original_title

    @original_title.setter
    def original_title(self, original_title):
        """Sets the original_title of this NationalAnthem.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :param original_title: The original_title of this NationalAnthem.
        :type original_title: List[str]
        """

        self._original_title = original_title

    @property
    def producer(self):
        """Gets the producer of this NationalAnthem.

        The producer of the creative work.  # noqa: E501

        :return: The producer of this NationalAnthem.
        :rtype: List[object]
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this NationalAnthem.

        The producer of the creative work.  # noqa: E501

        :param producer: The producer of this NationalAnthem.
        :type producer: List[object]
        """

        self._producer = producer

    @property
    def starring(self):
        """Gets the starring of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The starring of this NationalAnthem.
        :rtype: List[object]
        """
        return self._starring

    @starring.setter
    def starring(self, starring):
        """Sets the starring of this NationalAnthem.

        Description not available  # noqa: E501

        :param starring: The starring of this NationalAnthem.
        :type starring: List[object]
        """

        self._starring = starring

    @property
    def completion_date(self):
        """Gets the completion_date of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The completion_date of this NationalAnthem.
        :rtype: List[str]
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this NationalAnthem.

        Description not available  # noqa: E501

        :param completion_date: The completion_date of this NationalAnthem.
        :type completion_date: List[str]
        """

        self._completion_date = completion_date

    @property
    def writer(self):
        """Gets the writer of this NationalAnthem.

        Description not available  # noqa: E501

        :return: The writer of this NationalAnthem.
        :rtype: List[object]
        """
        return self._writer

    @writer.setter
    def writer(self, writer):
        """Sets the writer of this NationalAnthem.

        Description not available  # noqa: E501

        :param writer: The writer of this NationalAnthem.
        :type writer: List[object]
        """

        self._writer = writer

    @property
    def music_type(self):
        """Gets the music_type of this NationalAnthem.

        Type is too general. We should be able to distinguish types of music from types of architecture  # noqa: E501

        :return: The music_type of this NationalAnthem.
        :rtype: List[object]
        """
        return self._music_type

    @music_type.setter
    def music_type(self, music_type):
        """Sets the music_type of this NationalAnthem.

        Type is too general. We should be able to distinguish types of music from types of architecture  # noqa: E501

        :param music_type: The music_type of this NationalAnthem.
        :type music_type: List[object]
        """

        self._music_type = music_type
