import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AIRLINE_TYPE_NAME, AIRLINE_TYPE_URI

from openapi_server.models.airline import Airline  # noqa: E501
from openapi_server import util

def airlines_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Airline

    Gets a list of all instances of Airline (more information in http://dbpedia.org/ontology/Airline) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Airline]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AIRLINE_TYPE_URI,
        rdf_type_name=AIRLINE_TYPE_NAME, 
        kls=Airline)

def airlines_id_get(id):  # noqa: E501
    """Get a single Airline by its id

    Gets the details of a given Airline (more information in http://dbpedia.org/ontology/Airline) # noqa: E501

    :param id: The ID of the Airline to be retrieved
    :type id: str

    :rtype: Airline
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AIRLINE_TYPE_URI,
        rdf_type_name=AIRLINE_TYPE_NAME, 
        kls=Airline)
