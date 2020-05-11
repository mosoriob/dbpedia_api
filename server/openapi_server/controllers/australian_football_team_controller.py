import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AUSTRALIANFOOTBALLTEAM_TYPE_NAME, AUSTRALIANFOOTBALLTEAM_TYPE_URI

from openapi_server.models.australian_football_team import AustralianFootballTeam  # noqa: E501
from openapi_server import util

def australianfootballteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AustralianFootballTeam

    Gets a list of all instances of AustralianFootballTeam (more information in http://dbpedia.org/ontology/AustralianFootballTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AustralianFootballTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AUSTRALIANFOOTBALLTEAM_TYPE_URI,
        rdf_type_name=AUSTRALIANFOOTBALLTEAM_TYPE_NAME, 
        kls=AustralianFootballTeam)

def australianfootballteams_id_get(id):  # noqa: E501
    """Get a single AustralianFootballTeam by its id

    Gets the details of a given AustralianFootballTeam (more information in http://dbpedia.org/ontology/AustralianFootballTeam) # noqa: E501

    :param id: The ID of the AustralianFootballTeam to be retrieved
    :type id: str

    :rtype: AustralianFootballTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AUSTRALIANFOOTBALLTEAM_TYPE_URI,
        rdf_type_name=AUSTRALIANFOOTBALLTEAM_TYPE_NAME, 
        kls=AustralianFootballTeam)
