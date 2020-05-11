import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BEAUTYQUEEN_TYPE_NAME, BEAUTYQUEEN_TYPE_URI

from openapi_server.models.beauty_queen import BeautyQueen  # noqa: E501
from openapi_server import util

def beautyqueens_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BeautyQueen

    Gets a list of all instances of BeautyQueen (more information in http://dbpedia.org/ontology/BeautyQueen) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BeautyQueen]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BEAUTYQUEEN_TYPE_URI,
        rdf_type_name=BEAUTYQUEEN_TYPE_NAME, 
        kls=BeautyQueen)

def beautyqueens_id_get(id):  # noqa: E501
    """Get a single BeautyQueen by its id

    Gets the details of a given BeautyQueen (more information in http://dbpedia.org/ontology/BeautyQueen) # noqa: E501

    :param id: The ID of the BeautyQueen to be retrieved
    :type id: str

    :rtype: BeautyQueen
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BEAUTYQUEEN_TYPE_URI,
        rdf_type_name=BEAUTYQUEEN_TYPE_NAME, 
        kls=BeautyQueen)
