import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NCAATEAMSEASON_TYPE_NAME, NCAATEAMSEASON_TYPE_URI

from openapi_server.models.ncaa_team_season import NCAATeamSeason  # noqa: E501
from openapi_server import util

def ncaateamseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NCAATeamSeason

    Gets a list of all instances of NCAATeamSeason (more information in http://dbpedia.org/ontology/NCAATeamSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NCAATeamSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NCAATEAMSEASON_TYPE_URI,
        rdf_type_name=NCAATEAMSEASON_TYPE_NAME, 
        kls=NCAATeamSeason)

def ncaateamseasons_id_get(id):  # noqa: E501
    """Get a single NCAATeamSeason by its id

    Gets the details of a given NCAATeamSeason (more information in http://dbpedia.org/ontology/NCAATeamSeason) # noqa: E501

    :param id: The ID of the NCAATeamSeason to be retrieved
    :type id: str

    :rtype: NCAATeamSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NCAATEAMSEASON_TYPE_URI,
        rdf_type_name=NCAATEAMSEASON_TYPE_NAME, 
        kls=NCAATeamSeason)
