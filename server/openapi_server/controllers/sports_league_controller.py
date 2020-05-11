import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORTSLEAGUE_TYPE_NAME, SPORTSLEAGUE_TYPE_URI

from openapi_server.models.sports_league import SportsLeague  # noqa: E501
from openapi_server import util

def sportsleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SportsLeague

    Gets a list of all instances of SportsLeague (more information in http://dbpedia.org/ontology/SportsLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SportsLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORTSLEAGUE_TYPE_URI,
        rdf_type_name=SPORTSLEAGUE_TYPE_NAME, 
        kls=SportsLeague)

def sportsleagues_id_get(id):  # noqa: E501
    """Get a single SportsLeague by its id

    Gets the details of a given SportsLeague (more information in http://dbpedia.org/ontology/SportsLeague) # noqa: E501

    :param id: The ID of the SportsLeague to be retrieved
    :type id: str

    :rtype: SportsLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORTSLEAGUE_TYPE_URI,
        rdf_type_name=SPORTSLEAGUE_TYPE_NAME, 
        kls=SportsLeague)
