import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TENNISPLAYER_TYPE_NAME, TENNISPLAYER_TYPE_URI

from openapi_server.models.tennis_player import TennisPlayer  # noqa: E501
from openapi_server import util

def tennisplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TennisPlayer

    Gets a list of all instances of TennisPlayer (more information in http://dbpedia.org/ontology/TennisPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TennisPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TENNISPLAYER_TYPE_URI,
        rdf_type_name=TENNISPLAYER_TYPE_NAME, 
        kls=TennisPlayer)

def tennisplayers_id_get(id):  # noqa: E501
    """Get a single TennisPlayer by its id

    Gets the details of a given TennisPlayer (more information in http://dbpedia.org/ontology/TennisPlayer) # noqa: E501

    :param id: The ID of the TennisPlayer to be retrieved
    :type id: str

    :rtype: TennisPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TENNISPLAYER_TYPE_URI,
        rdf_type_name=TENNISPLAYER_TYPE_NAME, 
        kls=TennisPlayer)
