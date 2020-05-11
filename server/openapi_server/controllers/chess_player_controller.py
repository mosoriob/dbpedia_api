import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHESSPLAYER_TYPE_NAME, CHESSPLAYER_TYPE_URI

from openapi_server.models.chess_player import ChessPlayer  # noqa: E501
from openapi_server import util

def chessplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ChessPlayer

    Gets a list of all instances of ChessPlayer (more information in http://dbpedia.org/ontology/ChessPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ChessPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHESSPLAYER_TYPE_URI,
        rdf_type_name=CHESSPLAYER_TYPE_NAME, 
        kls=ChessPlayer)

def chessplayers_id_get(id):  # noqa: E501
    """Get a single ChessPlayer by its id

    Gets the details of a given ChessPlayer (more information in http://dbpedia.org/ontology/ChessPlayer) # noqa: E501

    :param id: The ID of the ChessPlayer to be retrieved
    :type id: str

    :rtype: ChessPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHESSPLAYER_TYPE_URI,
        rdf_type_name=CHESSPLAYER_TYPE_NAME, 
        kls=ChessPlayer)
