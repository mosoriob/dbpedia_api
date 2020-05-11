import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BASEBALLTEAM_TYPE_NAME, BASEBALLTEAM_TYPE_URI

from openapi_server.models.baseball_team import BaseballTeam  # noqa: E501
from openapi_server import util

def baseballteams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BaseballTeam

    Gets a list of all instances of BaseballTeam (more information in http://dbpedia.org/ontology/BaseballTeam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BaseballTeam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BASEBALLTEAM_TYPE_URI,
        rdf_type_name=BASEBALLTEAM_TYPE_NAME, 
        kls=BaseballTeam)

def baseballteams_id_get(id):  # noqa: E501
    """Get a single BaseballTeam by its id

    Gets the details of a given BaseballTeam (more information in http://dbpedia.org/ontology/BaseballTeam) # noqa: E501

    :param id: The ID of the BaseballTeam to be retrieved
    :type id: str

    :rtype: BaseballTeam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BASEBALLTEAM_TYPE_URI,
        rdf_type_name=BASEBALLTEAM_TYPE_NAME, 
        kls=BaseballTeam)
