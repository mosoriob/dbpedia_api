import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VIDEOGAMESLEAGUE_TYPE_NAME, VIDEOGAMESLEAGUE_TYPE_URI

from openapi_server.models.videogames_league import VideogamesLeague  # noqa: E501
from openapi_server import util

def videogamesleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of VideogamesLeague

    Gets a list of all instances of VideogamesLeague (more information in http://dbpedia.org/ontology/VideogamesLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[VideogamesLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VIDEOGAMESLEAGUE_TYPE_URI,
        rdf_type_name=VIDEOGAMESLEAGUE_TYPE_NAME, 
        kls=VideogamesLeague)

def videogamesleagues_id_get(id):  # noqa: E501
    """Get a single VideogamesLeague by its id

    Gets the details of a given VideogamesLeague (more information in http://dbpedia.org/ontology/VideogamesLeague) # noqa: E501

    :param id: The ID of the VideogamesLeague to be retrieved
    :type id: str

    :rtype: VideogamesLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VIDEOGAMESLEAGUE_TYPE_URI,
        rdf_type_name=VIDEOGAMESLEAGUE_TYPE_NAME, 
        kls=VideogamesLeague)
