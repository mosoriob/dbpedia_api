import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MAYOR_TYPE_NAME, MAYOR_TYPE_URI

from openapi_server.models.mayor import Mayor  # noqa: E501
from openapi_server import util

def mayors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Mayor

    Gets a list of all instances of Mayor (more information in http://dbpedia.org/ontology/Mayor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Mayor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MAYOR_TYPE_URI,
        rdf_type_name=MAYOR_TYPE_NAME, 
        kls=Mayor)

def mayors_id_get(id):  # noqa: E501
    """Get a single Mayor by its id

    Gets the details of a given Mayor (more information in http://dbpedia.org/ontology/Mayor) # noqa: E501

    :param id: The ID of the Mayor to be retrieved
    :type id: str

    :rtype: Mayor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MAYOR_TYPE_URI,
        rdf_type_name=MAYOR_TYPE_NAME, 
        kls=Mayor)
