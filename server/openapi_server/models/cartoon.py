# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Cartoon(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, previous_work=None, translator=None, alternative_title=None, description=None, subsequent_work=None, chief_editor=None, music_composer=None, type=None, main_character=None, id=None, based_on=None, release_date=None, composer=None, author=None, runtime=None, production_company=None, label=None, original_language=None, license=None, subject_term=None, original_title=None, producer=None, starring=None, completion_date=None, writer=None, animator=None):  # noqa: E501
        """Cartoon - a model defined in OpenAPI

        :param previous_work: The previous_work of this Cartoon.  # noqa: E501
        :type previous_work: List[object]
        :param translator: The translator of this Cartoon.  # noqa: E501
        :type translator: List[object]
        :param alternative_title: The alternative_title of this Cartoon.  # noqa: E501
        :type alternative_title: List[str]
        :param description: The description of this Cartoon.  # noqa: E501
        :type description: List[str]
        :param subsequent_work: The subsequent_work of this Cartoon.  # noqa: E501
        :type subsequent_work: List[object]
        :param chief_editor: The chief_editor of this Cartoon.  # noqa: E501
        :type chief_editor: List[object]
        :param music_composer: The music_composer of this Cartoon.  # noqa: E501
        :type music_composer: List[object]
        :param type: The type of this Cartoon.  # noqa: E501
        :type type: List[str]
        :param main_character: The main_character of this Cartoon.  # noqa: E501
        :type main_character: List[object]
        :param id: The id of this Cartoon.  # noqa: E501
        :type id: str
        :param based_on: The based_on of this Cartoon.  # noqa: E501
        :type based_on: List[object]
        :param release_date: The release_date of this Cartoon.  # noqa: E501
        :type release_date: List[str]
        :param composer: The composer of this Cartoon.  # noqa: E501
        :type composer: List[object]
        :param author: The author of this Cartoon.  # noqa: E501
        :type author: List[object]
        :param runtime: The runtime of this Cartoon.  # noqa: E501
        :type runtime: List[object]
        :param production_company: The production_company of this Cartoon.  # noqa: E501
        :type production_company: List[object]
        :param label: The label of this Cartoon.  # noqa: E501
        :type label: List[str]
        :param original_language: The original_language of this Cartoon.  # noqa: E501
        :type original_language: List[object]
        :param license: The license of this Cartoon.  # noqa: E501
        :type license: List[object]
        :param subject_term: The subject_term of this Cartoon.  # noqa: E501
        :type subject_term: List[str]
        :param original_title: The original_title of this Cartoon.  # noqa: E501
        :type original_title: List[str]
        :param producer: The producer of this Cartoon.  # noqa: E501
        :type producer: List[object]
        :param starring: The starring of this Cartoon.  # noqa: E501
        :type starring: List[object]
        :param completion_date: The completion_date of this Cartoon.  # noqa: E501
        :type completion_date: List[str]
        :param writer: The writer of this Cartoon.  # noqa: E501
        :type writer: List[object]
        :param animator: The animator of this Cartoon.  # noqa: E501
        :type animator: List[object]
        """


        self.openapi_types = {
            'previous_work': List[object],
            'translator': List[object],
            'alternative_title': List[str],
            'description': List[str],
            'subsequent_work': List[object],
            'chief_editor': List[object],
            'music_composer': List[object],
            'type': List[str],
            'main_character': List[object],
            'id': str,
            'based_on': List[object],
            'release_date': List[str],
            'composer': List[object],
            'author': List[object],
            'runtime': List[object],
            'production_company': List[object],
            'label': List[str],
            'original_language': List[object],
            'license': List[object],
            'subject_term': List[str],
            'original_title': List[str],
            'producer': List[object],
            'starring': List[object],
            'completion_date': List[str],
            'writer': List[object],
            'animator': List[object]
        }

        self.attribute_map = {
            'previous_work': 'previousWork',
            'translator': 'translator',
            'alternative_title': 'alternativeTitle',
            'description': 'description',
            'subsequent_work': 'subsequentWork',
            'chief_editor': 'chiefEditor',
            'music_composer': 'musicComposer',
            'type': 'type',
            'main_character': 'mainCharacter',
            'id': 'id',
            'based_on': 'basedOn',
            'release_date': 'releaseDate',
            'composer': 'composer',
            'author': 'author',
            'runtime': 'runtime',
            'production_company': 'productionCompany',
            'label': 'label',
            'original_language': 'originalLanguage',
            'license': 'license',
            'subject_term': 'subjectTerm',
            'original_title': 'originalTitle',
            'producer': 'producer',
            'starring': 'starring',
            'completion_date': 'completionDate',
            'writer': 'writer',
            'animator': 'animator'
        }

        self._previous_work = previous_work
        self._translator = translator
        self._alternative_title = alternative_title
        self._description = description
        self._subsequent_work = subsequent_work
        self._chief_editor = chief_editor
        self._music_composer = music_composer
        self._type = type
        self._main_character = main_character
        self._id = id
        self._based_on = based_on
        self._release_date = release_date
        self._composer = composer
        self._author = author
        self._runtime = runtime
        self._production_company = production_company
        self._label = label
        self._original_language = original_language
        self._license = license
        self._subject_term = subject_term
        self._original_title = original_title
        self._producer = producer
        self._starring = starring
        self._completion_date = completion_date
        self._writer = writer
        self._animator = animator

    @classmethod
    def from_dict(cls, dikt) -> 'Cartoon':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Cartoon of this Cartoon.  # noqa: E501
        :rtype: Cartoon
        """
        return util.deserialize_model(dikt, cls)

    @property
    def previous_work(self):
        """Gets the previous_work of this Cartoon.

        Description not available  # noqa: E501

        :return: The previous_work of this Cartoon.
        :rtype: List[object]
        """
        return self._previous_work

    @previous_work.setter
    def previous_work(self, previous_work):
        """Sets the previous_work of this Cartoon.

        Description not available  # noqa: E501

        :param previous_work: The previous_work of this Cartoon.
        :type previous_work: List[object]
        """

        self._previous_work = previous_work

    @property
    def translator(self):
        """Gets the translator of this Cartoon.

        Translator(s), if original not in English  # noqa: E501

        :return: The translator of this Cartoon.
        :rtype: List[object]
        """
        return self._translator

    @translator.setter
    def translator(self, translator):
        """Sets the translator of this Cartoon.

        Translator(s), if original not in English  # noqa: E501

        :param translator: The translator of this Cartoon.
        :type translator: List[object]
        """

        self._translator = translator

    @property
    def alternative_title(self):
        """Gets the alternative_title of this Cartoon.

        The alternative title attributed to a work  # noqa: E501

        :return: The alternative_title of this Cartoon.
        :rtype: List[str]
        """
        return self._alternative_title

    @alternative_title.setter
    def alternative_title(self, alternative_title):
        """Sets the alternative_title of this Cartoon.

        The alternative title attributed to a work  # noqa: E501

        :param alternative_title: The alternative_title of this Cartoon.
        :type alternative_title: List[str]
        """

        self._alternative_title = alternative_title

    @property
    def description(self):
        """Gets the description of this Cartoon.

        small description  # noqa: E501

        :return: The description of this Cartoon.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Cartoon.

        small description  # noqa: E501

        :param description: The description of this Cartoon.
        :type description: List[str]
        """

        self._description = description

    @property
    def subsequent_work(self):
        """Gets the subsequent_work of this Cartoon.

        Description not available  # noqa: E501

        :return: The subsequent_work of this Cartoon.
        :rtype: List[object]
        """
        return self._subsequent_work

    @subsequent_work.setter
    def subsequent_work(self, subsequent_work):
        """Sets the subsequent_work of this Cartoon.

        Description not available  # noqa: E501

        :param subsequent_work: The subsequent_work of this Cartoon.
        :type subsequent_work: List[object]
        """

        self._subsequent_work = subsequent_work

    @property
    def chief_editor(self):
        """Gets the chief_editor of this Cartoon.

        Description not available  # noqa: E501

        :return: The chief_editor of this Cartoon.
        :rtype: List[object]
        """
        return self._chief_editor

    @chief_editor.setter
    def chief_editor(self, chief_editor):
        """Sets the chief_editor of this Cartoon.

        Description not available  # noqa: E501

        :param chief_editor: The chief_editor of this Cartoon.
        :type chief_editor: List[object]
        """

        self._chief_editor = chief_editor

    @property
    def music_composer(self):
        """Gets the music_composer of this Cartoon.

        Description not available  # noqa: E501

        :return: The music_composer of this Cartoon.
        :rtype: List[object]
        """
        return self._music_composer

    @music_composer.setter
    def music_composer(self, music_composer):
        """Sets the music_composer of this Cartoon.

        Description not available  # noqa: E501

        :param music_composer: The music_composer of this Cartoon.
        :type music_composer: List[object]
        """

        self._music_composer = music_composer

    @property
    def type(self):
        """Gets the type of this Cartoon.

        type of the resource  # noqa: E501

        :return: The type of this Cartoon.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Cartoon.

        type of the resource  # noqa: E501

        :param type: The type of this Cartoon.
        :type type: List[str]
        """

        self._type = type

    @property
    def main_character(self):
        """Gets the main_character of this Cartoon.

        Description not available  # noqa: E501

        :return: The main_character of this Cartoon.
        :rtype: List[object]
        """
        return self._main_character

    @main_character.setter
    def main_character(self, main_character):
        """Sets the main_character of this Cartoon.

        Description not available  # noqa: E501

        :param main_character: The main_character of this Cartoon.
        :type main_character: List[object]
        """

        self._main_character = main_character

    @property
    def id(self):
        """Gets the id of this Cartoon.

        identifier  # noqa: E501

        :return: The id of this Cartoon.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Cartoon.

        identifier  # noqa: E501

        :param id: The id of this Cartoon.
        :type id: str
        """

        self._id = id

    @property
    def based_on(self):
        """Gets the based_on of this Cartoon.

        Description not available  # noqa: E501

        :return: The based_on of this Cartoon.
        :rtype: List[object]
        """
        return self._based_on

    @based_on.setter
    def based_on(self, based_on):
        """Sets the based_on of this Cartoon.

        Description not available  # noqa: E501

        :param based_on: The based_on of this Cartoon.
        :type based_on: List[object]
        """

        self._based_on = based_on

    @property
    def release_date(self):
        """Gets the release_date of this Cartoon.

        Description not available  # noqa: E501

        :return: The release_date of this Cartoon.
        :rtype: List[str]
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this Cartoon.

        Description not available  # noqa: E501

        :param release_date: The release_date of this Cartoon.
        :type release_date: List[str]
        """

        self._release_date = release_date

    @property
    def composer(self):
        """Gets the composer of this Cartoon.

        Description not available  # noqa: E501

        :return: The composer of this Cartoon.
        :rtype: List[object]
        """
        return self._composer

    @composer.setter
    def composer(self, composer):
        """Sets the composer of this Cartoon.

        Description not available  # noqa: E501

        :param composer: The composer of this Cartoon.
        :type composer: List[object]
        """

        self._composer = composer

    @property
    def author(self):
        """Gets the author of this Cartoon.

        Description not available  # noqa: E501

        :return: The author of this Cartoon.
        :rtype: List[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Cartoon.

        Description not available  # noqa: E501

        :param author: The author of this Cartoon.
        :type author: List[object]
        """

        self._author = author

    @property
    def runtime(self):
        """Gets the runtime of this Cartoon.

        Description not available  # noqa: E501

        :return: The runtime of this Cartoon.
        :rtype: List[object]
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this Cartoon.

        Description not available  # noqa: E501

        :param runtime: The runtime of this Cartoon.
        :type runtime: List[object]
        """

        self._runtime = runtime

    @property
    def production_company(self):
        """Gets the production_company of this Cartoon.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :return: The production_company of this Cartoon.
        :rtype: List[object]
        """
        return self._production_company

    @production_company.setter
    def production_company(self, production_company):
        """Sets the production_company of this Cartoon.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :param production_company: The production_company of this Cartoon.
        :type production_company: List[object]
        """

        self._production_company = production_company

    @property
    def label(self):
        """Gets the label of this Cartoon.

        short description of the resource  # noqa: E501

        :return: The label of this Cartoon.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Cartoon.

        short description of the resource  # noqa: E501

        :param label: The label of this Cartoon.
        :type label: List[str]
        """

        self._label = label

    @property
    def original_language(self):
        """Gets the original_language of this Cartoon.

        The original language of the work.  # noqa: E501

        :return: The original_language of this Cartoon.
        :rtype: List[object]
        """
        return self._original_language

    @original_language.setter
    def original_language(self, original_language):
        """Sets the original_language of this Cartoon.

        The original language of the work.  # noqa: E501

        :param original_language: The original_language of this Cartoon.
        :type original_language: List[object]
        """

        self._original_language = original_language

    @property
    def license(self):
        """Gets the license of this Cartoon.

        Description not available  # noqa: E501

        :return: The license of this Cartoon.
        :rtype: List[object]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Cartoon.

        Description not available  # noqa: E501

        :param license: The license of this Cartoon.
        :type license: List[object]
        """

        self._license = license

    @property
    def subject_term(self):
        """Gets the subject_term of this Cartoon.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :return: The subject_term of this Cartoon.
        :rtype: List[str]
        """
        return self._subject_term

    @subject_term.setter
    def subject_term(self, subject_term):
        """Sets the subject_term of this Cartoon.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :param subject_term: The subject_term of this Cartoon.
        :type subject_term: List[str]
        """

        self._subject_term = subject_term

    @property
    def original_title(self):
        """Gets the original_title of this Cartoon.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :return: The original_title of this Cartoon.
        :rtype: List[str]
        """
        return self._original_title

    @original_title.setter
    def original_title(self, original_title):
        """Sets the original_title of this Cartoon.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :param original_title: The original_title of this Cartoon.
        :type original_title: List[str]
        """

        self._original_title = original_title

    @property
    def producer(self):
        """Gets the producer of this Cartoon.

        The producer of the creative work.  # noqa: E501

        :return: The producer of this Cartoon.
        :rtype: List[object]
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this Cartoon.

        The producer of the creative work.  # noqa: E501

        :param producer: The producer of this Cartoon.
        :type producer: List[object]
        """

        self._producer = producer

    @property
    def starring(self):
        """Gets the starring of this Cartoon.

        Description not available  # noqa: E501

        :return: The starring of this Cartoon.
        :rtype: List[object]
        """
        return self._starring

    @starring.setter
    def starring(self, starring):
        """Sets the starring of this Cartoon.

        Description not available  # noqa: E501

        :param starring: The starring of this Cartoon.
        :type starring: List[object]
        """

        self._starring = starring

    @property
    def completion_date(self):
        """Gets the completion_date of this Cartoon.

        Description not available  # noqa: E501

        :return: The completion_date of this Cartoon.
        :rtype: List[str]
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this Cartoon.

        Description not available  # noqa: E501

        :param completion_date: The completion_date of this Cartoon.
        :type completion_date: List[str]
        """

        self._completion_date = completion_date

    @property
    def writer(self):
        """Gets the writer of this Cartoon.

        Description not available  # noqa: E501

        :return: The writer of this Cartoon.
        :rtype: List[object]
        """
        return self._writer

    @writer.setter
    def writer(self, writer):
        """Sets the writer of this Cartoon.

        Description not available  # noqa: E501

        :param writer: The writer of this Cartoon.
        :type writer: List[object]
        """

        self._writer = writer

    @property
    def animator(self):
        """Gets the animator of this Cartoon.

        Description not available  # noqa: E501

        :return: The animator of this Cartoon.
        :rtype: List[object]
        """
        return self._animator

    @animator.setter
    def animator(self, animator):
        """Sets the animator of this Cartoon.

        Description not available  # noqa: E501

        :param animator: The animator of this Cartoon.
        :type animator: List[object]
        """

        self._animator = animator
