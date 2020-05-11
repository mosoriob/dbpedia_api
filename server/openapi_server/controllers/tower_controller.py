import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TOWER_TYPE_NAME, TOWER_TYPE_URI

from openapi_server.models.tower import Tower  # noqa: E501
from openapi_server import util

def towers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Tower

    Gets a list of all instances of Tower (more information in http://dbpedia.org/ontology/Tower) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Tower]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TOWER_TYPE_URI,
        rdf_type_name=TOWER_TYPE_NAME, 
        kls=Tower)

def towers_id_get(id):  # noqa: E501
    """Get a single Tower by its id

    Gets the details of a given Tower (more information in http://dbpedia.org/ontology/Tower) # noqa: E501

    :param id: The ID of the Tower to be retrieved
    :type id: str

    :rtype: Tower
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TOWER_TYPE_URI,
        rdf_type_name=TOWER_TYPE_NAME, 
        kls=Tower)
