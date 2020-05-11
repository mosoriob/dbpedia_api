import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ROUTEOFTRANSPORTATION_TYPE_NAME, ROUTEOFTRANSPORTATION_TYPE_URI

from openapi_server.models.route_of_transportation import RouteOfTransportation  # noqa: E501
from openapi_server import util

def routeoftransportations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RouteOfTransportation

    Gets a list of all instances of RouteOfTransportation (more information in http://dbpedia.org/ontology/RouteOfTransportation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RouteOfTransportation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ROUTEOFTRANSPORTATION_TYPE_URI,
        rdf_type_name=ROUTEOFTRANSPORTATION_TYPE_NAME, 
        kls=RouteOfTransportation)

def routeoftransportations_id_get(id):  # noqa: E501
    """Get a single RouteOfTransportation by its id

    Gets the details of a given RouteOfTransportation (more information in http://dbpedia.org/ontology/RouteOfTransportation) # noqa: E501

    :param id: The ID of the RouteOfTransportation to be retrieved
    :type id: str

    :rtype: RouteOfTransportation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ROUTEOFTRANSPORTATION_TYPE_URI,
        rdf_type_name=ROUTEOFTRANSPORTATION_TYPE_NAME, 
        kls=RouteOfTransportation)
