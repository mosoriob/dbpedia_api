import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPEEDWAYTEAM_TYPE_NAME, SPEEDWAYTEAM_TYPE_URI

from openapi_server.models.speedway_team import SpeedwayTeam  # noqa: E501
from openapi_server import util

def speedwayteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SpeedwayTeam

    Gets a list of all instances of SpeedwayTeam (more information in http://dbpedia.org/ontology/SpeedwayTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SpeedwayTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPEEDWAYTEAM_TYPE_URI,
        rdf_type_name=SPEEDWAYTEAM_TYPE_NAME, 
        kls=SpeedwayTeam)

def speedwayteams_id_get(id):  # noqa: E501
    """Get a single SpeedwayTeam by its id

    Gets the details of a given SpeedwayTeam (more information in http://dbpedia.org/ontology/SpeedwayTeam) # noqa: E501

    :param id: The ID of the SpeedwayTeam to be retrieved
    :type id: str

    :rtype: SpeedwayTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPEEDWAYTEAM_TYPE_URI,
        rdf_type_name=SPEEDWAYTEAM_TYPE_NAME, 
        kls=SpeedwayTeam)
