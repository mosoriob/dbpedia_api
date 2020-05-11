import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RUGBYPLAYER_TYPE_NAME, RUGBYPLAYER_TYPE_URI

from openapi_server.models.rugby_player import RugbyPlayer  # noqa: E501
from openapi_server import util

def rugbyplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RugbyPlayer

    Gets a list of all instances of RugbyPlayer (more information in http://dbpedia.org/ontology/RugbyPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RugbyPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RUGBYPLAYER_TYPE_URI,
        rdf_type_name=RUGBYPLAYER_TYPE_NAME, 
        kls=RugbyPlayer)

def rugbyplayers_id_get(id):  # noqa: E501
    """Get a single RugbyPlayer by its id

    Gets the details of a given RugbyPlayer (more information in http://dbpedia.org/ontology/RugbyPlayer) # noqa: E501

    :param id: The ID of the RugbyPlayer to be retrieved
    :type id: str

    :rtype: RugbyPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RUGBYPLAYER_TYPE_URI,
        rdf_type_name=RUGBYPLAYER_TYPE_NAME, 
        kls=RugbyPlayer)
