import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHEF_TYPE_NAME, CHEF_TYPE_URI

from openapi_server.models.chef import Chef  # noqa: E501
from openapi_server import util

def chefs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Chef

    Gets a list of all instances of Chef (more information in http://dbpedia.org/ontology/Chef) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Chef]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHEF_TYPE_URI,
        rdf_type_name=CHEF_TYPE_NAME, 
        kls=Chef)

def chefs_id_get(id):  # noqa: E501
    """Get a single Chef by its id

    Gets the details of a given Chef (more information in http://dbpedia.org/ontology/Chef) # noqa: E501

    :param id: The ID of the Chef to be retrieved
    :type id: str

    :rtype: Chef
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHEF_TYPE_URI,
        rdf_type_name=CHEF_TYPE_NAME, 
        kls=Chef)
