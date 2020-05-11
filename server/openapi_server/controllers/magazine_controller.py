import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MAGAZINE_TYPE_NAME, MAGAZINE_TYPE_URI

from openapi_server.models.magazine import Magazine  # noqa: E501
from openapi_server import util

def magazines_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Magazine

    Gets a list of all instances of Magazine (more information in http://dbpedia.org/ontology/Magazine) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Magazine]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MAGAZINE_TYPE_URI,
        rdf_type_name=MAGAZINE_TYPE_NAME, 
        kls=Magazine)

def magazines_id_get(id):  # noqa: E501
    """Get a single Magazine by its id

    Gets the details of a given Magazine (more information in http://dbpedia.org/ontology/Magazine) # noqa: E501

    :param id: The ID of the Magazine to be retrieved
    :type id: str

    :rtype: Magazine
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MAGAZINE_TYPE_URI,
        rdf_type_name=MAGAZINE_TYPE_NAME, 
        kls=Magazine)
