import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARCHIPELAGO_TYPE_NAME, ARCHIPELAGO_TYPE_URI

from openapi_server.models.archipelago import Archipelago  # noqa: E501
from openapi_server import util

def archipelagos_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Archipelago

    Gets a list of all instances of Archipelago (more information in http://dbpedia.org/ontology/Archipelago) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Archipelago]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARCHIPELAGO_TYPE_URI,
        rdf_type_name=ARCHIPELAGO_TYPE_NAME, 
        kls=Archipelago)

def archipelagos_id_get(id):  # noqa: E501
    """Get a single Archipelago by its id

    Gets the details of a given Archipelago (more information in http://dbpedia.org/ontology/Archipelago) # noqa: E501

    :param id: The ID of the Archipelago to be retrieved
    :type id: str

    :rtype: Archipelago
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARCHIPELAGO_TYPE_URI,
        rdf_type_name=ARCHIPELAGO_TYPE_NAME, 
        kls=Archipelago)
