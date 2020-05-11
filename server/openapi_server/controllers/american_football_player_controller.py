import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AMERICANFOOTBALLPLAYER_TYPE_NAME, AMERICANFOOTBALLPLAYER_TYPE_URI

from openapi_server.models.american_football_player import AmericanFootballPlayer  # noqa: E501
from openapi_server import util

def americanfootballplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AmericanFootballPlayer

    Gets a list of all instances of AmericanFootballPlayer (more information in http://dbpedia.org/ontology/AmericanFootballPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AmericanFootballPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AMERICANFOOTBALLPLAYER_TYPE_URI,
        rdf_type_name=AMERICANFOOTBALLPLAYER_TYPE_NAME, 
        kls=AmericanFootballPlayer)

def americanfootballplayers_id_get(id):  # noqa: E501
    """Get a single AmericanFootballPlayer by its id

    Gets the details of a given AmericanFootballPlayer (more information in http://dbpedia.org/ontology/AmericanFootballPlayer) # noqa: E501

    :param id: The ID of the AmericanFootballPlayer to be retrieved
    :type id: str

    :rtype: AmericanFootballPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AMERICANFOOTBALLPLAYER_TYPE_URI,
        rdf_type_name=AMERICANFOOTBALLPLAYER_TYPE_NAME, 
        kls=AmericanFootballPlayer)
