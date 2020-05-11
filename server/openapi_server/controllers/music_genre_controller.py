import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MUSICGENRE_TYPE_NAME, MUSICGENRE_TYPE_URI

from openapi_server.models.music_genre import MusicGenre  # noqa: E501
from openapi_server import util

def musicgenres_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MusicGenre

    Gets a list of all instances of MusicGenre (more information in http://dbpedia.org/ontology/MusicGenre) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MusicGenre]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MUSICGENRE_TYPE_URI,
        rdf_type_name=MUSICGENRE_TYPE_NAME, 
        kls=MusicGenre)

def musicgenres_id_get(id):  # noqa: E501
    """Get a single MusicGenre by its id

    Gets the details of a given MusicGenre (more information in http://dbpedia.org/ontology/MusicGenre) # noqa: E501

    :param id: The ID of the MusicGenre to be retrieved
    :type id: str

    :rtype: MusicGenre
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MUSICGENRE_TYPE_URI,
        rdf_type_name=MUSICGENRE_TYPE_NAME, 
        kls=MusicGenre)
