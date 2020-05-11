import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOUNTAIN_TYPE_NAME, MOUNTAIN_TYPE_URI

from openapi_server.models.mountain import Mountain  # noqa: E501
from openapi_server import util

def mountains_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Mountain

    Gets a list of all instances of Mountain (more information in http://dbpedia.org/ontology/Mountain) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Mountain]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOUNTAIN_TYPE_URI,
        rdf_type_name=MOUNTAIN_TYPE_NAME, 
        kls=Mountain)

def mountains_id_get(id):  # noqa: E501
    """Get a single Mountain by its id

    Gets the details of a given Mountain (more information in http://dbpedia.org/ontology/Mountain) # noqa: E501

    :param id: The ID of the Mountain to be retrieved
    :type id: str

    :rtype: Mountain
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOUNTAIN_TYPE_URI,
        rdf_type_name=MOUNTAIN_TYPE_NAME, 
        kls=Mountain)
