import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TEAMMEMBER_TYPE_NAME, TEAMMEMBER_TYPE_URI

from openapi_server.models.team_member import TeamMember  # noqa: E501
from openapi_server import util

def teammembers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TeamMember

    Gets a list of all instances of TeamMember (more information in http://dbpedia.org/ontology/TeamMember) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TeamMember]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TEAMMEMBER_TYPE_URI,
        rdf_type_name=TEAMMEMBER_TYPE_NAME, 
        kls=TeamMember)

def teammembers_id_get(id):  # noqa: E501
    """Get a single TeamMember by its id

    Gets the details of a given TeamMember (more information in http://dbpedia.org/ontology/TeamMember) # noqa: E501

    :param id: The ID of the TeamMember to be retrieved
    :type id: str

    :rtype: TeamMember
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TEAMMEMBER_TYPE_URI,
        rdf_type_name=TEAMMEMBER_TYPE_NAME, 
        kls=TeamMember)
