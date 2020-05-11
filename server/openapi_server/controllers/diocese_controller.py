import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DIOCESE_TYPE_NAME, DIOCESE_TYPE_URI

from openapi_server.models.diocese import Diocese  # noqa: E501
from openapi_server import util

def dioceses_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Diocese

    Gets a list of all instances of Diocese (more information in http://dbpedia.org/ontology/Diocese) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Diocese]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DIOCESE_TYPE_URI,
        rdf_type_name=DIOCESE_TYPE_NAME, 
        kls=Diocese)

def dioceses_id_get(id):  # noqa: E501
    """Get a single Diocese by its id

    Gets the details of a given Diocese (more information in http://dbpedia.org/ontology/Diocese) # noqa: E501

    :param id: The ID of the Diocese to be retrieved
    :type id: str

    :rtype: Diocese
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DIOCESE_TYPE_URI,
        rdf_type_name=DIOCESE_TYPE_NAME, 
        kls=Diocese)
