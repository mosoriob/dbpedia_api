import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ANIME_TYPE_NAME, ANIME_TYPE_URI

from openapi_server.models.anime import Anime  # noqa: E501
from openapi_server import util

def animes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Anime

    Gets a list of all instances of Anime (more information in http://dbpedia.org/ontology/Anime) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Anime]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ANIME_TYPE_URI,
        rdf_type_name=ANIME_TYPE_NAME, 
        kls=Anime)

def animes_id_get(id):  # noqa: E501
    """Get a single Anime by its id

    Gets the details of a given Anime (more information in http://dbpedia.org/ontology/Anime) # noqa: E501

    :param id: The ID of the Anime to be retrieved
    :type id: str

    :rtype: Anime
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ANIME_TYPE_URI,
        rdf_type_name=ANIME_TYPE_NAME, 
        kls=Anime)
