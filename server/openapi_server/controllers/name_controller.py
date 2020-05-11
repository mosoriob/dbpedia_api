import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NAME_TYPE_NAME, NAME_TYPE_URI

from openapi_server.models.name import Name  # noqa: E501
from openapi_server import util

def names_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Name

    Gets a list of all instances of Name (more information in http://dbpedia.org/ontology/Name) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Name]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NAME_TYPE_URI,
        rdf_type_name=NAME_TYPE_NAME, 
        kls=Name)

def names_id_get(id):  # noqa: E501
    """Get a single Name by its id

    Gets the details of a given Name (more information in http://dbpedia.org/ontology/Name) # noqa: E501

    :param id: The ID of the Name to be retrieved
    :type id: str

    :rtype: Name
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NAME_TYPE_URI,
        rdf_type_name=NAME_TYPE_NAME, 
        kls=Name)
