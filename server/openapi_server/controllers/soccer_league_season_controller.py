import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOCCERLEAGUESEASON_TYPE_NAME, SOCCERLEAGUESEASON_TYPE_URI

from openapi_server.models.soccer_league_season import SoccerLeagueSeason  # noqa: E501
from openapi_server import util

def soccerleagueseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoccerLeagueSeason

    Gets a list of all instances of SoccerLeagueSeason (more information in http://dbpedia.org/ontology/SoccerLeagueSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoccerLeagueSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOCCERLEAGUESEASON_TYPE_URI,
        rdf_type_name=SOCCERLEAGUESEASON_TYPE_NAME, 
        kls=SoccerLeagueSeason)

def soccerleagueseasons_id_get(id):  # noqa: E501
    """Get a single SoccerLeagueSeason by its id

    Gets the details of a given SoccerLeagueSeason (more information in http://dbpedia.org/ontology/SoccerLeagueSeason) # noqa: E501

    :param id: The ID of the SoccerLeagueSeason to be retrieved
    :type id: str

    :rtype: SoccerLeagueSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOCCERLEAGUESEASON_TYPE_URI,
        rdf_type_name=SOCCERLEAGUESEASON_TYPE_NAME, 
        kls=SoccerLeagueSeason)
