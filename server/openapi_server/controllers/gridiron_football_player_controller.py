import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GRIDIRONFOOTBALLPLAYER_TYPE_NAME, GRIDIRONFOOTBALLPLAYER_TYPE_URI

from openapi_server.models.gridiron_football_player import GridironFootballPlayer  # noqa: E501
from openapi_server import util

def gridironfootballplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GridironFootballPlayer

    Gets a list of all instances of GridironFootballPlayer (more information in http://dbpedia.org/ontology/GridironFootballPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GridironFootballPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GRIDIRONFOOTBALLPLAYER_TYPE_URI,
        rdf_type_name=GRIDIRONFOOTBALLPLAYER_TYPE_NAME, 
        kls=GridironFootballPlayer)

def gridironfootballplayers_id_get(id):  # noqa: E501
    """Get a single GridironFootballPlayer by its id

    Gets the details of a given GridironFootballPlayer (more information in http://dbpedia.org/ontology/GridironFootballPlayer) # noqa: E501

    :param id: The ID of the GridironFootballPlayer to be retrieved
    :type id: str

    :rtype: GridironFootballPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GRIDIRONFOOTBALLPLAYER_TYPE_URI,
        rdf_type_name=GRIDIRONFOOTBALLPLAYER_TYPE_NAME, 
        kls=GridironFootballPlayer)
