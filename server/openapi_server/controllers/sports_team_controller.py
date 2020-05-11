import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORTSTEAM_TYPE_NAME, SPORTSTEAM_TYPE_URI

from openapi_server.models.sports_team import SportsTeam  # noqa: E501
from openapi_server import util

def sportsteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SportsTeam

    Gets a list of all instances of SportsTeam (more information in http://dbpedia.org/ontology/SportsTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SportsTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORTSTEAM_TYPE_URI,
        rdf_type_name=SPORTSTEAM_TYPE_NAME, 
        kls=SportsTeam)

def sportsteams_id_get(id):  # noqa: E501
    """Get a single SportsTeam by its id

    Gets the details of a given SportsTeam (more information in http://dbpedia.org/ontology/SportsTeam) # noqa: E501

    :param id: The ID of the SportsTeam to be retrieved
    :type id: str

    :rtype: SportsTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORTSTEAM_TYPE_URI,
        rdf_type_name=SPORTSTEAM_TYPE_NAME, 
        kls=SportsTeam)
