import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PARK_TYPE_NAME, PARK_TYPE_URI

from openapi_server.models.park import Park  # noqa: E501
from openapi_server import util

def parks_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Park

    Gets a list of all instances of Park (more information in http://dbpedia.org/ontology/Park) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Park]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PARK_TYPE_URI,
        rdf_type_name=PARK_TYPE_NAME, 
        kls=Park)

def parks_id_get(id):  # noqa: E501
    """Get a single Park by its id

    Gets the details of a given Park (more information in http://dbpedia.org/ontology/Park) # noqa: E501

    :param id: The ID of the Park to be retrieved
    :type id: str

    :rtype: Park
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PARK_TYPE_URI,
        rdf_type_name=PARK_TYPE_NAME, 
        kls=Park)
