import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AMERICANFOOTBALLLEAGUE_TYPE_NAME, AMERICANFOOTBALLLEAGUE_TYPE_URI

from openapi_server.models.american_football_league import AmericanFootballLeague  # noqa: E501
from openapi_server import util

def americanfootballleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AmericanFootballLeague

    Gets a list of all instances of AmericanFootballLeague (more information in http://dbpedia.org/ontology/AmericanFootballLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AmericanFootballLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AMERICANFOOTBALLLEAGUE_TYPE_URI,
        rdf_type_name=AMERICANFOOTBALLLEAGUE_TYPE_NAME, 
        kls=AmericanFootballLeague)

def americanfootballleagues_id_get(id):  # noqa: E501
    """Get a single AmericanFootballLeague by its id

    Gets the details of a given AmericanFootballLeague (more information in http://dbpedia.org/ontology/AmericanFootballLeague) # noqa: E501

    :param id: The ID of the AmericanFootballLeague to be retrieved
    :type id: str

    :rtype: AmericanFootballLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AMERICANFOOTBALLLEAGUE_TYPE_URI,
        rdf_type_name=AMERICANFOOTBALLLEAGUE_TYPE_NAME, 
        kls=AmericanFootballLeague)
