import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RAILWAYTUNNEL_TYPE_NAME, RAILWAYTUNNEL_TYPE_URI

from openapi_server.models.railway_tunnel import RailwayTunnel  # noqa: E501
from openapi_server import util

def railwaytunnels_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RailwayTunnel

    Gets a list of all instances of RailwayTunnel (more information in http://dbpedia.org/ontology/RailwayTunnel) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RailwayTunnel]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RAILWAYTUNNEL_TYPE_URI,
        rdf_type_name=RAILWAYTUNNEL_TYPE_NAME, 
        kls=RailwayTunnel)

def railwaytunnels_id_get(id):  # noqa: E501
    """Get a single RailwayTunnel by its id

    Gets the details of a given RailwayTunnel (more information in http://dbpedia.org/ontology/RailwayTunnel) # noqa: E501

    :param id: The ID of the RailwayTunnel to be retrieved
    :type id: str

    :rtype: RailwayTunnel
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RAILWAYTUNNEL_TYPE_URI,
        rdf_type_name=RAILWAYTUNNEL_TYPE_NAME, 
        kls=RailwayTunnel)
