import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CAPITAL_TYPE_NAME, CAPITAL_TYPE_URI

from openapi_server.models.capital import Capital  # noqa: E501
from openapi_server import util

def capitals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Capital

    Gets a list of all instances of Capital (more information in http://dbpedia.org/ontology/Capital) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Capital]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CAPITAL_TYPE_URI,
        rdf_type_name=CAPITAL_TYPE_NAME, 
        kls=Capital)

def capitals_id_get(id):  # noqa: E501
    """Get a single Capital by its id

    Gets the details of a given Capital (more information in http://dbpedia.org/ontology/Capital) # noqa: E501

    :param id: The ID of the Capital to be retrieved
    :type id: str

    :rtype: Capital
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CAPITAL_TYPE_URI,
        rdf_type_name=CAPITAL_TYPE_NAME, 
        kls=Capital)
