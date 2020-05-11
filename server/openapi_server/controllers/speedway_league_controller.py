import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPEEDWAYLEAGUE_TYPE_NAME, SPEEDWAYLEAGUE_TYPE_URI

from openapi_server.models.speedway_league import SpeedwayLeague  # noqa: E501
from openapi_server import util

def speedwayleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SpeedwayLeague

    Gets a list of all instances of SpeedwayLeague (more information in http://dbpedia.org/ontology/SpeedwayLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SpeedwayLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPEEDWAYLEAGUE_TYPE_URI,
        rdf_type_name=SPEEDWAYLEAGUE_TYPE_NAME, 
        kls=SpeedwayLeague)

def speedwayleagues_id_get(id):  # noqa: E501
    """Get a single SpeedwayLeague by its id

    Gets the details of a given SpeedwayLeague (more information in http://dbpedia.org/ontology/SpeedwayLeague) # noqa: E501

    :param id: The ID of the SpeedwayLeague to be retrieved
    :type id: str

    :rtype: SpeedwayLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPEEDWAYLEAGUE_TYPE_URI,
        rdf_type_name=SPEEDWAYLEAGUE_TYPE_NAME, 
        kls=SpeedwayLeague)
