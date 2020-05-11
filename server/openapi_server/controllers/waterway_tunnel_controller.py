import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WATERWAYTUNNEL_TYPE_NAME, WATERWAYTUNNEL_TYPE_URI

from openapi_server.models.waterway_tunnel import WaterwayTunnel  # noqa: E501
from openapi_server import util

def waterwaytunnels_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of WaterwayTunnel

    Gets a list of all instances of WaterwayTunnel (more information in http://dbpedia.org/ontology/WaterwayTunnel) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[WaterwayTunnel]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WATERWAYTUNNEL_TYPE_URI,
        rdf_type_name=WATERWAYTUNNEL_TYPE_NAME, 
        kls=WaterwayTunnel)

def waterwaytunnels_id_get(id):  # noqa: E501
    """Get a single WaterwayTunnel by its id

    Gets the details of a given WaterwayTunnel (more information in http://dbpedia.org/ontology/WaterwayTunnel) # noqa: E501

    :param id: The ID of the WaterwayTunnel to be retrieved
    :type id: str

    :rtype: WaterwayTunnel
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WATERWAYTUNNEL_TYPE_URI,
        rdf_type_name=WATERWAYTUNNEL_TYPE_NAME, 
        kls=WaterwayTunnel)
