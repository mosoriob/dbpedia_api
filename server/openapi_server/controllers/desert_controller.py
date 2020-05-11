import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DESERT_TYPE_NAME, DESERT_TYPE_URI

from openapi_server.models.desert import Desert  # noqa: E501
from openapi_server import util

def deserts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Desert

    Gets a list of all instances of Desert (more information in http://dbpedia.org/ontology/Desert) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Desert]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DESERT_TYPE_URI,
        rdf_type_name=DESERT_TYPE_NAME, 
        kls=Desert)

def deserts_id_get(id):  # noqa: E501
    """Get a single Desert by its id

    Gets the details of a given Desert (more information in http://dbpedia.org/ontology/Desert) # noqa: E501

    :param id: The ID of the Desert to be retrieved
    :type id: str

    :rtype: Desert
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DESERT_TYPE_URI,
        rdf_type_name=DESERT_TYPE_NAME, 
        kls=Desert)
