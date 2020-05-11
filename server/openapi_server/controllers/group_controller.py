import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GROUP_TYPE_NAME, GROUP_TYPE_URI

from openapi_server.models.group import Group  # noqa: E501
from openapi_server import util

def groups_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Group

    Gets a list of all instances of Group (more information in http://dbpedia.org/ontology/Group) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Group]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GROUP_TYPE_URI,
        rdf_type_name=GROUP_TYPE_NAME, 
        kls=Group)

def groups_id_get(id):  # noqa: E501
    """Get a single Group by its id

    Gets the details of a given Group (more information in http://dbpedia.org/ontology/Group) # noqa: E501

    :param id: The ID of the Group to be retrieved
    :type id: str

    :rtype: Group
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GROUP_TYPE_URI,
        rdf_type_name=GROUP_TYPE_NAME, 
        kls=Group)
