import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORTSTEAMSEASON_TYPE_NAME, SPORTSTEAMSEASON_TYPE_URI

from openapi_server.models.sports_team_season import SportsTeamSeason  # noqa: E501
from openapi_server import util

def sportsteamseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SportsTeamSeason

    Gets a list of all instances of SportsTeamSeason (more information in http://dbpedia.org/ontology/SportsTeamSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SportsTeamSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORTSTEAMSEASON_TYPE_URI,
        rdf_type_name=SPORTSTEAMSEASON_TYPE_NAME, 
        kls=SportsTeamSeason)

def sportsteamseasons_id_get(id):  # noqa: E501
    """Get a single SportsTeamSeason by its id

    Gets the details of a given SportsTeamSeason (more information in http://dbpedia.org/ontology/SportsTeamSeason) # noqa: E501

    :param id: The ID of the SportsTeamSeason to be retrieved
    :type id: str

    :rtype: SportsTeamSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORTSTEAMSEASON_TYPE_URI,
        rdf_type_name=SPORTSTEAMSEASON_TYPE_NAME, 
        kls=SportsTeamSeason)
