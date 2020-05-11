import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LIEUTENANT_TYPE_NAME, LIEUTENANT_TYPE_URI

from openapi_server.models.lieutenant import Lieutenant  # noqa: E501
from openapi_server import util

def lieutenants_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Lieutenant

    Gets a list of all instances of Lieutenant (more information in http://dbpedia.org/ontology/Lieutenant) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Lieutenant]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LIEUTENANT_TYPE_URI,
        rdf_type_name=LIEUTENANT_TYPE_NAME, 
        kls=Lieutenant)

def lieutenants_id_get(id):  # noqa: E501
    """Get a single Lieutenant by its id

    Gets the details of a given Lieutenant (more information in http://dbpedia.org/ontology/Lieutenant) # noqa: E501

    :param id: The ID of the Lieutenant to be retrieved
    :type id: str

    :rtype: Lieutenant
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LIEUTENANT_TYPE_URI,
        rdf_type_name=LIEUTENANT_TYPE_NAME, 
        kls=Lieutenant)
