import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RIVER_TYPE_NAME, RIVER_TYPE_URI

from openapi_server.models.river import River  # noqa: E501
from openapi_server import util

def rivers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of River

    Gets a list of all instances of River (more information in http://dbpedia.org/ontology/River) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[River]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RIVER_TYPE_URI,
        rdf_type_name=RIVER_TYPE_NAME, 
        kls=River)

def rivers_id_get(id):  # noqa: E501
    """Get a single River by its id

    Gets the details of a given River (more information in http://dbpedia.org/ontology/River) # noqa: E501

    :param id: The ID of the River to be retrieved
    :type id: str

    :rtype: River
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RIVER_TYPE_URI,
        rdf_type_name=RIVER_TYPE_NAME, 
        kls=River)
