import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COMMUNITY_TYPE_NAME, COMMUNITY_TYPE_URI

from openapi_server.models.community import Community  # noqa: E501
from openapi_server import util

def communitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Community

    Gets a list of all instances of Community (more information in http://dbpedia.org/ontology/Community) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Community]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COMMUNITY_TYPE_URI,
        rdf_type_name=COMMUNITY_TYPE_NAME, 
        kls=Community)

def communitys_id_get(id):  # noqa: E501
    """Get a single Community by its id

    Gets the details of a given Community (more information in http://dbpedia.org/ontology/Community) # noqa: E501

    :param id: The ID of the Community to be retrieved
    :type id: str

    :rtype: Community
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COMMUNITY_TYPE_URI,
        rdf_type_name=COMMUNITY_TYPE_NAME, 
        kls=Community)
