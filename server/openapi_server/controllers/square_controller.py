import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SQUARE_TYPE_NAME, SQUARE_TYPE_URI

from openapi_server.models.square import Square  # noqa: E501
from openapi_server import util

def squares_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Square

    Gets a list of all instances of Square (more information in http://dbpedia.org/ontology/Square) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Square]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SQUARE_TYPE_URI,
        rdf_type_name=SQUARE_TYPE_NAME, 
        kls=Square)

def squares_id_get(id):  # noqa: E501
    """Get a single Square by its id

    Gets the details of a given Square (more information in http://dbpedia.org/ontology/Square) # noqa: E501

    :param id: The ID of the Square to be retrieved
    :type id: str

    :rtype: Square
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SQUARE_TYPE_URI,
        rdf_type_name=SQUARE_TYPE_NAME, 
        kls=Square)
