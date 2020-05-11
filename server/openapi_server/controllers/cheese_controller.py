import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHEESE_TYPE_NAME, CHEESE_TYPE_URI

from openapi_server.models.cheese import Cheese  # noqa: E501
from openapi_server import util

def cheeses_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Cheese

    Gets a list of all instances of Cheese (more information in http://dbpedia.org/ontology/Cheese) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Cheese]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHEESE_TYPE_URI,
        rdf_type_name=CHEESE_TYPE_NAME, 
        kls=Cheese)

def cheeses_id_get(id):  # noqa: E501
    """Get a single Cheese by its id

    Gets the details of a given Cheese (more information in http://dbpedia.org/ontology/Cheese) # noqa: E501

    :param id: The ID of the Cheese to be retrieved
    :type id: str

    :rtype: Cheese
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHEESE_TYPE_URI,
        rdf_type_name=CHEESE_TYPE_NAME, 
        kls=Cheese)
