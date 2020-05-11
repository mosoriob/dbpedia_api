import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AUSTRALIANFOOTBALLLEAGUE_TYPE_NAME, AUSTRALIANFOOTBALLLEAGUE_TYPE_URI

from openapi_server.models.australian_football_league import AustralianFootballLeague  # noqa: E501
from openapi_server import util

def australianfootballleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AustralianFootballLeague

    Gets a list of all instances of AustralianFootballLeague (more information in http://dbpedia.org/ontology/AustralianFootballLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AustralianFootballLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AUSTRALIANFOOTBALLLEAGUE_TYPE_URI,
        rdf_type_name=AUSTRALIANFOOTBALLLEAGUE_TYPE_NAME, 
        kls=AustralianFootballLeague)

def australianfootballleagues_id_get(id):  # noqa: E501
    """Get a single AustralianFootballLeague by its id

    Gets the details of a given AustralianFootballLeague (more information in http://dbpedia.org/ontology/AustralianFootballLeague) # noqa: E501

    :param id: The ID of the AustralianFootballLeague to be retrieved
    :type id: str

    :rtype: AustralianFootballLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AUSTRALIANFOOTBALLLEAGUE_TYPE_URI,
        rdf_type_name=AUSTRALIANFOOTBALLLEAGUE_TYPE_NAME, 
        kls=AustralianFootballLeague)
