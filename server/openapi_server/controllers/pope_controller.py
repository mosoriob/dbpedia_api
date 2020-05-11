import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POPE_TYPE_NAME, POPE_TYPE_URI

from openapi_server.models.pope import Pope  # noqa: E501
from openapi_server import util

def popes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Pope

    Gets a list of all instances of Pope (more information in http://dbpedia.org/ontology/Pope) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Pope]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POPE_TYPE_URI,
        rdf_type_name=POPE_TYPE_NAME, 
        kls=Pope)

def popes_id_get(id):  # noqa: E501
    """Get a single Pope by its id

    Gets the details of a given Pope (more information in http://dbpedia.org/ontology/Pope) # noqa: E501

    :param id: The ID of the Pope to be retrieved
    :type id: str

    :rtype: Pope
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POPE_TYPE_URI,
        rdf_type_name=POPE_TYPE_NAME, 
        kls=Pope)
