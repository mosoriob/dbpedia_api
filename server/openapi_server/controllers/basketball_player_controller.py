import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BASKETBALLPLAYER_TYPE_NAME, BASKETBALLPLAYER_TYPE_URI

from openapi_server.models.basketball_player import BasketballPlayer  # noqa: E501
from openapi_server import util

def basketballplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BasketballPlayer

    Gets a list of all instances of BasketballPlayer (more information in http://dbpedia.org/ontology/BasketballPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BasketballPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BASKETBALLPLAYER_TYPE_URI,
        rdf_type_name=BASKETBALLPLAYER_TYPE_NAME, 
        kls=BasketballPlayer)

def basketballplayers_id_get(id):  # noqa: E501
    """Get a single BasketballPlayer by its id

    Gets the details of a given BasketballPlayer (more information in http://dbpedia.org/ontology/BasketballPlayer) # noqa: E501

    :param id: The ID of the BasketballPlayer to be retrieved
    :type id: str

    :rtype: BasketballPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BASKETBALLPLAYER_TYPE_URI,
        rdf_type_name=BASKETBALLPLAYER_TYPE_NAME, 
        kls=BasketballPlayer)
