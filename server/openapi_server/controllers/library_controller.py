import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LIBRARY_TYPE_NAME, LIBRARY_TYPE_URI

from openapi_server.models.library import Library  # noqa: E501
from openapi_server import util

def librarys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Library

    Gets a list of all instances of Library (more information in http://dbpedia.org/ontology/Library) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Library]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LIBRARY_TYPE_URI,
        rdf_type_name=LIBRARY_TYPE_NAME, 
        kls=Library)

def librarys_id_get(id):  # noqa: E501
    """Get a single Library by its id

    Gets the details of a given Library (more information in http://dbpedia.org/ontology/Library) # noqa: E501

    :param id: The ID of the Library to be retrieved
    :type id: str

    :rtype: Library
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LIBRARY_TYPE_URI,
        rdf_type_name=LIBRARY_TYPE_NAME, 
        kls=Library)
