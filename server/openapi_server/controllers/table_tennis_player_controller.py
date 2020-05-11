import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TABLETENNISPLAYER_TYPE_NAME, TABLETENNISPLAYER_TYPE_URI

from openapi_server.models.table_tennis_player import TableTennisPlayer  # noqa: E501
from openapi_server import util

def tabletennisplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TableTennisPlayer

    Gets a list of all instances of TableTennisPlayer (more information in http://dbpedia.org/ontology/TableTennisPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TableTennisPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TABLETENNISPLAYER_TYPE_URI,
        rdf_type_name=TABLETENNISPLAYER_TYPE_NAME, 
        kls=TableTennisPlayer)

def tabletennisplayers_id_get(id):  # noqa: E501
    """Get a single TableTennisPlayer by its id

    Gets the details of a given TableTennisPlayer (more information in http://dbpedia.org/ontology/TableTennisPlayer) # noqa: E501

    :param id: The ID of the TableTennisPlayer to be retrieved
    :type id: str

    :rtype: TableTennisPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TABLETENNISPLAYER_TYPE_URI,
        rdf_type_name=TABLETENNISPLAYER_TYPE_NAME, 
        kls=TableTennisPlayer)
