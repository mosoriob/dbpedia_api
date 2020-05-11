import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SNOOKERPLAYER_TYPE_NAME, SNOOKERPLAYER_TYPE_URI

from openapi_server.models.snooker_player import SnookerPlayer  # noqa: E501
from openapi_server import util

def snookerplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SnookerPlayer

    Gets a list of all instances of SnookerPlayer (more information in http://dbpedia.org/ontology/SnookerPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SnookerPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SNOOKERPLAYER_TYPE_URI,
        rdf_type_name=SNOOKERPLAYER_TYPE_NAME, 
        kls=SnookerPlayer)

def snookerplayers_id_get(id):  # noqa: E501
    """Get a single SnookerPlayer by its id

    Gets the details of a given SnookerPlayer (more information in http://dbpedia.org/ontology/SnookerPlayer) # noqa: E501

    :param id: The ID of the SnookerPlayer to be retrieved
    :type id: str

    :rtype: SnookerPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SNOOKERPLAYER_TYPE_URI,
        rdf_type_name=SNOOKERPLAYER_TYPE_NAME, 
        kls=SnookerPlayer)
