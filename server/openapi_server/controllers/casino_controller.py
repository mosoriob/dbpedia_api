import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CASINO_TYPE_NAME, CASINO_TYPE_URI

from openapi_server.models.casino import Casino  # noqa: E501
from openapi_server import util

def casinos_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Casino

    Gets a list of all instances of Casino (more information in http://dbpedia.org/ontology/Casino) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Casino]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CASINO_TYPE_URI,
        rdf_type_name=CASINO_TYPE_NAME, 
        kls=Casino)

def casinos_id_get(id):  # noqa: E501
    """Get a single Casino by its id

    Gets the details of a given Casino (more information in http://dbpedia.org/ontology/Casino) # noqa: E501

    :param id: The ID of the Casino to be retrieved
    :type id: str

    :rtype: Casino
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CASINO_TYPE_URI,
        rdf_type_name=CASINO_TYPE_NAME, 
        kls=Casino)
