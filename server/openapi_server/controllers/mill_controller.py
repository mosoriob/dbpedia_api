import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MILL_TYPE_NAME, MILL_TYPE_URI

from openapi_server.models.mill import Mill  # noqa: E501
from openapi_server import util

def mills_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Mill

    Gets a list of all instances of Mill (more information in http://dbpedia.org/ontology/Mill) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Mill]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MILL_TYPE_URI,
        rdf_type_name=MILL_TYPE_NAME, 
        kls=Mill)

def mills_id_get(id):  # noqa: E501
    """Get a single Mill by its id

    Gets the details of a given Mill (more information in http://dbpedia.org/ontology/Mill) # noqa: E501

    :param id: The ID of the Mill to be retrieved
    :type id: str

    :rtype: Mill
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MILL_TYPE_URI,
        rdf_type_name=MILL_TYPE_NAME, 
        kls=Mill)
