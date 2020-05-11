import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CANADIANFOOTBALLPLAYER_TYPE_NAME, CANADIANFOOTBALLPLAYER_TYPE_URI

from openapi_server.models.canadian_football_player import CanadianFootballPlayer  # noqa: E501
from openapi_server import util

def canadianfootballplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CanadianFootballPlayer

    Gets a list of all instances of CanadianFootballPlayer (more information in http://dbpedia.org/ontology/CanadianFootballPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CanadianFootballPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CANADIANFOOTBALLPLAYER_TYPE_URI,
        rdf_type_name=CANADIANFOOTBALLPLAYER_TYPE_NAME, 
        kls=CanadianFootballPlayer)

def canadianfootballplayers_id_get(id):  # noqa: E501
    """Get a single CanadianFootballPlayer by its id

    Gets the details of a given CanadianFootballPlayer (more information in http://dbpedia.org/ontology/CanadianFootballPlayer) # noqa: E501

    :param id: The ID of the CanadianFootballPlayer to be retrieved
    :type id: str

    :rtype: CanadianFootballPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CANADIANFOOTBALLPLAYER_TYPE_URI,
        rdf_type_name=CANADIANFOOTBALLPLAYER_TYPE_NAME, 
        kls=CanadianFootballPlayer)
