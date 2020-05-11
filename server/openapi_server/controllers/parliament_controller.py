import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PARLIAMENT_TYPE_NAME, PARLIAMENT_TYPE_URI

from openapi_server.models.parliament import Parliament  # noqa: E501
from openapi_server import util

def parliaments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Parliament

    Gets a list of all instances of Parliament (more information in http://dbpedia.org/ontology/Parliament) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Parliament]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PARLIAMENT_TYPE_URI,
        rdf_type_name=PARLIAMENT_TYPE_NAME, 
        kls=Parliament)

def parliaments_id_get(id):  # noqa: E501
    """Get a single Parliament by its id

    Gets the details of a given Parliament (more information in http://dbpedia.org/ontology/Parliament) # noqa: E501

    :param id: The ID of the Parliament to be retrieved
    :type id: str

    :rtype: Parliament
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PARLIAMENT_TYPE_URI,
        rdf_type_name=PARLIAMENT_TYPE_NAME, 
        kls=Parliament)
