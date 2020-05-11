import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ATHLETICS_TYPE_NAME, ATHLETICS_TYPE_URI

from openapi_server.models.athletics import Athletics  # noqa: E501
from openapi_server import util

def athleticss_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Athletics

    Gets a list of all instances of Athletics (more information in http://dbpedia.org/ontology/Athletics) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Athletics]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ATHLETICS_TYPE_URI,
        rdf_type_name=ATHLETICS_TYPE_NAME, 
        kls=Athletics)

def athleticss_id_get(id):  # noqa: E501
    """Get a single Athletics by its id

    Gets the details of a given Athletics (more information in http://dbpedia.org/ontology/Athletics) # noqa: E501

    :param id: The ID of the Athletics to be retrieved
    :type id: str

    :rtype: Athletics
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ATHLETICS_TYPE_URI,
        rdf_type_name=ATHLETICS_TYPE_NAME, 
        kls=Athletics)
