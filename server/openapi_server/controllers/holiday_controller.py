import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HOLIDAY_TYPE_NAME, HOLIDAY_TYPE_URI

from openapi_server.models.holiday import Holiday  # noqa: E501
from openapi_server import util

def holidays_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Holiday

    Gets a list of all instances of Holiday (more information in http://dbpedia.org/ontology/Holiday) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Holiday]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HOLIDAY_TYPE_URI,
        rdf_type_name=HOLIDAY_TYPE_NAME, 
        kls=Holiday)

def holidays_id_get(id):  # noqa: E501
    """Get a single Holiday by its id

    Gets the details of a given Holiday (more information in http://dbpedia.org/ontology/Holiday) # noqa: E501

    :param id: The ID of the Holiday to be retrieved
    :type id: str

    :rtype: Holiday
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HOLIDAY_TYPE_URI,
        rdf_type_name=HOLIDAY_TYPE_NAME, 
        kls=Holiday)
