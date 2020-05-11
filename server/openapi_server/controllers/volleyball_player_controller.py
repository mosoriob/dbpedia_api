import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VOLLEYBALLPLAYER_TYPE_NAME, VOLLEYBALLPLAYER_TYPE_URI

from openapi_server.models.volleyball_player import VolleyballPlayer  # noqa: E501
from openapi_server import util

def volleyballplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of VolleyballPlayer

    Gets a list of all instances of VolleyballPlayer (more information in http://dbpedia.org/ontology/VolleyballPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[VolleyballPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VOLLEYBALLPLAYER_TYPE_URI,
        rdf_type_name=VOLLEYBALLPLAYER_TYPE_NAME, 
        kls=VolleyballPlayer)

def volleyballplayers_id_get(id):  # noqa: E501
    """Get a single VolleyballPlayer by its id

    Gets the details of a given VolleyballPlayer (more information in http://dbpedia.org/ontology/VolleyballPlayer) # noqa: E501

    :param id: The ID of the VolleyballPlayer to be retrieved
    :type id: str

    :rtype: VolleyballPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VOLLEYBALLPLAYER_TYPE_URI,
        rdf_type_name=VOLLEYBALLPLAYER_TYPE_NAME, 
        kls=VolleyballPlayer)
