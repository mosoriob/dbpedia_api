# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TelevisionShow(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, previous_work=None, ending_theme=None, opening_theme=None, translator=None, co_producer=None, tv_com_id=None, alternative_title=None, description=None, subsequent_work=None, chief_editor=None, music_composer=None, type=None, number_of_seasons=None, main_character=None, id=None, based_on=None, presenter=None, release_date=None, composer=None, author=None, runtime=None, production_company=None, label=None, original_language=None, number_of_episodes=None, license=None, subject_term=None, creative_director=None, original_title=None, producer=None, starring=None, completion_date=None, story_editor=None, writer=None, co_executive_producer=None, show_judge=None):  # noqa: E501
        """TelevisionShow - a model defined in OpenAPI

        :param previous_work: The previous_work of this TelevisionShow.  # noqa: E501
        :type previous_work: List[object]
        :param ending_theme: The ending_theme of this TelevisionShow.  # noqa: E501
        :type ending_theme: List[object]
        :param opening_theme: The opening_theme of this TelevisionShow.  # noqa: E501
        :type opening_theme: List[object]
        :param translator: The translator of this TelevisionShow.  # noqa: E501
        :type translator: List[object]
        :param co_producer: The co_producer of this TelevisionShow.  # noqa: E501
        :type co_producer: List[object]
        :param tv_com_id: The tv_com_id of this TelevisionShow.  # noqa: E501
        :type tv_com_id: List[int]
        :param alternative_title: The alternative_title of this TelevisionShow.  # noqa: E501
        :type alternative_title: List[str]
        :param description: The description of this TelevisionShow.  # noqa: E501
        :type description: List[str]
        :param subsequent_work: The subsequent_work of this TelevisionShow.  # noqa: E501
        :type subsequent_work: List[object]
        :param chief_editor: The chief_editor of this TelevisionShow.  # noqa: E501
        :type chief_editor: List[object]
        :param music_composer: The music_composer of this TelevisionShow.  # noqa: E501
        :type music_composer: List[object]
        :param type: The type of this TelevisionShow.  # noqa: E501
        :type type: List[str]
        :param number_of_seasons: The number_of_seasons of this TelevisionShow.  # noqa: E501
        :type number_of_seasons: List[int]
        :param main_character: The main_character of this TelevisionShow.  # noqa: E501
        :type main_character: List[object]
        :param id: The id of this TelevisionShow.  # noqa: E501
        :type id: str
        :param based_on: The based_on of this TelevisionShow.  # noqa: E501
        :type based_on: List[object]
        :param presenter: The presenter of this TelevisionShow.  # noqa: E501
        :type presenter: List[object]
        :param release_date: The release_date of this TelevisionShow.  # noqa: E501
        :type release_date: List[str]
        :param composer: The composer of this TelevisionShow.  # noqa: E501
        :type composer: List[object]
        :param author: The author of this TelevisionShow.  # noqa: E501
        :type author: List[object]
        :param runtime: The runtime of this TelevisionShow.  # noqa: E501
        :type runtime: List[object]
        :param production_company: The production_company of this TelevisionShow.  # noqa: E501
        :type production_company: List[object]
        :param label: The label of this TelevisionShow.  # noqa: E501
        :type label: List[str]
        :param original_language: The original_language of this TelevisionShow.  # noqa: E501
        :type original_language: List[object]
        :param number_of_episodes: The number_of_episodes of this TelevisionShow.  # noqa: E501
        :type number_of_episodes: List[int]
        :param license: The license of this TelevisionShow.  # noqa: E501
        :type license: List[object]
        :param subject_term: The subject_term of this TelevisionShow.  # noqa: E501
        :type subject_term: List[str]
        :param creative_director: The creative_director of this TelevisionShow.  # noqa: E501
        :type creative_director: List[object]
        :param original_title: The original_title of this TelevisionShow.  # noqa: E501
        :type original_title: List[str]
        :param producer: The producer of this TelevisionShow.  # noqa: E501
        :type producer: List[object]
        :param starring: The starring of this TelevisionShow.  # noqa: E501
        :type starring: List[object]
        :param completion_date: The completion_date of this TelevisionShow.  # noqa: E501
        :type completion_date: List[str]
        :param story_editor: The story_editor of this TelevisionShow.  # noqa: E501
        :type story_editor: List[object]
        :param writer: The writer of this TelevisionShow.  # noqa: E501
        :type writer: List[object]
        :param co_executive_producer: The co_executive_producer of this TelevisionShow.  # noqa: E501
        :type co_executive_producer: List[object]
        :param show_judge: The show_judge of this TelevisionShow.  # noqa: E501
        :type show_judge: List[object]
        """


        self.openapi_types = {
            'previous_work': List[object],
            'ending_theme': List[object],
            'opening_theme': List[object],
            'translator': List[object],
            'co_producer': List[object],
            'tv_com_id': List[int],
            'alternative_title': List[str],
            'description': List[str],
            'subsequent_work': List[object],
            'chief_editor': List[object],
            'music_composer': List[object],
            'type': List[str],
            'number_of_seasons': List[int],
            'main_character': List[object],
            'id': str,
            'based_on': List[object],
            'presenter': List[object],
            'release_date': List[str],
            'composer': List[object],
            'author': List[object],
            'runtime': List[object],
            'production_company': List[object],
            'label': List[str],
            'original_language': List[object],
            'number_of_episodes': List[int],
            'license': List[object],
            'subject_term': List[str],
            'creative_director': List[object],
            'original_title': List[str],
            'producer': List[object],
            'starring': List[object],
            'completion_date': List[str],
            'story_editor': List[object],
            'writer': List[object],
            'co_executive_producer': List[object],
            'show_judge': List[object]
        }

        self.attribute_map = {
            'previous_work': 'previousWork',
            'ending_theme': 'endingTheme',
            'opening_theme': 'openingTheme',
            'translator': 'translator',
            'co_producer': 'coProducer',
            'tv_com_id': 'tvComId',
            'alternative_title': 'alternativeTitle',
            'description': 'description',
            'subsequent_work': 'subsequentWork',
            'chief_editor': 'chiefEditor',
            'music_composer': 'musicComposer',
            'type': 'type',
            'number_of_seasons': 'numberOfSeasons',
            'main_character': 'mainCharacter',
            'id': 'id',
            'based_on': 'basedOn',
            'presenter': 'presenter',
            'release_date': 'releaseDate',
            'composer': 'composer',
            'author': 'author',
            'runtime': 'runtime',
            'production_company': 'productionCompany',
            'label': 'label',
            'original_language': 'originalLanguage',
            'number_of_episodes': 'numberOfEpisodes',
            'license': 'license',
            'subject_term': 'subjectTerm',
            'creative_director': 'creativeDirector',
            'original_title': 'originalTitle',
            'producer': 'producer',
            'starring': 'starring',
            'completion_date': 'completionDate',
            'story_editor': 'storyEditor',
            'writer': 'writer',
            'co_executive_producer': 'coExecutiveProducer',
            'show_judge': 'showJudge'
        }

        self._previous_work = previous_work
        self._ending_theme = ending_theme
        self._opening_theme = opening_theme
        self._translator = translator
        self._co_producer = co_producer
        self._tv_com_id = tv_com_id
        self._alternative_title = alternative_title
        self._description = description
        self._subsequent_work = subsequent_work
        self._chief_editor = chief_editor
        self._music_composer = music_composer
        self._type = type
        self._number_of_seasons = number_of_seasons
        self._main_character = main_character
        self._id = id
        self._based_on = based_on
        self._presenter = presenter
        self._release_date = release_date
        self._composer = composer
        self._author = author
        self._runtime = runtime
        self._production_company = production_company
        self._label = label
        self._original_language = original_language
        self._number_of_episodes = number_of_episodes
        self._license = license
        self._subject_term = subject_term
        self._creative_director = creative_director
        self._original_title = original_title
        self._producer = producer
        self._starring = starring
        self._completion_date = completion_date
        self._story_editor = story_editor
        self._writer = writer
        self._co_executive_producer = co_executive_producer
        self._show_judge = show_judge

    @classmethod
    def from_dict(cls, dikt) -> 'TelevisionShow':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TelevisionShow of this TelevisionShow.  # noqa: E501
        :rtype: TelevisionShow
        """
        return util.deserialize_model(dikt, cls)

    @property
    def previous_work(self):
        """Gets the previous_work of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The previous_work of this TelevisionShow.
        :rtype: List[object]
        """
        return self._previous_work

    @previous_work.setter
    def previous_work(self, previous_work):
        """Sets the previous_work of this TelevisionShow.

        Description not available  # noqa: E501

        :param previous_work: The previous_work of this TelevisionShow.
        :type previous_work: List[object]
        """

        self._previous_work = previous_work

    @property
    def ending_theme(self):
        """Gets the ending_theme of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The ending_theme of this TelevisionShow.
        :rtype: List[object]
        """
        return self._ending_theme

    @ending_theme.setter
    def ending_theme(self, ending_theme):
        """Sets the ending_theme of this TelevisionShow.

        Description not available  # noqa: E501

        :param ending_theme: The ending_theme of this TelevisionShow.
        :type ending_theme: List[object]
        """

        self._ending_theme = ending_theme

    @property
    def opening_theme(self):
        """Gets the opening_theme of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The opening_theme of this TelevisionShow.
        :rtype: List[object]
        """
        return self._opening_theme

    @opening_theme.setter
    def opening_theme(self, opening_theme):
        """Sets the opening_theme of this TelevisionShow.

        Description not available  # noqa: E501

        :param opening_theme: The opening_theme of this TelevisionShow.
        :type opening_theme: List[object]
        """

        self._opening_theme = opening_theme

    @property
    def translator(self):
        """Gets the translator of this TelevisionShow.

        Translator(s), if original not in English  # noqa: E501

        :return: The translator of this TelevisionShow.
        :rtype: List[object]
        """
        return self._translator

    @translator.setter
    def translator(self, translator):
        """Sets the translator of this TelevisionShow.

        Translator(s), if original not in English  # noqa: E501

        :param translator: The translator of this TelevisionShow.
        :type translator: List[object]
        """

        self._translator = translator

    @property
    def co_producer(self):
        """Gets the co_producer of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The co_producer of this TelevisionShow.
        :rtype: List[object]
        """
        return self._co_producer

    @co_producer.setter
    def co_producer(self, co_producer):
        """Sets the co_producer of this TelevisionShow.

        Description not available  # noqa: E501

        :param co_producer: The co_producer of this TelevisionShow.
        :type co_producer: List[object]
        """

        self._co_producer = co_producer

    @property
    def tv_com_id(self):
        """Gets the tv_com_id of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The tv_com_id of this TelevisionShow.
        :rtype: List[int]
        """
        return self._tv_com_id

    @tv_com_id.setter
    def tv_com_id(self, tv_com_id):
        """Sets the tv_com_id of this TelevisionShow.

        Description not available  # noqa: E501

        :param tv_com_id: The tv_com_id of this TelevisionShow.
        :type tv_com_id: List[int]
        """

        self._tv_com_id = tv_com_id

    @property
    def alternative_title(self):
        """Gets the alternative_title of this TelevisionShow.

        The alternative title attributed to a work  # noqa: E501

        :return: The alternative_title of this TelevisionShow.
        :rtype: List[str]
        """
        return self._alternative_title

    @alternative_title.setter
    def alternative_title(self, alternative_title):
        """Sets the alternative_title of this TelevisionShow.

        The alternative title attributed to a work  # noqa: E501

        :param alternative_title: The alternative_title of this TelevisionShow.
        :type alternative_title: List[str]
        """

        self._alternative_title = alternative_title

    @property
    def description(self):
        """Gets the description of this TelevisionShow.

        small description  # noqa: E501

        :return: The description of this TelevisionShow.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TelevisionShow.

        small description  # noqa: E501

        :param description: The description of this TelevisionShow.
        :type description: List[str]
        """

        self._description = description

    @property
    def subsequent_work(self):
        """Gets the subsequent_work of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The subsequent_work of this TelevisionShow.
        :rtype: List[object]
        """
        return self._subsequent_work

    @subsequent_work.setter
    def subsequent_work(self, subsequent_work):
        """Sets the subsequent_work of this TelevisionShow.

        Description not available  # noqa: E501

        :param subsequent_work: The subsequent_work of this TelevisionShow.
        :type subsequent_work: List[object]
        """

        self._subsequent_work = subsequent_work

    @property
    def chief_editor(self):
        """Gets the chief_editor of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The chief_editor of this TelevisionShow.
        :rtype: List[object]
        """
        return self._chief_editor

    @chief_editor.setter
    def chief_editor(self, chief_editor):
        """Sets the chief_editor of this TelevisionShow.

        Description not available  # noqa: E501

        :param chief_editor: The chief_editor of this TelevisionShow.
        :type chief_editor: List[object]
        """

        self._chief_editor = chief_editor

    @property
    def music_composer(self):
        """Gets the music_composer of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The music_composer of this TelevisionShow.
        :rtype: List[object]
        """
        return self._music_composer

    @music_composer.setter
    def music_composer(self, music_composer):
        """Sets the music_composer of this TelevisionShow.

        Description not available  # noqa: E501

        :param music_composer: The music_composer of this TelevisionShow.
        :type music_composer: List[object]
        """

        self._music_composer = music_composer

    @property
    def type(self):
        """Gets the type of this TelevisionShow.

        type of the resource  # noqa: E501

        :return: The type of this TelevisionShow.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TelevisionShow.

        type of the resource  # noqa: E501

        :param type: The type of this TelevisionShow.
        :type type: List[str]
        """

        self._type = type

    @property
    def number_of_seasons(self):
        """Gets the number_of_seasons of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The number_of_seasons of this TelevisionShow.
        :rtype: List[int]
        """
        return self._number_of_seasons

    @number_of_seasons.setter
    def number_of_seasons(self, number_of_seasons):
        """Sets the number_of_seasons of this TelevisionShow.

        Description not available  # noqa: E501

        :param number_of_seasons: The number_of_seasons of this TelevisionShow.
        :type number_of_seasons: List[int]
        """

        self._number_of_seasons = number_of_seasons

    @property
    def main_character(self):
        """Gets the main_character of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The main_character of this TelevisionShow.
        :rtype: List[object]
        """
        return self._main_character

    @main_character.setter
    def main_character(self, main_character):
        """Sets the main_character of this TelevisionShow.

        Description not available  # noqa: E501

        :param main_character: The main_character of this TelevisionShow.
        :type main_character: List[object]
        """

        self._main_character = main_character

    @property
    def id(self):
        """Gets the id of this TelevisionShow.

        identifier  # noqa: E501

        :return: The id of this TelevisionShow.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TelevisionShow.

        identifier  # noqa: E501

        :param id: The id of this TelevisionShow.
        :type id: str
        """

        self._id = id

    @property
    def based_on(self):
        """Gets the based_on of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The based_on of this TelevisionShow.
        :rtype: List[object]
        """
        return self._based_on

    @based_on.setter
    def based_on(self, based_on):
        """Sets the based_on of this TelevisionShow.

        Description not available  # noqa: E501

        :param based_on: The based_on of this TelevisionShow.
        :type based_on: List[object]
        """

        self._based_on = based_on

    @property
    def presenter(self):
        """Gets the presenter of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The presenter of this TelevisionShow.
        :rtype: List[object]
        """
        return self._presenter

    @presenter.setter
    def presenter(self, presenter):
        """Sets the presenter of this TelevisionShow.

        Description not available  # noqa: E501

        :param presenter: The presenter of this TelevisionShow.
        :type presenter: List[object]
        """

        self._presenter = presenter

    @property
    def release_date(self):
        """Gets the release_date of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The release_date of this TelevisionShow.
        :rtype: List[str]
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this TelevisionShow.

        Description not available  # noqa: E501

        :param release_date: The release_date of this TelevisionShow.
        :type release_date: List[str]
        """

        self._release_date = release_date

    @property
    def composer(self):
        """Gets the composer of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The composer of this TelevisionShow.
        :rtype: List[object]
        """
        return self._composer

    @composer.setter
    def composer(self, composer):
        """Sets the composer of this TelevisionShow.

        Description not available  # noqa: E501

        :param composer: The composer of this TelevisionShow.
        :type composer: List[object]
        """

        self._composer = composer

    @property
    def author(self):
        """Gets the author of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The author of this TelevisionShow.
        :rtype: List[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this TelevisionShow.

        Description not available  # noqa: E501

        :param author: The author of this TelevisionShow.
        :type author: List[object]
        """

        self._author = author

    @property
    def runtime(self):
        """Gets the runtime of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The runtime of this TelevisionShow.
        :rtype: List[object]
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this TelevisionShow.

        Description not available  # noqa: E501

        :param runtime: The runtime of this TelevisionShow.
        :type runtime: List[object]
        """

        self._runtime = runtime

    @property
    def production_company(self):
        """Gets the production_company of this TelevisionShow.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :return: The production_company of this TelevisionShow.
        :rtype: List[object]
        """
        return self._production_company

    @production_company.setter
    def production_company(self, production_company):
        """Sets the production_company of this TelevisionShow.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :param production_company: The production_company of this TelevisionShow.
        :type production_company: List[object]
        """

        self._production_company = production_company

    @property
    def label(self):
        """Gets the label of this TelevisionShow.

        short description of the resource  # noqa: E501

        :return: The label of this TelevisionShow.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TelevisionShow.

        short description of the resource  # noqa: E501

        :param label: The label of this TelevisionShow.
        :type label: List[str]
        """

        self._label = label

    @property
    def original_language(self):
        """Gets the original_language of this TelevisionShow.

        The original language of the work.  # noqa: E501

        :return: The original_language of this TelevisionShow.
        :rtype: List[object]
        """
        return self._original_language

    @original_language.setter
    def original_language(self, original_language):
        """Sets the original_language of this TelevisionShow.

        The original language of the work.  # noqa: E501

        :param original_language: The original_language of this TelevisionShow.
        :type original_language: List[object]
        """

        self._original_language = original_language

    @property
    def number_of_episodes(self):
        """Gets the number_of_episodes of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The number_of_episodes of this TelevisionShow.
        :rtype: List[int]
        """
        return self._number_of_episodes

    @number_of_episodes.setter
    def number_of_episodes(self, number_of_episodes):
        """Sets the number_of_episodes of this TelevisionShow.

        Description not available  # noqa: E501

        :param number_of_episodes: The number_of_episodes of this TelevisionShow.
        :type number_of_episodes: List[int]
        """

        self._number_of_episodes = number_of_episodes

    @property
    def license(self):
        """Gets the license of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The license of this TelevisionShow.
        :rtype: List[object]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this TelevisionShow.

        Description not available  # noqa: E501

        :param license: The license of this TelevisionShow.
        :type license: List[object]
        """

        self._license = license

    @property
    def subject_term(self):
        """Gets the subject_term of this TelevisionShow.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :return: The subject_term of this TelevisionShow.
        :rtype: List[str]
        """
        return self._subject_term

    @subject_term.setter
    def subject_term(self, subject_term):
        """Sets the subject_term of this TelevisionShow.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :param subject_term: The subject_term of this TelevisionShow.
        :type subject_term: List[str]
        """

        self._subject_term = subject_term

    @property
    def creative_director(self):
        """Gets the creative_director of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The creative_director of this TelevisionShow.
        :rtype: List[object]
        """
        return self._creative_director

    @creative_director.setter
    def creative_director(self, creative_director):
        """Sets the creative_director of this TelevisionShow.

        Description not available  # noqa: E501

        :param creative_director: The creative_director of this TelevisionShow.
        :type creative_director: List[object]
        """

        self._creative_director = creative_director

    @property
    def original_title(self):
        """Gets the original_title of this TelevisionShow.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :return: The original_title of this TelevisionShow.
        :rtype: List[str]
        """
        return self._original_title

    @original_title.setter
    def original_title(self, original_title):
        """Sets the original_title of this TelevisionShow.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :param original_title: The original_title of this TelevisionShow.
        :type original_title: List[str]
        """

        self._original_title = original_title

    @property
    def producer(self):
        """Gets the producer of this TelevisionShow.

        The producer of the creative work.  # noqa: E501

        :return: The producer of this TelevisionShow.
        :rtype: List[object]
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this TelevisionShow.

        The producer of the creative work.  # noqa: E501

        :param producer: The producer of this TelevisionShow.
        :type producer: List[object]
        """

        self._producer = producer

    @property
    def starring(self):
        """Gets the starring of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The starring of this TelevisionShow.
        :rtype: List[object]
        """
        return self._starring

    @starring.setter
    def starring(self, starring):
        """Sets the starring of this TelevisionShow.

        Description not available  # noqa: E501

        :param starring: The starring of this TelevisionShow.
        :type starring: List[object]
        """

        self._starring = starring

    @property
    def completion_date(self):
        """Gets the completion_date of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The completion_date of this TelevisionShow.
        :rtype: List[str]
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this TelevisionShow.

        Description not available  # noqa: E501

        :param completion_date: The completion_date of this TelevisionShow.
        :type completion_date: List[str]
        """

        self._completion_date = completion_date

    @property
    def story_editor(self):
        """Gets the story_editor of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The story_editor of this TelevisionShow.
        :rtype: List[object]
        """
        return self._story_editor

    @story_editor.setter
    def story_editor(self, story_editor):
        """Sets the story_editor of this TelevisionShow.

        Description not available  # noqa: E501

        :param story_editor: The story_editor of this TelevisionShow.
        :type story_editor: List[object]
        """

        self._story_editor = story_editor

    @property
    def writer(self):
        """Gets the writer of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The writer of this TelevisionShow.
        :rtype: List[object]
        """
        return self._writer

    @writer.setter
    def writer(self, writer):
        """Sets the writer of this TelevisionShow.

        Description not available  # noqa: E501

        :param writer: The writer of this TelevisionShow.
        :type writer: List[object]
        """

        self._writer = writer

    @property
    def co_executive_producer(self):
        """Gets the co_executive_producer of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The co_executive_producer of this TelevisionShow.
        :rtype: List[object]
        """
        return self._co_executive_producer

    @co_executive_producer.setter
    def co_executive_producer(self, co_executive_producer):
        """Sets the co_executive_producer of this TelevisionShow.

        Description not available  # noqa: E501

        :param co_executive_producer: The co_executive_producer of this TelevisionShow.
        :type co_executive_producer: List[object]
        """

        self._co_executive_producer = co_executive_producer

    @property
    def show_judge(self):
        """Gets the show_judge of this TelevisionShow.

        Description not available  # noqa: E501

        :return: The show_judge of this TelevisionShow.
        :rtype: List[object]
        """
        return self._show_judge

    @show_judge.setter
    def show_judge(self, show_judge):
        """Sets the show_judge of this TelevisionShow.

        Description not available  # noqa: E501

        :param show_judge: The show_judge of this TelevisionShow.
        :type show_judge: List[object]
        """

        self._show_judge = show_judge
