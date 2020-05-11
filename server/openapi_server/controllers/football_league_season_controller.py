import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FOOTBALLLEAGUESEASON_TYPE_NAME, FOOTBALLLEAGUESEASON_TYPE_URI

from openapi_server.models.football_league_season import FootballLeagueSeason  # noqa: E501
from openapi_server import util

def footballleagueseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FootballLeagueSeason

    Gets a list of all instances of FootballLeagueSeason (more information in http://dbpedia.org/ontology/FootballLeagueSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FootballLeagueSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FOOTBALLLEAGUESEASON_TYPE_URI,
        rdf_type_name=FOOTBALLLEAGUESEASON_TYPE_NAME, 
        kls=FootballLeagueSeason)

def footballleagueseasons_id_get(id):  # noqa: E501
    """Get a single FootballLeagueSeason by its id

    Gets the details of a given FootballLeagueSeason (more information in http://dbpedia.org/ontology/FootballLeagueSeason) # noqa: E501

    :param id: The ID of the FootballLeagueSeason to be retrieved
    :type id: str

    :rtype: FootballLeagueSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FOOTBALLLEAGUESEASON_TYPE_URI,
        rdf_type_name=FOOTBALLLEAGUESEASON_TYPE_NAME, 
        kls=FootballLeagueSeason)
