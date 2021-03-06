import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LAKE_TYPE_NAME, LAKE_TYPE_URI

from openapi_server.models.lake import Lake  # noqa: E501
from openapi_server import util

def lakes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Lake

    Gets a list of all instances of Lake (more information in http://dbpedia.org/ontology/Lake) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Lake]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LAKE_TYPE_URI,
        rdf_type_name=LAKE_TYPE_NAME, 
        kls=Lake)

def lakes_id_get(id):  # noqa: E501
    """Get a single Lake by its id

    Gets the details of a given Lake (more information in http://dbpedia.org/ontology/Lake) # noqa: E501

    :param id: The ID of the Lake to be retrieved
    :type id: str

    :rtype: Lake
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LAKE_TYPE_URI,
        rdf_type_name=LAKE_TYPE_NAME, 
        kls=Lake)
