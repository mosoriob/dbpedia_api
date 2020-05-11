import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HANDBALLPLAYER_TYPE_NAME, HANDBALLPLAYER_TYPE_URI

from openapi_server.models.handball_player import HandballPlayer  # noqa: E501
from openapi_server import util

def handballplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HandballPlayer

    Gets a list of all instances of HandballPlayer (more information in http://dbpedia.org/ontology/HandballPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HandballPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HANDBALLPLAYER_TYPE_URI,
        rdf_type_name=HANDBALLPLAYER_TYPE_NAME, 
        kls=HandballPlayer)

def handballplayers_id_get(id):  # noqa: E501
    """Get a single HandballPlayer by its id

    Gets the details of a given HandballPlayer (more information in http://dbpedia.org/ontology/HandballPlayer) # noqa: E501

    :param id: The ID of the HandballPlayer to be retrieved
    :type id: str

    :rtype: HandballPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HANDBALLPLAYER_TYPE_URI,
        rdf_type_name=HANDBALLPLAYER_TYPE_NAME, 
        kls=HandballPlayer)
