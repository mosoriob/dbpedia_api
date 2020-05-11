import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOCCERPLAYER_TYPE_NAME, SOCCERPLAYER_TYPE_URI

from openapi_server.models.soccer_player import SoccerPlayer  # noqa: E501
from openapi_server import util

def soccerplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoccerPlayer

    Gets a list of all instances of SoccerPlayer (more information in http://dbpedia.org/ontology/SoccerPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoccerPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOCCERPLAYER_TYPE_URI,
        rdf_type_name=SOCCERPLAYER_TYPE_NAME, 
        kls=SoccerPlayer)

def soccerplayers_id_get(id):  # noqa: E501
    """Get a single SoccerPlayer by its id

    Gets the details of a given SoccerPlayer (more information in http://dbpedia.org/ontology/SoccerPlayer) # noqa: E501

    :param id: The ID of the SoccerPlayer to be retrieved
    :type id: str

    :rtype: SoccerPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOCCERPLAYER_TYPE_URI,
        rdf_type_name=SOCCERPLAYER_TYPE_NAME, 
        kls=SoccerPlayer)
