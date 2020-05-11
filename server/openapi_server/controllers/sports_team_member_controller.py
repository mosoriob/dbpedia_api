import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORTSTEAMMEMBER_TYPE_NAME, SPORTSTEAMMEMBER_TYPE_URI

from openapi_server.models.sports_team_member import SportsTeamMember  # noqa: E501
from openapi_server import util

def sportsteammembers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SportsTeamMember

    Gets a list of all instances of SportsTeamMember (more information in http://dbpedia.org/ontology/SportsTeamMember) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SportsTeamMember]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORTSTEAMMEMBER_TYPE_URI,
        rdf_type_name=SPORTSTEAMMEMBER_TYPE_NAME, 
        kls=SportsTeamMember)

def sportsteammembers_id_get(id):  # noqa: E501
    """Get a single SportsTeamMember by its id

    Gets the details of a given SportsTeamMember (more information in http://dbpedia.org/ontology/SportsTeamMember) # noqa: E501

    :param id: The ID of the SportsTeamMember to be retrieved
    :type id: str

    :rtype: SportsTeamMember
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORTSTEAMMEMBER_TYPE_URI,
        rdf_type_name=SPORTSTEAMMEMBER_TYPE_NAME, 
        kls=SportsTeamMember)
