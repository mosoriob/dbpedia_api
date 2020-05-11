import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ATHLETICSPLAYER_TYPE_NAME, ATHLETICSPLAYER_TYPE_URI

from openapi_server.models.athletics_player import AthleticsPlayer  # noqa: E501
from openapi_server import util

def athleticsplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AthleticsPlayer

    Gets a list of all instances of AthleticsPlayer (more information in http://dbpedia.org/ontology/AthleticsPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AthleticsPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ATHLETICSPLAYER_TYPE_URI,
        rdf_type_name=ATHLETICSPLAYER_TYPE_NAME, 
        kls=AthleticsPlayer)

def athleticsplayers_id_get(id):  # noqa: E501
    """Get a single AthleticsPlayer by its id

    Gets the details of a given AthleticsPlayer (more information in http://dbpedia.org/ontology/AthleticsPlayer) # noqa: E501

    :param id: The ID of the AthleticsPlayer to be retrieved
    :type id: str

    :rtype: AthleticsPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ATHLETICSPLAYER_TYPE_URI,
        rdf_type_name=ATHLETICSPLAYER_TYPE_NAME, 
        kls=AthleticsPlayer)
