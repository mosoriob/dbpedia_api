import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DEPTH_TYPE_NAME, DEPTH_TYPE_URI

from openapi_server.models.depth import Depth  # noqa: E501
from openapi_server import util

def depths_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Depth

    Gets a list of all instances of Depth (more information in http://dbpedia.org/ontology/Depth) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Depth]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DEPTH_TYPE_URI,
        rdf_type_name=DEPTH_TYPE_NAME, 
        kls=Depth)

def depths_id_get(id):  # noqa: E501
    """Get a single Depth by its id

    Gets the details of a given Depth (more information in http://dbpedia.org/ontology/Depth) # noqa: E501

    :param id: The ID of the Depth to be retrieved
    :type id: str

    :rtype: Depth
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DEPTH_TYPE_URI,
        rdf_type_name=DEPTH_TYPE_NAME, 
        kls=Depth)
