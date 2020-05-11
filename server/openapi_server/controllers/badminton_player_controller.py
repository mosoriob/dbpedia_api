import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BADMINTONPLAYER_TYPE_NAME, BADMINTONPLAYER_TYPE_URI

from openapi_server.models.badminton_player import BadmintonPlayer  # noqa: E501
from openapi_server import util

def badmintonplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BadmintonPlayer

    Gets a list of all instances of BadmintonPlayer (more information in http://dbpedia.org/ontology/BadmintonPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BadmintonPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BADMINTONPLAYER_TYPE_URI,
        rdf_type_name=BADMINTONPLAYER_TYPE_NAME, 
        kls=BadmintonPlayer)

def badmintonplayers_id_get(id):  # noqa: E501
    """Get a single BadmintonPlayer by its id

    Gets the details of a given BadmintonPlayer (more information in http://dbpedia.org/ontology/BadmintonPlayer) # noqa: E501

    :param id: The ID of the BadmintonPlayer to be retrieved
    :type id: str

    :rtype: BadmintonPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BADMINTONPLAYER_TYPE_URI,
        rdf_type_name=BADMINTONPLAYER_TYPE_NAME, 
        kls=BadmintonPlayer)
