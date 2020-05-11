import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BASEBALLPLAYER_TYPE_NAME, BASEBALLPLAYER_TYPE_URI

from openapi_server.models.baseball_player import BaseballPlayer  # noqa: E501
from openapi_server import util

def baseballplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BaseballPlayer

    Gets a list of all instances of BaseballPlayer (more information in http://dbpedia.org/ontology/BaseballPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BaseballPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BASEBALLPLAYER_TYPE_URI,
        rdf_type_name=BASEBALLPLAYER_TYPE_NAME, 
        kls=BaseballPlayer)

def baseballplayers_id_get(id):  # noqa: E501
    """Get a single BaseballPlayer by its id

    Gets the details of a given BaseballPlayer (more information in http://dbpedia.org/ontology/BaseballPlayer) # noqa: E501

    :param id: The ID of the BaseballPlayer to be retrieved
    :type id: str

    :rtype: BaseballPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BASEBALLPLAYER_TYPE_URI,
        rdf_type_name=BASEBALLPLAYER_TYPE_NAME, 
        kls=BaseballPlayer)
