import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ICEHOCKEYPLAYER_TYPE_NAME, ICEHOCKEYPLAYER_TYPE_URI

from openapi_server.models.ice_hockey_player import IceHockeyPlayer  # noqa: E501
from openapi_server import util

def icehockeyplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of IceHockeyPlayer

    Gets a list of all instances of IceHockeyPlayer (more information in http://dbpedia.org/ontology/IceHockeyPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[IceHockeyPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ICEHOCKEYPLAYER_TYPE_URI,
        rdf_type_name=ICEHOCKEYPLAYER_TYPE_NAME, 
        kls=IceHockeyPlayer)

def icehockeyplayers_id_get(id):  # noqa: E501
    """Get a single IceHockeyPlayer by its id

    Gets the details of a given IceHockeyPlayer (more information in http://dbpedia.org/ontology/IceHockeyPlayer) # noqa: E501

    :param id: The ID of the IceHockeyPlayer to be retrieved
    :type id: str

    :rtype: IceHockeyPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ICEHOCKEYPLAYER_TYPE_URI,
        rdf_type_name=ICEHOCKEYPLAYER_TYPE_NAME, 
        kls=IceHockeyPlayer)
