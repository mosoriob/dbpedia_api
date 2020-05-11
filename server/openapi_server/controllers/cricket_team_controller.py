import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CRICKETTEAM_TYPE_NAME, CRICKETTEAM_TYPE_URI

from openapi_server.models.cricket_team import CricketTeam  # noqa: E501
from openapi_server import util

def cricketteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CricketTeam

    Gets a list of all instances of CricketTeam (more information in http://dbpedia.org/ontology/CricketTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CricketTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CRICKETTEAM_TYPE_URI,
        rdf_type_name=CRICKETTEAM_TYPE_NAME, 
        kls=CricketTeam)

def cricketteams_id_get(id):  # noqa: E501
    """Get a single CricketTeam by its id

    Gets the details of a given CricketTeam (more information in http://dbpedia.org/ontology/CricketTeam) # noqa: E501

    :param id: The ID of the CricketTeam to be retrieved
    :type id: str

    :rtype: CricketTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CRICKETTEAM_TYPE_URI,
        rdf_type_name=CRICKETTEAM_TYPE_NAME, 
        kls=CricketTeam)
