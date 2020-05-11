import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ROADTUNNEL_TYPE_NAME, ROADTUNNEL_TYPE_URI

from openapi_server.models.road_tunnel import RoadTunnel  # noqa: E501
from openapi_server import util

def roadtunnels_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RoadTunnel

    Gets a list of all instances of RoadTunnel (more information in http://dbpedia.org/ontology/RoadTunnel) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RoadTunnel]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ROADTUNNEL_TYPE_URI,
        rdf_type_name=ROADTUNNEL_TYPE_NAME, 
        kls=RoadTunnel)

def roadtunnels_id_get(id):  # noqa: E501
    """Get a single RoadTunnel by its id

    Gets the details of a given RoadTunnel (more information in http://dbpedia.org/ontology/RoadTunnel) # noqa: E501

    :param id: The ID of the RoadTunnel to be retrieved
    :type id: str

    :rtype: RoadTunnel
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ROADTUNNEL_TYPE_URI,
        rdf_type_name=ROADTUNNEL_TYPE_NAME, 
        kls=RoadTunnel)
