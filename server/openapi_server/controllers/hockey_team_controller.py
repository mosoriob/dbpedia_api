import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HOCKEYTEAM_TYPE_NAME, HOCKEYTEAM_TYPE_URI

from openapi_server.models.hockey_team import HockeyTeam  # noqa: E501
from openapi_server import util

def hockeyteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HockeyTeam

    Gets a list of all instances of HockeyTeam (more information in http://dbpedia.org/ontology/HockeyTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HockeyTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HOCKEYTEAM_TYPE_URI,
        rdf_type_name=HOCKEYTEAM_TYPE_NAME, 
        kls=HockeyTeam)

def hockeyteams_id_get(id):  # noqa: E501
    """Get a single HockeyTeam by its id

    Gets the details of a given HockeyTeam (more information in http://dbpedia.org/ontology/HockeyTeam) # noqa: E501

    :param id: The ID of the HockeyTeam to be retrieved
    :type id: str

    :rtype: HockeyTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HOCKEYTEAM_TYPE_URI,
        rdf_type_name=HOCKEYTEAM_TYPE_NAME, 
        kls=HockeyTeam)
