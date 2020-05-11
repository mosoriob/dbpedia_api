import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CITY_TYPE_NAME, CITY_TYPE_URI

from openapi_server.models.city import City  # noqa: E501
from openapi_server import util

def citys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of City

    Gets a list of all instances of City (more information in http://dbpedia.org/ontology/City) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[City]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CITY_TYPE_URI,
        rdf_type_name=CITY_TYPE_NAME, 
        kls=City)

def citys_id_get(id):  # noqa: E501
    """Get a single City by its id

    Gets the details of a given City (more information in http://dbpedia.org/ontology/City) # noqa: E501

    :param id: The ID of the City to be retrieved
    :type id: str

    :rtype: City
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CITY_TYPE_URI,
        rdf_type_name=CITY_TYPE_NAME, 
        kls=City)
