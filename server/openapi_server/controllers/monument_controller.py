import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MONUMENT_TYPE_NAME, MONUMENT_TYPE_URI

from openapi_server.models.monument import Monument  # noqa: E501
from openapi_server import util

def monuments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Monument

    Gets a list of all instances of Monument (more information in http://dbpedia.org/ontology/Monument) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Monument]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MONUMENT_TYPE_URI,
        rdf_type_name=MONUMENT_TYPE_NAME, 
        kls=Monument)

def monuments_id_get(id):  # noqa: E501
    """Get a single Monument by its id

    Gets the details of a given Monument (more information in http://dbpedia.org/ontology/Monument) # noqa: E501

    :param id: The ID of the Monument to be retrieved
    :type id: str

    :rtype: Monument
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MONUMENT_TYPE_URI,
        rdf_type_name=MONUMENT_TYPE_NAME, 
        kls=Monument)
