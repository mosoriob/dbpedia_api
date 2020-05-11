import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SHOPPINGMALL_TYPE_NAME, SHOPPINGMALL_TYPE_URI

from openapi_server.models.shopping_mall import ShoppingMall  # noqa: E501
from openapi_server import util

def shoppingmalls_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ShoppingMall

    Gets a list of all instances of ShoppingMall (more information in http://dbpedia.org/ontology/ShoppingMall) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ShoppingMall]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SHOPPINGMALL_TYPE_URI,
        rdf_type_name=SHOPPINGMALL_TYPE_NAME, 
        kls=ShoppingMall)

def shoppingmalls_id_get(id):  # noqa: E501
    """Get a single ShoppingMall by its id

    Gets the details of a given ShoppingMall (more information in http://dbpedia.org/ontology/ShoppingMall) # noqa: E501

    :param id: The ID of the ShoppingMall to be retrieved
    :type id: str

    :rtype: ShoppingMall
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SHOPPINGMALL_TYPE_URI,
        rdf_type_name=SHOPPINGMALL_TYPE_NAME, 
        kls=ShoppingMall)
