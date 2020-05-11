import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CAVE_TYPE_NAME, CAVE_TYPE_URI

from openapi_server.models.cave import Cave  # noqa: E501
from openapi_server import util

def caves_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Cave

    Gets a list of all instances of Cave (more information in http://dbpedia.org/ontology/Cave) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Cave]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CAVE_TYPE_URI,
        rdf_type_name=CAVE_TYPE_NAME, 
        kls=Cave)

def caves_id_get(id):  # noqa: E501
    """Get a single Cave by its id

    Gets the details of a given Cave (more information in http://dbpedia.org/ontology/Cave) # noqa: E501

    :param id: The ID of the Cave to be retrieved
    :type id: str

    :rtype: Cave
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CAVE_TYPE_URI,
        rdf_type_name=CAVE_TYPE_NAME, 
        kls=Cave)
