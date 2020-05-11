import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GOLFPLAYER_TYPE_NAME, GOLFPLAYER_TYPE_URI

from openapi_server.models.golf_player import GolfPlayer  # noqa: E501
from openapi_server import util

def golfplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GolfPlayer

    Gets a list of all instances of GolfPlayer (more information in http://dbpedia.org/ontology/GolfPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GolfPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GOLFPLAYER_TYPE_URI,
        rdf_type_name=GOLFPLAYER_TYPE_NAME, 
        kls=GolfPlayer)

def golfplayers_id_get(id):  # noqa: E501
    """Get a single GolfPlayer by its id

    Gets the details of a given GolfPlayer (more information in http://dbpedia.org/ontology/GolfPlayer) # noqa: E501

    :param id: The ID of the GolfPlayer to be retrieved
    :type id: str

    :rtype: GolfPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GOLFPLAYER_TYPE_URI,
        rdf_type_name=GOLFPLAYER_TYPE_NAME, 
        kls=GolfPlayer)
