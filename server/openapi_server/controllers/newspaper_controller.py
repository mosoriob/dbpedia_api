import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NEWSPAPER_TYPE_NAME, NEWSPAPER_TYPE_URI

from openapi_server.models.newspaper import Newspaper  # noqa: E501
from openapi_server import util

def newspapers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Newspaper

    Gets a list of all instances of Newspaper (more information in http://dbpedia.org/ontology/Newspaper) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Newspaper]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NEWSPAPER_TYPE_URI,
        rdf_type_name=NEWSPAPER_TYPE_NAME, 
        kls=Newspaper)

def newspapers_id_get(id):  # noqa: E501
    """Get a single Newspaper by its id

    Gets the details of a given Newspaper (more information in http://dbpedia.org/ontology/Newspaper) # noqa: E501

    :param id: The ID of the Newspaper to be retrieved
    :type id: str

    :rtype: Newspaper
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NEWSPAPER_TYPE_URI,
        rdf_type_name=NEWSPAPER_TYPE_NAME, 
        kls=Newspaper)
