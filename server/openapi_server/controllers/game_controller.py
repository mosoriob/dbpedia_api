import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GAME_TYPE_NAME, GAME_TYPE_URI

from openapi_server.models.game import Game  # noqa: E501
from openapi_server import util

def games_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Game

    Gets a list of all instances of Game (more information in http://dbpedia.org/ontology/Game) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Game]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GAME_TYPE_URI,
        rdf_type_name=GAME_TYPE_NAME, 
        kls=Game)

def games_id_get(id):  # noqa: E501
    """Get a single Game by its id

    Gets the details of a given Game (more information in http://dbpedia.org/ontology/Game) # noqa: E501

    :param id: The ID of the Game to be retrieved
    :type id: str

    :rtype: Game
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GAME_TYPE_URI,
        rdf_type_name=GAME_TYPE_NAME, 
        kls=Game)
