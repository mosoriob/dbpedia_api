import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOCCERCLUBSEASON_TYPE_NAME, SOCCERCLUBSEASON_TYPE_URI

from openapi_server.models.soccer_club_season import SoccerClubSeason  # noqa: E501
from openapi_server import util

def soccerclubseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoccerClubSeason

    Gets a list of all instances of SoccerClubSeason (more information in http://dbpedia.org/ontology/SoccerClubSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoccerClubSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOCCERCLUBSEASON_TYPE_URI,
        rdf_type_name=SOCCERCLUBSEASON_TYPE_NAME, 
        kls=SoccerClubSeason)

def soccerclubseasons_id_get(id):  # noqa: E501
    """Get a single SoccerClubSeason by its id

    Gets the details of a given SoccerClubSeason (more information in http://dbpedia.org/ontology/SoccerClubSeason) # noqa: E501

    :param id: The ID of the SoccerClubSeason to be retrieved
    :type id: str

    :rtype: SoccerClubSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOCCERCLUBSEASON_TYPE_URI,
        rdf_type_name=SOCCERCLUBSEASON_TYPE_NAME, 
        kls=SoccerClubSeason)
