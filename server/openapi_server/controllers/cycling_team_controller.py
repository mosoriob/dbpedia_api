import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CYCLINGTEAM_TYPE_NAME, CYCLINGTEAM_TYPE_URI

from openapi_server.models.cycling_team import CyclingTeam  # noqa: E501
from openapi_server import util

def cyclingteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CyclingTeam

    Gets a list of all instances of CyclingTeam (more information in http://dbpedia.org/ontology/CyclingTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CyclingTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CYCLINGTEAM_TYPE_URI,
        rdf_type_name=CYCLINGTEAM_TYPE_NAME, 
        kls=CyclingTeam)

def cyclingteams_id_get(id):  # noqa: E501
    """Get a single CyclingTeam by its id

    Gets the details of a given CyclingTeam (more information in http://dbpedia.org/ontology/CyclingTeam) # noqa: E501

    :param id: The ID of the CyclingTeam to be retrieved
    :type id: str

    :rtype: CyclingTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CYCLINGTEAM_TYPE_URI,
        rdf_type_name=CYCLINGTEAM_TYPE_NAME, 
        kls=CyclingTeam)
