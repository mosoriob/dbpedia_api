import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CANADIANFOOTBALLTEAM_TYPE_NAME, CANADIANFOOTBALLTEAM_TYPE_URI

from openapi_server.models.canadian_football_team import CanadianFootballTeam  # noqa: E501
from openapi_server import util

def canadianfootballteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CanadianFootballTeam

    Gets a list of all instances of CanadianFootballTeam (more information in http://dbpedia.org/ontology/CanadianFootballTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CanadianFootballTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CANADIANFOOTBALLTEAM_TYPE_URI,
        rdf_type_name=CANADIANFOOTBALLTEAM_TYPE_NAME, 
        kls=CanadianFootballTeam)

def canadianfootballteams_id_get(id):  # noqa: E501
    """Get a single CanadianFootballTeam by its id

    Gets the details of a given CanadianFootballTeam (more information in http://dbpedia.org/ontology/CanadianFootballTeam) # noqa: E501

    :param id: The ID of the CanadianFootballTeam to be retrieved
    :type id: str

    :rtype: CanadianFootballTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CANADIANFOOTBALLTEAM_TYPE_URI,
        rdf_type_name=CANADIANFOOTBALLTEAM_TYPE_NAME, 
        kls=CanadianFootballTeam)
