import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TUNNEL_TYPE_NAME, TUNNEL_TYPE_URI

from openapi_server.models.tunnel import Tunnel  # noqa: E501
from openapi_server import util

def tunnels_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Tunnel

    Gets a list of all instances of Tunnel (more information in http://dbpedia.org/ontology/Tunnel) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Tunnel]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TUNNEL_TYPE_URI,
        rdf_type_name=TUNNEL_TYPE_NAME, 
        kls=Tunnel)

def tunnels_id_get(id):  # noqa: E501
    """Get a single Tunnel by its id

    Gets the details of a given Tunnel (more information in http://dbpedia.org/ontology/Tunnel) # noqa: E501

    :param id: The ID of the Tunnel to be retrieved
    :type id: str

    :rtype: Tunnel
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TUNNEL_TYPE_URI,
        rdf_type_name=TUNNEL_TYPE_NAME, 
        kls=Tunnel)
