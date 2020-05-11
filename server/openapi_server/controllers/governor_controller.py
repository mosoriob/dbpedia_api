import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GOVERNOR_TYPE_NAME, GOVERNOR_TYPE_URI

from openapi_server.models.governor import Governor  # noqa: E501
from openapi_server import util

def governors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Governor

    Gets a list of all instances of Governor (more information in http://dbpedia.org/ontology/Governor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Governor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GOVERNOR_TYPE_URI,
        rdf_type_name=GOVERNOR_TYPE_NAME, 
        kls=Governor)

def governors_id_get(id):  # noqa: E501
    """Get a single Governor by its id

    Gets the details of a given Governor (more information in http://dbpedia.org/ontology/Governor) # noqa: E501

    :param id: The ID of the Governor to be retrieved
    :type id: str

    :rtype: Governor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GOVERNOR_TYPE_URI,
        rdf_type_name=GOVERNOR_TYPE_NAME, 
        kls=Governor)
