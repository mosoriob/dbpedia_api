import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HISTORIAN_TYPE_NAME, HISTORIAN_TYPE_URI

from openapi_server.models.historian import Historian  # noqa: E501
from openapi_server import util

def historians_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Historian

    Gets a list of all instances of Historian (more information in http://dbpedia.org/ontology/Historian) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Historian]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HISTORIAN_TYPE_URI,
        rdf_type_name=HISTORIAN_TYPE_NAME, 
        kls=Historian)

def historians_id_get(id):  # noqa: E501
    """Get a single Historian by its id

    Gets the details of a given Historian (more information in http://dbpedia.org/ontology/Historian) # noqa: E501

    :param id: The ID of the Historian to be retrieved
    :type id: str

    :rtype: Historian
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HISTORIAN_TYPE_URI,
        rdf_type_name=HISTORIAN_TYPE_NAME, 
        kls=Historian)
