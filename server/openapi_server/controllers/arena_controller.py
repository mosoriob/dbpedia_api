import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARENA_TYPE_NAME, ARENA_TYPE_URI

from openapi_server.models.arena import Arena  # noqa: E501
from openapi_server import util

def arenas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Arena

    Gets a list of all instances of Arena (more information in http://dbpedia.org/ontology/Arena) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Arena]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARENA_TYPE_URI,
        rdf_type_name=ARENA_TYPE_NAME, 
        kls=Arena)

def arenas_id_get(id):  # noqa: E501
    """Get a single Arena by its id

    Gets the details of a given Arena (more information in http://dbpedia.org/ontology/Arena) # noqa: E501

    :param id: The ID of the Arena to be retrieved
    :type id: str

    :rtype: Arena
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARENA_TYPE_URI,
        rdf_type_name=ARENA_TYPE_NAME, 
        kls=Arena)
