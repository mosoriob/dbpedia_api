import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SQUASHPLAYER_TYPE_NAME, SQUASHPLAYER_TYPE_URI

from openapi_server.models.squash_player import SquashPlayer  # noqa: E501
from openapi_server import util

def squashplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SquashPlayer

    Gets a list of all instances of SquashPlayer (more information in http://dbpedia.org/ontology/SquashPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SquashPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SQUASHPLAYER_TYPE_URI,
        rdf_type_name=SQUASHPLAYER_TYPE_NAME, 
        kls=SquashPlayer)

def squashplayers_id_get(id):  # noqa: E501
    """Get a single SquashPlayer by its id

    Gets the details of a given SquashPlayer (more information in http://dbpedia.org/ontology/SquashPlayer) # noqa: E501

    :param id: The ID of the SquashPlayer to be retrieved
    :type id: str

    :rtype: SquashPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SQUASHPLAYER_TYPE_URI,
        rdf_type_name=SQUASHPLAYER_TYPE_NAME, 
        kls=SquashPlayer)
