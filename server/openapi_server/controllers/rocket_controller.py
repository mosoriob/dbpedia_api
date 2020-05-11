import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ROCKET_TYPE_NAME, ROCKET_TYPE_URI

from openapi_server.models.rocket import Rocket  # noqa: E501
from openapi_server import util

def rockets_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Rocket

    Gets a list of all instances of Rocket (more information in http://dbpedia.org/ontology/Rocket) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Rocket]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ROCKET_TYPE_URI,
        rdf_type_name=ROCKET_TYPE_NAME, 
        kls=Rocket)

def rockets_id_get(id):  # noqa: E501
    """Get a single Rocket by its id

    Gets the details of a given Rocket (more information in http://dbpedia.org/ontology/Rocket) # noqa: E501

    :param id: The ID of the Rocket to be retrieved
    :type id: str

    :rtype: Rocket
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ROCKET_TYPE_URI,
        rdf_type_name=ROCKET_TYPE_NAME, 
        kls=Rocket)
