import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FOOD_TYPE_NAME, FOOD_TYPE_URI

from openapi_server.models.food import Food  # noqa: E501
from openapi_server import util

def foods_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Food

    Gets a list of all instances of Food (more information in http://dbpedia.org/ontology/Food) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Food]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FOOD_TYPE_URI,
        rdf_type_name=FOOD_TYPE_NAME, 
        kls=Food)

def foods_id_get(id):  # noqa: E501
    """Get a single Food by its id

    Gets the details of a given Food (more information in http://dbpedia.org/ontology/Food) # noqa: E501

    :param id: The ID of the Food to be retrieved
    :type id: str

    :rtype: Food
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FOOD_TYPE_URI,
        rdf_type_name=FOOD_TYPE_NAME, 
        kls=Food)
