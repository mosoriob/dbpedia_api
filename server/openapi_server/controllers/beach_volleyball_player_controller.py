import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BEACHVOLLEYBALLPLAYER_TYPE_NAME, BEACHVOLLEYBALLPLAYER_TYPE_URI

from openapi_server.models.beach_volleyball_player import BeachVolleyballPlayer  # noqa: E501
from openapi_server import util

def beachvolleyballplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BeachVolleyballPlayer

    Gets a list of all instances of BeachVolleyballPlayer (more information in http://dbpedia.org/ontology/BeachVolleyballPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BeachVolleyballPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BEACHVOLLEYBALLPLAYER_TYPE_URI,
        rdf_type_name=BEACHVOLLEYBALLPLAYER_TYPE_NAME, 
        kls=BeachVolleyballPlayer)

def beachvolleyballplayers_id_get(id):  # noqa: E501
    """Get a single BeachVolleyballPlayer by its id

    Gets the details of a given BeachVolleyballPlayer (more information in http://dbpedia.org/ontology/BeachVolleyballPlayer) # noqa: E501

    :param id: The ID of the BeachVolleyballPlayer to be retrieved
    :type id: str

    :rtype: BeachVolleyballPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BEACHVOLLEYBALLPLAYER_TYPE_URI,
        rdf_type_name=BEACHVOLLEYBALLPLAYER_TYPE_NAME, 
        kls=BeachVolleyballPlayer)
