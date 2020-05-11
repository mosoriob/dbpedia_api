# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Comic(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, previous_work=None, coden=None, translator=None, alternative_title=None, description=None, subsequent_work=None, chief_editor=None, music_composer=None, last_publication_date=None, type=None, lcc=None, lccn=None, main_character=None, id=None, literary_genre=None, based_on=None, first_publisher=None, first_publication_date=None, film_version=None, release_date=None, number_of_volumes=None, composer=None, author=None, preface_by=None, runtime=None, production_company=None, label=None, original_language=None, license=None, subject_term=None, original_title=None, circulation=None, oclc=None, producer=None, starring=None, completion_date=None, writer=None, magazine=None):  # noqa: E501
        """Comic - a model defined in OpenAPI

        :param previous_work: The previous_work of this Comic.  # noqa: E501
        :type previous_work: List[object]
        :param coden: The coden of this Comic.  # noqa: E501
        :type coden: List[str]
        :param translator: The translator of this Comic.  # noqa: E501
        :type translator: List[object]
        :param alternative_title: The alternative_title of this Comic.  # noqa: E501
        :type alternative_title: List[str]
        :param description: The description of this Comic.  # noqa: E501
        :type description: List[str]
        :param subsequent_work: The subsequent_work of this Comic.  # noqa: E501
        :type subsequent_work: List[object]
        :param chief_editor: The chief_editor of this Comic.  # noqa: E501
        :type chief_editor: List[object]
        :param music_composer: The music_composer of this Comic.  # noqa: E501
        :type music_composer: List[object]
        :param last_publication_date: The last_publication_date of this Comic.  # noqa: E501
        :type last_publication_date: List[str]
        :param type: The type of this Comic.  # noqa: E501
        :type type: List[str]
        :param lcc: The lcc of this Comic.  # noqa: E501
        :type lcc: List[str]
        :param lccn: The lccn of this Comic.  # noqa: E501
        :type lccn: List[str]
        :param main_character: The main_character of this Comic.  # noqa: E501
        :type main_character: List[object]
        :param id: The id of this Comic.  # noqa: E501
        :type id: str
        :param literary_genre: The literary_genre of this Comic.  # noqa: E501
        :type literary_genre: List[object]
        :param based_on: The based_on of this Comic.  # noqa: E501
        :type based_on: List[object]
        :param first_publisher: The first_publisher of this Comic.  # noqa: E501
        :type first_publisher: List[object]
        :param first_publication_date: The first_publication_date of this Comic.  # noqa: E501
        :type first_publication_date: List[str]
        :param film_version: The film_version of this Comic.  # noqa: E501
        :type film_version: List[object]
        :param release_date: The release_date of this Comic.  # noqa: E501
        :type release_date: List[str]
        :param number_of_volumes: The number_of_volumes of this Comic.  # noqa: E501
        :type number_of_volumes: List[int]
        :param composer: The composer of this Comic.  # noqa: E501
        :type composer: List[object]
        :param author: The author of this Comic.  # noqa: E501
        :type author: List[object]
        :param preface_by: The preface_by of this Comic.  # noqa: E501
        :type preface_by: List[object]
        :param runtime: The runtime of this Comic.  # noqa: E501
        :type runtime: List[object]
        :param production_company: The production_company of this Comic.  # noqa: E501
        :type production_company: List[object]
        :param label: The label of this Comic.  # noqa: E501
        :type label: List[str]
        :param original_language: The original_language of this Comic.  # noqa: E501
        :type original_language: List[object]
        :param license: The license of this Comic.  # noqa: E501
        :type license: List[object]
        :param subject_term: The subject_term of this Comic.  # noqa: E501
        :type subject_term: List[str]
        :param original_title: The original_title of this Comic.  # noqa: E501
        :type original_title: List[str]
        :param circulation: The circulation of this Comic.  # noqa: E501
        :type circulation: List[int]
        :param oclc: The oclc of this Comic.  # noqa: E501
        :type oclc: List[str]
        :param producer: The producer of this Comic.  # noqa: E501
        :type producer: List[object]
        :param starring: The starring of this Comic.  # noqa: E501
        :type starring: List[object]
        :param completion_date: The completion_date of this Comic.  # noqa: E501
        :type completion_date: List[str]
        :param writer: The writer of this Comic.  # noqa: E501
        :type writer: List[object]
        :param magazine: The magazine of this Comic.  # noqa: E501
        :type magazine: List[object]
        """


        self.openapi_types = {
            'previous_work': List[object],
            'coden': List[str],
            'translator': List[object],
            'alternative_title': List[str],
            'description': List[str],
            'subsequent_work': List[object],
            'chief_editor': List[object],
            'music_composer': List[object],
            'last_publication_date': List[str],
            'type': List[str],
            'lcc': List[str],
            'lccn': List[str],
            'main_character': List[object],
            'id': str,
            'literary_genre': List[object],
            'based_on': List[object],
            'first_publisher': List[object],
            'first_publication_date': List[str],
            'film_version': List[object],
            'release_date': List[str],
            'number_of_volumes': List[int],
            'composer': List[object],
            'author': List[object],
            'preface_by': List[object],
            'runtime': List[object],
            'production_company': List[object],
            'label': List[str],
            'original_language': List[object],
            'license': List[object],
            'subject_term': List[str],
            'original_title': List[str],
            'circulation': List[int],
            'oclc': List[str],
            'producer': List[object],
            'starring': List[object],
            'completion_date': List[str],
            'writer': List[object],
            'magazine': List[object]
        }

        self.attribute_map = {
            'previous_work': 'previousWork',
            'coden': 'coden',
            'translator': 'translator',
            'alternative_title': 'alternativeTitle',
            'description': 'description',
            'subsequent_work': 'subsequentWork',
            'chief_editor': 'chiefEditor',
            'music_composer': 'musicComposer',
            'last_publication_date': 'lastPublicationDate',
            'type': 'type',
            'lcc': 'lcc',
            'lccn': 'lccn',
            'main_character': 'mainCharacter',
            'id': 'id',
            'literary_genre': 'literaryGenre',
            'based_on': 'basedOn',
            'first_publisher': 'firstPublisher',
            'first_publication_date': 'firstPublicationDate',
            'film_version': 'filmVersion',
            'release_date': 'releaseDate',
            'number_of_volumes': 'numberOfVolumes',
            'composer': 'composer',
            'author': 'author',
            'preface_by': 'prefaceBy',
            'runtime': 'runtime',
            'production_company': 'productionCompany',
            'label': 'label',
            'original_language': 'originalLanguage',
            'license': 'license',
            'subject_term': 'subjectTerm',
            'original_title': 'originalTitle',
            'circulation': 'circulation',
            'oclc': 'oclc',
            'producer': 'producer',
            'starring': 'starring',
            'completion_date': 'completionDate',
            'writer': 'writer',
            'magazine': 'magazine'
        }

        self._previous_work = previous_work
        self._coden = coden
        self._translator = translator
        self._alternative_title = alternative_title
        self._description = description
        self._subsequent_work = subsequent_work
        self._chief_editor = chief_editor
        self._music_composer = music_composer
        self._last_publication_date = last_publication_date
        self._type = type
        self._lcc = lcc
        self._lccn = lccn
        self._main_character = main_character
        self._id = id
        self._literary_genre = literary_genre
        self._based_on = based_on
        self._first_publisher = first_publisher
        self._first_publication_date = first_publication_date
        self._film_version = film_version
        self._release_date = release_date
        self._number_of_volumes = number_of_volumes
        self._composer = composer
        self._author = author
        self._preface_by = preface_by
        self._runtime = runtime
        self._production_company = production_company
        self._label = label
        self._original_language = original_language
        self._license = license
        self._subject_term = subject_term
        self._original_title = original_title
        self._circulation = circulation
        self._oclc = oclc
        self._producer = producer
        self._starring = starring
        self._completion_date = completion_date
        self._writer = writer
        self._magazine = magazine

    @classmethod
    def from_dict(cls, dikt) -> 'Comic':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Comic of this Comic.  # noqa: E501
        :rtype: Comic
        """
        return util.deserialize_model(dikt, cls)

    @property
    def previous_work(self):
        """Gets the previous_work of this Comic.

        Description not available  # noqa: E501

        :return: The previous_work of this Comic.
        :rtype: List[object]
        """
        return self._previous_work

    @previous_work.setter
    def previous_work(self, previous_work):
        """Sets the previous_work of this Comic.

        Description not available  # noqa: E501

        :param previous_work: The previous_work of this Comic.
        :type previous_work: List[object]
        """

        self._previous_work = previous_work

    @property
    def coden(self):
        """Gets the coden of this Comic.

        CODEN is a six character, alphanumeric bibliographic code, that provides concise, unique and unambiguous identification of the titles of serials and non-serial publications from all subject areas.  # noqa: E501

        :return: The coden of this Comic.
        :rtype: List[str]
        """
        return self._coden

    @coden.setter
    def coden(self, coden):
        """Sets the coden of this Comic.

        CODEN is a six character, alphanumeric bibliographic code, that provides concise, unique and unambiguous identification of the titles of serials and non-serial publications from all subject areas.  # noqa: E501

        :param coden: The coden of this Comic.
        :type coden: List[str]
        """

        self._coden = coden

    @property
    def translator(self):
        """Gets the translator of this Comic.

        Translator(s), if original not in English  # noqa: E501

        :return: The translator of this Comic.
        :rtype: List[object]
        """
        return self._translator

    @translator.setter
    def translator(self, translator):
        """Sets the translator of this Comic.

        Translator(s), if original not in English  # noqa: E501

        :param translator: The translator of this Comic.
        :type translator: List[object]
        """

        self._translator = translator

    @property
    def alternative_title(self):
        """Gets the alternative_title of this Comic.

        The alternative title attributed to a work  # noqa: E501

        :return: The alternative_title of this Comic.
        :rtype: List[str]
        """
        return self._alternative_title

    @alternative_title.setter
    def alternative_title(self, alternative_title):
        """Sets the alternative_title of this Comic.

        The alternative title attributed to a work  # noqa: E501

        :param alternative_title: The alternative_title of this Comic.
        :type alternative_title: List[str]
        """

        self._alternative_title = alternative_title

    @property
    def description(self):
        """Gets the description of this Comic.

        small description  # noqa: E501

        :return: The description of this Comic.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Comic.

        small description  # noqa: E501

        :param description: The description of this Comic.
        :type description: List[str]
        """

        self._description = description

    @property
    def subsequent_work(self):
        """Gets the subsequent_work of this Comic.

        Description not available  # noqa: E501

        :return: The subsequent_work of this Comic.
        :rtype: List[object]
        """
        return self._subsequent_work

    @subsequent_work.setter
    def subsequent_work(self, subsequent_work):
        """Sets the subsequent_work of this Comic.

        Description not available  # noqa: E501

        :param subsequent_work: The subsequent_work of this Comic.
        :type subsequent_work: List[object]
        """

        self._subsequent_work = subsequent_work

    @property
    def chief_editor(self):
        """Gets the chief_editor of this Comic.

        Description not available  # noqa: E501

        :return: The chief_editor of this Comic.
        :rtype: List[object]
        """
        return self._chief_editor

    @chief_editor.setter
    def chief_editor(self, chief_editor):
        """Sets the chief_editor of this Comic.

        Description not available  # noqa: E501

        :param chief_editor: The chief_editor of this Comic.
        :type chief_editor: List[object]
        """

        self._chief_editor = chief_editor

    @property
    def music_composer(self):
        """Gets the music_composer of this Comic.

        Description not available  # noqa: E501

        :return: The music_composer of this Comic.
        :rtype: List[object]
        """
        return self._music_composer

    @music_composer.setter
    def music_composer(self, music_composer):
        """Sets the music_composer of this Comic.

        Description not available  # noqa: E501

        :param music_composer: The music_composer of this Comic.
        :type music_composer: List[object]
        """

        self._music_composer = music_composer

    @property
    def last_publication_date(self):
        """Gets the last_publication_date of this Comic.

        Date of the last publication.  # noqa: E501

        :return: The last_publication_date of this Comic.
        :rtype: List[str]
        """
        return self._last_publication_date

    @last_publication_date.setter
    def last_publication_date(self, last_publication_date):
        """Sets the last_publication_date of this Comic.

        Date of the last publication.  # noqa: E501

        :param last_publication_date: The last_publication_date of this Comic.
        :type last_publication_date: List[str]
        """

        self._last_publication_date = last_publication_date

    @property
    def type(self):
        """Gets the type of this Comic.

        type of the resource  # noqa: E501

        :return: The type of this Comic.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Comic.

        type of the resource  # noqa: E501

        :param type: The type of this Comic.
        :type type: List[str]
        """

        self._type = type

    @property
    def lcc(self):
        """Gets the lcc of this Comic.

        The Library of Congress Classification (LCC) is a system of library classification developed by the Library of Congress.  # noqa: E501

        :return: The lcc of this Comic.
        :rtype: List[str]
        """
        return self._lcc

    @lcc.setter
    def lcc(self, lcc):
        """Sets the lcc of this Comic.

        The Library of Congress Classification (LCC) is a system of library classification developed by the Library of Congress.  # noqa: E501

        :param lcc: The lcc of this Comic.
        :type lcc: List[str]
        """

        self._lcc = lcc

    @property
    def lccn(self):
        """Gets the lccn of this Comic.

        The Library of Congress Control Number or LCCN is a serially based system of numbering cataloging records in the Library of Congress in the United States. It has nothing to do with the contents of any book, and should not be confused with Library of Congress Classification.  # noqa: E501

        :return: The lccn of this Comic.
        :rtype: List[str]
        """
        return self._lccn

    @lccn.setter
    def lccn(self, lccn):
        """Sets the lccn of this Comic.

        The Library of Congress Control Number or LCCN is a serially based system of numbering cataloging records in the Library of Congress in the United States. It has nothing to do with the contents of any book, and should not be confused with Library of Congress Classification.  # noqa: E501

        :param lccn: The lccn of this Comic.
        :type lccn: List[str]
        """

        self._lccn = lccn

    @property
    def main_character(self):
        """Gets the main_character of this Comic.

        Description not available  # noqa: E501

        :return: The main_character of this Comic.
        :rtype: List[object]
        """
        return self._main_character

    @main_character.setter
    def main_character(self, main_character):
        """Sets the main_character of this Comic.

        Description not available  # noqa: E501

        :param main_character: The main_character of this Comic.
        :type main_character: List[object]
        """

        self._main_character = main_character

    @property
    def id(self):
        """Gets the id of this Comic.

        identifier  # noqa: E501

        :return: The id of this Comic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comic.

        identifier  # noqa: E501

        :param id: The id of this Comic.
        :type id: str
        """

        self._id = id

    @property
    def literary_genre(self):
        """Gets the literary_genre of this Comic.

        A literary genre is a category of literary composition. Genres may be determined by literary technique, tone, content, or even (as in the case of fiction) length.  # noqa: E501

        :return: The literary_genre of this Comic.
        :rtype: List[object]
        """
        return self._literary_genre

    @literary_genre.setter
    def literary_genre(self, literary_genre):
        """Sets the literary_genre of this Comic.

        A literary genre is a category of literary composition. Genres may be determined by literary technique, tone, content, or even (as in the case of fiction) length.  # noqa: E501

        :param literary_genre: The literary_genre of this Comic.
        :type literary_genre: List[object]
        """

        self._literary_genre = literary_genre

    @property
    def based_on(self):
        """Gets the based_on of this Comic.

        Description not available  # noqa: E501

        :return: The based_on of this Comic.
        :rtype: List[object]
        """
        return self._based_on

    @based_on.setter
    def based_on(self, based_on):
        """Sets the based_on of this Comic.

        Description not available  # noqa: E501

        :param based_on: The based_on of this Comic.
        :type based_on: List[object]
        """

        self._based_on = based_on

    @property
    def first_publisher(self):
        """Gets the first_publisher of this Comic.

        Description not available  # noqa: E501

        :return: The first_publisher of this Comic.
        :rtype: List[object]
        """
        return self._first_publisher

    @first_publisher.setter
    def first_publisher(self, first_publisher):
        """Sets the first_publisher of this Comic.

        Description not available  # noqa: E501

        :param first_publisher: The first_publisher of this Comic.
        :type first_publisher: List[object]
        """

        self._first_publisher = first_publisher

    @property
    def first_publication_date(self):
        """Gets the first_publication_date of this Comic.

        Date of the first publication.  # noqa: E501

        :return: The first_publication_date of this Comic.
        :rtype: List[str]
        """
        return self._first_publication_date

    @first_publication_date.setter
    def first_publication_date(self, first_publication_date):
        """Sets the first_publication_date of this Comic.

        Date of the first publication.  # noqa: E501

        :param first_publication_date: The first_publication_date of this Comic.
        :type first_publication_date: List[str]
        """

        self._first_publication_date = first_publication_date

    @property
    def film_version(self):
        """Gets the film_version of this Comic.

        Description not available  # noqa: E501

        :return: The film_version of this Comic.
        :rtype: List[object]
        """
        return self._film_version

    @film_version.setter
    def film_version(self, film_version):
        """Sets the film_version of this Comic.

        Description not available  # noqa: E501

        :param film_version: The film_version of this Comic.
        :type film_version: List[object]
        """

        self._film_version = film_version

    @property
    def release_date(self):
        """Gets the release_date of this Comic.

        Description not available  # noqa: E501

        :return: The release_date of this Comic.
        :rtype: List[str]
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this Comic.

        Description not available  # noqa: E501

        :param release_date: The release_date of this Comic.
        :type release_date: List[str]
        """

        self._release_date = release_date

    @property
    def number_of_volumes(self):
        """Gets the number_of_volumes of this Comic.

        Description not available  # noqa: E501

        :return: The number_of_volumes of this Comic.
        :rtype: List[int]
        """
        return self._number_of_volumes

    @number_of_volumes.setter
    def number_of_volumes(self, number_of_volumes):
        """Sets the number_of_volumes of this Comic.

        Description not available  # noqa: E501

        :param number_of_volumes: The number_of_volumes of this Comic.
        :type number_of_volumes: List[int]
        """

        self._number_of_volumes = number_of_volumes

    @property
    def composer(self):
        """Gets the composer of this Comic.

        Description not available  # noqa: E501

        :return: The composer of this Comic.
        :rtype: List[object]
        """
        return self._composer

    @composer.setter
    def composer(self, composer):
        """Sets the composer of this Comic.

        Description not available  # noqa: E501

        :param composer: The composer of this Comic.
        :type composer: List[object]
        """

        self._composer = composer

    @property
    def author(self):
        """Gets the author of this Comic.

        Description not available  # noqa: E501

        :return: The author of this Comic.
        :rtype: List[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Comic.

        Description not available  # noqa: E501

        :param author: The author of this Comic.
        :type author: List[object]
        """

        self._author = author

    @property
    def preface_by(self):
        """Gets the preface_by of this Comic.

        Description not available  # noqa: E501

        :return: The preface_by of this Comic.
        :rtype: List[object]
        """
        return self._preface_by

    @preface_by.setter
    def preface_by(self, preface_by):
        """Sets the preface_by of this Comic.

        Description not available  # noqa: E501

        :param preface_by: The preface_by of this Comic.
        :type preface_by: List[object]
        """

        self._preface_by = preface_by

    @property
    def runtime(self):
        """Gets the runtime of this Comic.

        Description not available  # noqa: E501

        :return: The runtime of this Comic.
        :rtype: List[object]
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this Comic.

        Description not available  # noqa: E501

        :param runtime: The runtime of this Comic.
        :type runtime: List[object]
        """

        self._runtime = runtime

    @property
    def production_company(self):
        """Gets the production_company of this Comic.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :return: The production_company of this Comic.
        :rtype: List[object]
        """
        return self._production_company

    @production_company.setter
    def production_company(self, production_company):
        """Sets the production_company of this Comic.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :param production_company: The production_company of this Comic.
        :type production_company: List[object]
        """

        self._production_company = production_company

    @property
    def label(self):
        """Gets the label of this Comic.

        short description of the resource  # noqa: E501

        :return: The label of this Comic.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Comic.

        short description of the resource  # noqa: E501

        :param label: The label of this Comic.
        :type label: List[str]
        """

        self._label = label

    @property
    def original_language(self):
        """Gets the original_language of this Comic.

        The original language of the work.  # noqa: E501

        :return: The original_language of this Comic.
        :rtype: List[object]
        """
        return self._original_language

    @original_language.setter
    def original_language(self, original_language):
        """Sets the original_language of this Comic.

        The original language of the work.  # noqa: E501

        :param original_language: The original_language of this Comic.
        :type original_language: List[object]
        """

        self._original_language = original_language

    @property
    def license(self):
        """Gets the license of this Comic.

        Description not available  # noqa: E501

        :return: The license of this Comic.
        :rtype: List[object]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Comic.

        Description not available  # noqa: E501

        :param license: The license of this Comic.
        :type license: List[object]
        """

        self._license = license

    @property
    def subject_term(self):
        """Gets the subject_term of this Comic.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :return: The subject_term of this Comic.
        :rtype: List[str]
        """
        return self._subject_term

    @subject_term.setter
    def subject_term(self, subject_term):
        """Sets the subject_term of this Comic.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :param subject_term: The subject_term of this Comic.
        :type subject_term: List[str]
        """

        self._subject_term = subject_term

    @property
    def original_title(self):
        """Gets the original_title of this Comic.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :return: The original_title of this Comic.
        :rtype: List[str]
        """
        return self._original_title

    @original_title.setter
    def original_title(self, original_title):
        """Sets the original_title of this Comic.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :param original_title: The original_title of this Comic.
        :type original_title: List[str]
        """

        self._original_title = original_title

    @property
    def circulation(self):
        """Gets the circulation of this Comic.

        Description not available  # noqa: E501

        :return: The circulation of this Comic.
        :rtype: List[int]
        """
        return self._circulation

    @circulation.setter
    def circulation(self, circulation):
        """Sets the circulation of this Comic.

        Description not available  # noqa: E501

        :param circulation: The circulation of this Comic.
        :type circulation: List[int]
        """

        self._circulation = circulation

    @property
    def oclc(self):
        """Gets the oclc of this Comic.

        Online Computer Library Center number  # noqa: E501

        :return: The oclc of this Comic.
        :rtype: List[str]
        """
        return self._oclc

    @oclc.setter
    def oclc(self, oclc):
        """Sets the oclc of this Comic.

        Online Computer Library Center number  # noqa: E501

        :param oclc: The oclc of this Comic.
        :type oclc: List[str]
        """

        self._oclc = oclc

    @property
    def producer(self):
        """Gets the producer of this Comic.

        The producer of the creative work.  # noqa: E501

        :return: The producer of this Comic.
        :rtype: List[object]
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this Comic.

        The producer of the creative work.  # noqa: E501

        :param producer: The producer of this Comic.
        :type producer: List[object]
        """

        self._producer = producer

    @property
    def starring(self):
        """Gets the starring of this Comic.

        Description not available  # noqa: E501

        :return: The starring of this Comic.
        :rtype: List[object]
        """
        return self._starring

    @starring.setter
    def starring(self, starring):
        """Sets the starring of this Comic.

        Description not available  # noqa: E501

        :param starring: The starring of this Comic.
        :type starring: List[object]
        """

        self._starring = starring

    @property
    def completion_date(self):
        """Gets the completion_date of this Comic.

        Description not available  # noqa: E501

        :return: The completion_date of this Comic.
        :rtype: List[str]
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this Comic.

        Description not available  # noqa: E501

        :param completion_date: The completion_date of this Comic.
        :type completion_date: List[str]
        """

        self._completion_date = completion_date

    @property
    def writer(self):
        """Gets the writer of this Comic.

        Description not available  # noqa: E501

        :return: The writer of this Comic.
        :rtype: List[object]
        """
        return self._writer

    @writer.setter
    def writer(self, writer):
        """Sets the writer of this Comic.

        Description not available  # noqa: E501

        :param writer: The writer of this Comic.
        :type writer: List[object]
        """

        self._writer = writer

    @property
    def magazine(self):
        """Gets the magazine of this Comic.

        Description not available  # noqa: E501

        :return: The magazine of this Comic.
        :rtype: List[object]
        """
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        """Sets the magazine of this Comic.

        Description not available  # noqa: E501

        :param magazine: The magazine of this Comic.
        :type magazine: List[object]
        """

        self._magazine = magazine
