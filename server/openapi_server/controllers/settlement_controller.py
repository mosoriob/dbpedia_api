import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SETTLEMENT_TYPE_NAME, SETTLEMENT_TYPE_URI

from openapi_server.models.settlement import Settlement  # noqa: E501
from openapi_server import util

def settlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Settlement

    Gets a list of all instances of Settlement (more information in http://dbpedia.org/ontology/Settlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Settlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SETTLEMENT_TYPE_URI,
        rdf_type_name=SETTLEMENT_TYPE_NAME, 
        kls=Settlement)

def settlements_id_get(id):  # noqa: E501
    """Get a single Settlement by its id

    Gets the details of a given Settlement (more information in http://dbpedia.org/ontology/Settlement) # noqa: E501

    :param id: The ID of the Settlement to be retrieved
    :type id: str

    :rtype: Settlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SETTLEMENT_TYPE_URI,
        rdf_type_name=SETTLEMENT_TYPE_NAME, 
        kls=Settlement)
