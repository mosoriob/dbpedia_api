import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LOCK_TYPE_NAME, LOCK_TYPE_URI

from openapi_server.models.lock import Lock  # noqa: E501
from openapi_server import util

def locks_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Lock

    Gets a list of all instances of Lock (more information in http://dbpedia.org/ontology/Lock) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Lock]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LOCK_TYPE_URI,
        rdf_type_name=LOCK_TYPE_NAME, 
        kls=Lock)

def locks_id_get(id):  # noqa: E501
    """Get a single Lock by its id

    Gets the details of a given Lock (more information in http://dbpedia.org/ontology/Lock) # noqa: E501

    :param id: The ID of the Lock to be retrieved
    :type id: str

    :rtype: Lock
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LOCK_TYPE_URI,
        rdf_type_name=LOCK_TYPE_NAME, 
        kls=Lock)
