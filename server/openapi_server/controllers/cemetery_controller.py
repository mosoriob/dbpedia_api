import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CEMETERY_TYPE_NAME, CEMETERY_TYPE_URI

from openapi_server.models.cemetery import Cemetery  # noqa: E501
from openapi_server import util

def cemeterys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Cemetery

    Gets a list of all instances of Cemetery (more information in http://dbpedia.org/ontology/Cemetery) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Cemetery]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CEMETERY_TYPE_URI,
        rdf_type_name=CEMETERY_TYPE_NAME, 
        kls=Cemetery)

def cemeterys_id_get(id):  # noqa: E501
    """Get a single Cemetery by its id

    Gets the details of a given Cemetery (more information in http://dbpedia.org/ontology/Cemetery) # noqa: E501

    :param id: The ID of the Cemetery to be retrieved
    :type id: str

    :rtype: Cemetery
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CEMETERY_TYPE_URI,
        rdf_type_name=CEMETERY_TYPE_NAME, 
        kls=Cemetery)
