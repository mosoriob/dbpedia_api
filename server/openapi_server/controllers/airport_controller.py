import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AIRPORT_TYPE_NAME, AIRPORT_TYPE_URI

from openapi_server.models.airport import Airport  # noqa: E501
from openapi_server import util

def airports_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Airport

    Gets a list of all instances of Airport (more information in http://dbpedia.org/ontology/Airport) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Airport]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AIRPORT_TYPE_URI,
        rdf_type_name=AIRPORT_TYPE_NAME, 
        kls=Airport)

def airports_id_get(id):  # noqa: E501
    """Get a single Airport by its id

    Gets the details of a given Airport (more information in http://dbpedia.org/ontology/Airport) # noqa: E501

    :param id: The ID of the Airport to be retrieved
    :type id: str

    :rtype: Airport
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AIRPORT_TYPE_URI,
        rdf_type_name=AIRPORT_TYPE_NAME, 
        kls=Airport)
