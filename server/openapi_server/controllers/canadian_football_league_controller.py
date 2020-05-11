import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CANADIANFOOTBALLLEAGUE_TYPE_NAME, CANADIANFOOTBALLLEAGUE_TYPE_URI

from openapi_server.models.canadian_football_league import CanadianFootballLeague  # noqa: E501
from openapi_server import util

def canadianfootballleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CanadianFootballLeague

    Gets a list of all instances of CanadianFootballLeague (more information in http://dbpedia.org/ontology/CanadianFootballLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CanadianFootballLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CANADIANFOOTBALLLEAGUE_TYPE_URI,
        rdf_type_name=CANADIANFOOTBALLLEAGUE_TYPE_NAME, 
        kls=CanadianFootballLeague)

def canadianfootballleagues_id_get(id):  # noqa: E501
    """Get a single CanadianFootballLeague by its id

    Gets the details of a given CanadianFootballLeague (more information in http://dbpedia.org/ontology/CanadianFootballLeague) # noqa: E501

    :param id: The ID of the CanadianFootballLeague to be retrieved
    :type id: str

    :rtype: CanadianFootballLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CANADIANFOOTBALLLEAGUE_TYPE_URI,
        rdf_type_name=CANADIANFOOTBALLLEAGUE_TYPE_NAME, 
        kls=CanadianFootballLeague)
