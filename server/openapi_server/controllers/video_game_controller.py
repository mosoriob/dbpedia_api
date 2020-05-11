import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VIDEOGAME_TYPE_NAME, VIDEOGAME_TYPE_URI

from openapi_server.models.video_game import VideoGame  # noqa: E501
from openapi_server import util

def videogames_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of VideoGame

    Gets a list of all instances of VideoGame (more information in http://dbpedia.org/ontology/VideoGame) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[VideoGame]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VIDEOGAME_TYPE_URI,
        rdf_type_name=VIDEOGAME_TYPE_NAME, 
        kls=VideoGame)

def videogames_id_get(id):  # noqa: E501
    """Get a single VideoGame by its id

    Gets the details of a given VideoGame (more information in http://dbpedia.org/ontology/VideoGame) # noqa: E501

    :param id: The ID of the VideoGame to be retrieved
    :type id: str

    :rtype: VideoGame
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VIDEOGAME_TYPE_URI,
        rdf_type_name=VIDEOGAME_TYPE_NAME, 
        kls=VideoGame)
