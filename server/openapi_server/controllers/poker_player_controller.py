import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POKERPLAYER_TYPE_NAME, POKERPLAYER_TYPE_URI

from openapi_server.models.poker_player import PokerPlayer  # noqa: E501
from openapi_server import util

def pokerplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PokerPlayer

    Gets a list of all instances of PokerPlayer (more information in http://dbpedia.org/ontology/PokerPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PokerPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POKERPLAYER_TYPE_URI,
        rdf_type_name=POKERPLAYER_TYPE_NAME, 
        kls=PokerPlayer)

def pokerplayers_id_get(id):  # noqa: E501
    """Get a single PokerPlayer by its id

    Gets the details of a given PokerPlayer (more information in http://dbpedia.org/ontology/PokerPlayer) # noqa: E501

    :param id: The ID of the PokerPlayer to be retrieved
    :type id: str

    :rtype: PokerPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POKERPLAYER_TYPE_URI,
        rdf_type_name=POKERPLAYER_TYPE_NAME, 
        kls=PokerPlayer)
