import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import OLYMPICS_TYPE_NAME, OLYMPICS_TYPE_URI

from openapi_server.models.olympics import Olympics  # noqa: E501
from openapi_server import util

def olympicss_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Olympics

    Gets a list of all instances of Olympics (more information in http://dbpedia.org/ontology/Olympics) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Olympics]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=OLYMPICS_TYPE_URI,
        rdf_type_name=OLYMPICS_TYPE_NAME, 
        kls=Olympics)

def olympicss_id_get(id):  # noqa: E501
    """Get a single Olympics by its id

    Gets the details of a given Olympics (more information in http://dbpedia.org/ontology/Olympics) # noqa: E501

    :param id: The ID of the Olympics to be retrieved
    :type id: str

    :rtype: Olympics
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=OLYMPICS_TYPE_URI,
        rdf_type_name=OLYMPICS_TYPE_NAME, 
        kls=Olympics)
