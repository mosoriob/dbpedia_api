import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SEA_TYPE_NAME, SEA_TYPE_URI

from openapi_server.models.sea import Sea  # noqa: E501
from openapi_server import util

def seas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Sea

    Gets a list of all instances of Sea (more information in http://dbpedia.org/ontology/Sea) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Sea]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SEA_TYPE_URI,
        rdf_type_name=SEA_TYPE_NAME, 
        kls=Sea)

def seas_id_get(id):  # noqa: E501
    """Get a single Sea by its id

    Gets the details of a given Sea (more information in http://dbpedia.org/ontology/Sea) # noqa: E501

    :param id: The ID of the Sea to be retrieved
    :type id: str

    :rtype: Sea
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SEA_TYPE_URI,
        rdf_type_name=SEA_TYPE_NAME, 
        kls=Sea)
