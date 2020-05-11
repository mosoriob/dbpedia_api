import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BOARDGAME_TYPE_NAME, BOARDGAME_TYPE_URI

from openapi_server.models.board_game import BoardGame  # noqa: E501
from openapi_server import util

def boardgames_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BoardGame

    Gets a list of all instances of BoardGame (more information in http://dbpedia.org/ontology/BoardGame) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BoardGame]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BOARDGAME_TYPE_URI,
        rdf_type_name=BOARDGAME_TYPE_NAME, 
        kls=BoardGame)

def boardgames_id_get(id):  # noqa: E501
    """Get a single BoardGame by its id

    Gets the details of a given BoardGame (more information in http://dbpedia.org/ontology/BoardGame) # noqa: E501

    :param id: The ID of the BoardGame to be retrieved
    :type id: str

    :rtype: BoardGame
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BOARDGAME_TYPE_URI,
        rdf_type_name=BOARDGAME_TYPE_NAME, 
        kls=BoardGame)
