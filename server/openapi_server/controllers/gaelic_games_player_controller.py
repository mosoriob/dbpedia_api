import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GAELICGAMESPLAYER_TYPE_NAME, GAELICGAMESPLAYER_TYPE_URI

from openapi_server.models.gaelic_games_player import GaelicGamesPlayer  # noqa: E501
from openapi_server import util

def gaelicgamesplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GaelicGamesPlayer

    Gets a list of all instances of GaelicGamesPlayer (more information in http://dbpedia.org/ontology/GaelicGamesPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GaelicGamesPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GAELICGAMESPLAYER_TYPE_URI,
        rdf_type_name=GAELICGAMESPLAYER_TYPE_NAME, 
        kls=GaelicGamesPlayer)

def gaelicgamesplayers_id_get(id):  # noqa: E501
    """Get a single GaelicGamesPlayer by its id

    Gets the details of a given GaelicGamesPlayer (more information in http://dbpedia.org/ontology/GaelicGamesPlayer) # noqa: E501

    :param id: The ID of the GaelicGamesPlayer to be retrieved
    :type id: str

    :rtype: GaelicGamesPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GAELICGAMESPLAYER_TYPE_URI,
        rdf_type_name=GAELICGAMESPLAYER_TYPE_NAME, 
        kls=GaelicGamesPlayer)
