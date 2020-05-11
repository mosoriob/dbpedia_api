import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RESTAURANT_TYPE_NAME, RESTAURANT_TYPE_URI

from openapi_server.models.restaurant import Restaurant  # noqa: E501
from openapi_server import util

def restaurants_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Restaurant

    Gets a list of all instances of Restaurant (more information in http://dbpedia.org/ontology/Restaurant) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Restaurant]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RESTAURANT_TYPE_URI,
        rdf_type_name=RESTAURANT_TYPE_NAME, 
        kls=Restaurant)

def restaurants_id_get(id):  # noqa: E501
    """Get a single Restaurant by its id

    Gets the details of a given Restaurant (more information in http://dbpedia.org/ontology/Restaurant) # noqa: E501

    :param id: The ID of the Restaurant to be retrieved
    :type id: str

    :rtype: Restaurant
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RESTAURANT_TYPE_URI,
        rdf_type_name=RESTAURANT_TYPE_NAME, 
        kls=Restaurant)
