import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PLACE_TYPE_NAME, PLACE_TYPE_URI

from openapi_server.models.place import Place  # noqa: E501
from openapi_server import util

def places_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Place

    Gets a list of all instances of Place (more information in http://dbpedia.org/ontology/Place) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Place]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PLACE_TYPE_URI,
        rdf_type_name=PLACE_TYPE_NAME, 
        kls=Place)

def places_id_get(id):  # noqa: E501
    """Get a single Place by its id

    Gets the details of a given Place (more information in http://dbpedia.org/ontology/Place) # noqa: E501

    :param id: The ID of the Place to be retrieved
    :type id: str

    :rtype: Place
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PLACE_TYPE_URI,
        rdf_type_name=PLACE_TYPE_NAME, 
        kls=Place)
