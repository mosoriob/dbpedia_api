import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ATOLL_TYPE_NAME, ATOLL_TYPE_URI

from openapi_server.models.atoll import Atoll  # noqa: E501
from openapi_server import util

def atolls_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Atoll

    Gets a list of all instances of Atoll (more information in http://dbpedia.org/ontology/Atoll) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Atoll]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ATOLL_TYPE_URI,
        rdf_type_name=ATOLL_TYPE_NAME, 
        kls=Atoll)

def atolls_id_get(id):  # noqa: E501
    """Get a single Atoll by its id

    Gets the details of a given Atoll (more information in http://dbpedia.org/ontology/Atoll) # noqa: E501

    :param id: The ID of the Atoll to be retrieved
    :type id: str

    :rtype: Atoll
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ATOLL_TYPE_URI,
        rdf_type_name=ATOLL_TYPE_NAME, 
        kls=Atoll)
