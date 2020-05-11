import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NOBLE_TYPE_NAME, NOBLE_TYPE_URI

from openapi_server.models.noble import Noble  # noqa: E501
from openapi_server import util

def nobles_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Noble

    Gets a list of all instances of Noble (more information in http://dbpedia.org/ontology/Noble) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Noble]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NOBLE_TYPE_URI,
        rdf_type_name=NOBLE_TYPE_NAME, 
        kls=Noble)

def nobles_id_get(id):  # noqa: E501
    """Get a single Noble by its id

    Gets the details of a given Noble (more information in http://dbpedia.org/ontology/Noble) # noqa: E501

    :param id: The ID of the Noble to be retrieved
    :type id: str

    :rtype: Noble
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NOBLE_TYPE_URI,
        rdf_type_name=NOBLE_TYPE_NAME, 
        kls=Noble)
