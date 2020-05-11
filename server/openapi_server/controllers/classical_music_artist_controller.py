import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CLASSICALMUSICARTIST_TYPE_NAME, CLASSICALMUSICARTIST_TYPE_URI

from openapi_server.models.classical_music_artist import ClassicalMusicArtist  # noqa: E501
from openapi_server import util

def classicalmusicartists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ClassicalMusicArtist

    Gets a list of all instances of ClassicalMusicArtist (more information in http://dbpedia.org/ontology/ClassicalMusicArtist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ClassicalMusicArtist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CLASSICALMUSICARTIST_TYPE_URI,
        rdf_type_name=CLASSICALMUSICARTIST_TYPE_NAME, 
        kls=ClassicalMusicArtist)

def classicalmusicartists_id_get(id):  # noqa: E501
    """Get a single ClassicalMusicArtist by its id

    Gets the details of a given ClassicalMusicArtist (more information in http://dbpedia.org/ontology/ClassicalMusicArtist) # noqa: E501

    :param id: The ID of the ClassicalMusicArtist to be retrieved
    :type id: str

    :rtype: ClassicalMusicArtist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CLASSICALMUSICARTIST_TYPE_URI,
        rdf_type_name=CLASSICALMUSICARTIST_TYPE_NAME, 
        kls=ClassicalMusicArtist)
