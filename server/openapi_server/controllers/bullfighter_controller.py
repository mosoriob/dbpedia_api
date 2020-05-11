import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BULLFIGHTER_TYPE_NAME, BULLFIGHTER_TYPE_URI

from openapi_server.models.bullfighter import Bullfighter  # noqa: E501
from openapi_server import util

def bullfighters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Bullfighter

    Gets a list of all instances of Bullfighter (more information in http://dbpedia.org/ontology/Bullfighter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Bullfighter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BULLFIGHTER_TYPE_URI,
        rdf_type_name=BULLFIGHTER_TYPE_NAME, 
        kls=Bullfighter)

def bullfighters_id_get(id):  # noqa: E501
    """Get a single Bullfighter by its id

    Gets the details of a given Bullfighter (more information in http://dbpedia.org/ontology/Bullfighter) # noqa: E501

    :param id: The ID of the Bullfighter to be retrieved
    :type id: str

    :rtype: Bullfighter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BULLFIGHTER_TYPE_URI,
        rdf_type_name=BULLFIGHTER_TYPE_NAME, 
        kls=Bullfighter)
