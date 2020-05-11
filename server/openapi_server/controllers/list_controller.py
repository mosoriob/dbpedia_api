import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LIST_TYPE_NAME, LIST_TYPE_URI

from openapi_server import util

def lists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of List

    Gets a list of all instances of List (more information in http://dbpedia.org/ontology/List) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[List]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LIST_TYPE_URI,
        rdf_type_name=LIST_TYPE_NAME, 
        kls=List)

def lists_id_get(id):  # noqa: E501
    """Get a single List by its id

    Gets the details of a given List (more information in http://dbpedia.org/ontology/List) # noqa: E501

    :param id: The ID of the List to be retrieved
    :type id: str

    :rtype: List
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LIST_TYPE_URI,
        rdf_type_name=LIST_TYPE_NAME, 
        kls=List)
