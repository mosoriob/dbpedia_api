import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SENATOR_TYPE_NAME, SENATOR_TYPE_URI

from openapi_server.models.senator import Senator  # noqa: E501
from openapi_server import util

def senators_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Senator

    Gets a list of all instances of Senator (more information in http://dbpedia.org/ontology/Senator) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Senator]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SENATOR_TYPE_URI,
        rdf_type_name=SENATOR_TYPE_NAME, 
        kls=Senator)

def senators_id_get(id):  # noqa: E501
    """Get a single Senator by its id

    Gets the details of a given Senator (more information in http://dbpedia.org/ontology/Senator) # noqa: E501

    :param id: The ID of the Senator to be retrieved
    :type id: str

    :rtype: Senator
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SENATOR_TYPE_URI,
        rdf_type_name=SENATOR_TYPE_NAME, 
        kls=Senator)
