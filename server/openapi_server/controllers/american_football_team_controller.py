import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AMERICANFOOTBALLTEAM_TYPE_NAME, AMERICANFOOTBALLTEAM_TYPE_URI

from openapi_server.models.american_football_team import AmericanFootballTeam  # noqa: E501
from openapi_server import util

def americanfootballteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AmericanFootballTeam

    Gets a list of all instances of AmericanFootballTeam (more information in http://dbpedia.org/ontology/AmericanFootballTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AmericanFootballTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AMERICANFOOTBALLTEAM_TYPE_URI,
        rdf_type_name=AMERICANFOOTBALLTEAM_TYPE_NAME, 
        kls=AmericanFootballTeam)

def americanfootballteams_id_get(id):  # noqa: E501
    """Get a single AmericanFootballTeam by its id

    Gets the details of a given AmericanFootballTeam (more information in http://dbpedia.org/ontology/AmericanFootballTeam) # noqa: E501

    :param id: The ID of the AmericanFootballTeam to be retrieved
    :type id: str

    :rtype: AmericanFootballTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AMERICANFOOTBALLTEAM_TYPE_URI,
        rdf_type_name=AMERICANFOOTBALLTEAM_TYPE_NAME, 
        kls=AmericanFootballTeam)
