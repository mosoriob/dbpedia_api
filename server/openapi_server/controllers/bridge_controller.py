import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BRIDGE_TYPE_NAME, BRIDGE_TYPE_URI

from openapi_server.models.bridge import Bridge  # noqa: E501
from openapi_server import util

def bridges_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Bridge

    Gets a list of all instances of Bridge (more information in http://dbpedia.org/ontology/Bridge) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Bridge]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BRIDGE_TYPE_URI,
        rdf_type_name=BRIDGE_TYPE_NAME, 
        kls=Bridge)

def bridges_id_get(id):  # noqa: E501
    """Get a single Bridge by its id

    Gets the details of a given Bridge (more information in http://dbpedia.org/ontology/Bridge) # noqa: E501

    :param id: The ID of the Bridge to be retrieved
    :type id: str

    :rtype: Bridge
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BRIDGE_TYPE_URI,
        rdf_type_name=BRIDGE_TYPE_NAME, 
        kls=Bridge)
