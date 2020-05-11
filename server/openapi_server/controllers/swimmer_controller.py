import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SWIMMER_TYPE_NAME, SWIMMER_TYPE_URI

from openapi_server.models.swimmer import Swimmer  # noqa: E501
from openapi_server import util

def swimmers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Swimmer

    Gets a list of all instances of Swimmer (more information in http://dbpedia.org/ontology/Swimmer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Swimmer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SWIMMER_TYPE_URI,
        rdf_type_name=SWIMMER_TYPE_NAME, 
        kls=Swimmer)

def swimmers_id_get(id):  # noqa: E501
    """Get a single Swimmer by its id

    Gets the details of a given Swimmer (more information in http://dbpedia.org/ontology/Swimmer) # noqa: E501

    :param id: The ID of the Swimmer to be retrieved
    :type id: str

    :rtype: Swimmer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SWIMMER_TYPE_URI,
        rdf_type_name=SWIMMER_TYPE_NAME, 
        kls=Swimmer)
