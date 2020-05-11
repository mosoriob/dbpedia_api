import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SHIP_TYPE_NAME, SHIP_TYPE_URI

from openapi_server.models.ship import Ship  # noqa: E501
from openapi_server import util

def ships_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Ship

    Gets a list of all instances of Ship (more information in http://dbpedia.org/ontology/Ship) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Ship]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SHIP_TYPE_URI,
        rdf_type_name=SHIP_TYPE_NAME, 
        kls=Ship)

def ships_id_get(id):  # noqa: E501
    """Get a single Ship by its id

    Gets the details of a given Ship (more information in http://dbpedia.org/ontology/Ship) # noqa: E501

    :param id: The ID of the Ship to be retrieved
    :type id: str

    :rtype: Ship
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SHIP_TYPE_URI,
        rdf_type_name=SHIP_TYPE_NAME, 
        kls=Ship)
