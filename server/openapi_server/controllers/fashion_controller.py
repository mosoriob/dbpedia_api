import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FASHION_TYPE_NAME, FASHION_TYPE_URI

from openapi_server.models.fashion import Fashion  # noqa: E501
from openapi_server import util

def fashions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Fashion

    Gets a list of all instances of Fashion (more information in http://dbpedia.org/ontology/Fashion) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Fashion]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FASHION_TYPE_URI,
        rdf_type_name=FASHION_TYPE_NAME, 
        kls=Fashion)

def fashions_id_get(id):  # noqa: E501
    """Get a single Fashion by its id

    Gets the details of a given Fashion (more information in http://dbpedia.org/ontology/Fashion) # noqa: E501

    :param id: The ID of the Fashion to be retrieved
    :type id: str

    :rtype: Fashion
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FASHION_TYPE_URI,
        rdf_type_name=FASHION_TYPE_NAME, 
        kls=Fashion)
