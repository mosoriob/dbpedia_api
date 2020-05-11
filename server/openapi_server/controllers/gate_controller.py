import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GATE_TYPE_NAME, GATE_TYPE_URI

from openapi_server.models.gate import Gate  # noqa: E501
from openapi_server import util

def gates_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Gate

    Gets a list of all instances of Gate (more information in http://dbpedia.org/ontology/Gate) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Gate]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GATE_TYPE_URI,
        rdf_type_name=GATE_TYPE_NAME, 
        kls=Gate)

def gates_id_get(id):  # noqa: E501
    """Get a single Gate by its id

    Gets the details of a given Gate (more information in http://dbpedia.org/ontology/Gate) # noqa: E501

    :param id: The ID of the Gate to be retrieved
    :type id: str

    :rtype: Gate
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GATE_TYPE_URI,
        rdf_type_name=GATE_TYPE_NAME, 
        kls=Gate)
