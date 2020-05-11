import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import INFRASTRUCTURE_TYPE_NAME, INFRASTRUCTURE_TYPE_URI

from openapi_server.models.infrastructure import Infrastructure  # noqa: E501
from openapi_server import util

def infrastructures_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Infrastructure

    Gets a list of all instances of Infrastructure (more information in http://dbpedia.org/ontology/Infrastructure) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Infrastructure]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=INFRASTRUCTURE_TYPE_URI,
        rdf_type_name=INFRASTRUCTURE_TYPE_NAME, 
        kls=Infrastructure)

def infrastructures_id_get(id):  # noqa: E501
    """Get a single Infrastructure by its id

    Gets the details of a given Infrastructure (more information in http://dbpedia.org/ontology/Infrastructure) # noqa: E501

    :param id: The ID of the Infrastructure to be retrieved
    :type id: str

    :rtype: Infrastructure
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=INFRASTRUCTURE_TYPE_URI,
        rdf_type_name=INFRASTRUCTURE_TYPE_NAME, 
        kls=Infrastructure)
