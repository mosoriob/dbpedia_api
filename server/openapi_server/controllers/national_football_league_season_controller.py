import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NATIONALFOOTBALLLEAGUESEASON_TYPE_NAME, NATIONALFOOTBALLLEAGUESEASON_TYPE_URI

from openapi_server.models.national_football_league_season import NationalFootballLeagueSeason  # noqa: E501
from openapi_server import util

def nationalfootballleagueseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NationalFootballLeagueSeason

    Gets a list of all instances of NationalFootballLeagueSeason (more information in http://dbpedia.org/ontology/NationalFootballLeagueSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NationalFootballLeagueSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NATIONALFOOTBALLLEAGUESEASON_TYPE_URI,
        rdf_type_name=NATIONALFOOTBALLLEAGUESEASON_TYPE_NAME, 
        kls=NationalFootballLeagueSeason)

def nationalfootballleagueseasons_id_get(id):  # noqa: E501
    """Get a single NationalFootballLeagueSeason by its id

    Gets the details of a given NationalFootballLeagueSeason (more information in http://dbpedia.org/ontology/NationalFootballLeagueSeason) # noqa: E501

    :param id: The ID of the NationalFootballLeagueSeason to be retrieved
    :type id: str

    :rtype: NationalFootballLeagueSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NATIONALFOOTBALLLEAGUESEASON_TYPE_URI,
        rdf_type_name=NATIONALFOOTBALLLEAGUESEASON_TYPE_NAME, 
        kls=NationalFootballLeagueSeason)
