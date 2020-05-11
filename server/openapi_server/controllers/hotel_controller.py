import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HOTEL_TYPE_NAME, HOTEL_TYPE_URI

from openapi_server.models.hotel import Hotel  # noqa: E501
from openapi_server import util

def hotels_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Hotel

    Gets a list of all instances of Hotel (more information in http://dbpedia.org/ontology/Hotel) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Hotel]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HOTEL_TYPE_URI,
        rdf_type_name=HOTEL_TYPE_NAME, 
        kls=Hotel)

def hotels_id_get(id):  # noqa: E501
    """Get a single Hotel by its id

    Gets the details of a given Hotel (more information in http://dbpedia.org/ontology/Hotel) # noqa: E501

    :param id: The ID of the Hotel to be retrieved
    :type id: str

    :rtype: Hotel
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HOTEL_TYPE_URI,
        rdf_type_name=HOTEL_TYPE_NAME, 
        kls=Hotel)
