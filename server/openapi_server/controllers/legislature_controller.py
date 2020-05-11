import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LEGISLATURE_TYPE_NAME, LEGISLATURE_TYPE_URI

from openapi_server.models.legislature import Legislature  # noqa: E501
from openapi_server import util

def legislatures_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Legislature

    Gets a list of all instances of Legislature (more information in http://dbpedia.org/ontology/Legislature) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Legislature]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LEGISLATURE_TYPE_URI,
        rdf_type_name=LEGISLATURE_TYPE_NAME, 
        kls=Legislature)

def legislatures_id_get(id):  # noqa: E501
    """Get a single Legislature by its id

    Gets the details of a given Legislature (more information in http://dbpedia.org/ontology/Legislature) # noqa: E501

    :param id: The ID of the Legislature to be retrieved
    :type id: str

    :rtype: Legislature
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LEGISLATURE_TYPE_URI,
        rdf_type_name=LEGISLATURE_TYPE_NAME, 
        kls=Legislature)
