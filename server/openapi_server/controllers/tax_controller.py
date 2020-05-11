import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TAX_TYPE_NAME, TAX_TYPE_URI

from openapi_server.models.tax import Tax  # noqa: E501
from openapi_server import util

def taxs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Tax

    Gets a list of all instances of Tax (more information in http://dbpedia.org/ontology/Tax) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Tax]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TAX_TYPE_URI,
        rdf_type_name=TAX_TYPE_NAME, 
        kls=Tax)

def taxs_id_get(id):  # noqa: E501
    """Get a single Tax by its id

    Gets the details of a given Tax (more information in http://dbpedia.org/ontology/Tax) # noqa: E501

    :param id: The ID of the Tax to be retrieved
    :type id: str

    :rtype: Tax
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TAX_TYPE_URI,
        rdf_type_name=TAX_TYPE_NAME, 
        kls=Tax)
