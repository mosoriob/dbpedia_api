import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BEVERAGE_TYPE_NAME, BEVERAGE_TYPE_URI

from openapi_server.models.beverage import Beverage  # noqa: E501
from openapi_server import util

def beverages_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Beverage

    Gets a list of all instances of Beverage (more information in http://dbpedia.org/ontology/Beverage) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Beverage]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BEVERAGE_TYPE_URI,
        rdf_type_name=BEVERAGE_TYPE_NAME, 
        kls=Beverage)

def beverages_id_get(id):  # noqa: E501
    """Get a single Beverage by its id

    Gets the details of a given Beverage (more information in http://dbpedia.org/ontology/Beverage) # noqa: E501

    :param id: The ID of the Beverage to be retrieved
    :type id: str

    :rtype: Beverage
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BEVERAGE_TYPE_URI,
        rdf_type_name=BEVERAGE_TYPE_NAME, 
        kls=Beverage)
