import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SAINT_TYPE_NAME, SAINT_TYPE_URI

from openapi_server.models.saint import Saint  # noqa: E501
from openapi_server import util

def saints_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Saint

    Gets a list of all instances of Saint (more information in http://dbpedia.org/ontology/Saint) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Saint]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SAINT_TYPE_URI,
        rdf_type_name=SAINT_TYPE_NAME, 
        kls=Saint)

def saints_id_get(id):  # noqa: E501
    """Get a single Saint by its id

    Gets the details of a given Saint (more information in http://dbpedia.org/ontology/Saint) # noqa: E501

    :param id: The ID of the Saint to be retrieved
    :type id: str

    :rtype: Saint
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SAINT_TYPE_URI,
        rdf_type_name=SAINT_TYPE_NAME, 
        kls=Saint)
