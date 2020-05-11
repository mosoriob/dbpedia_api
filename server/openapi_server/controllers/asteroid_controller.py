import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ASTEROID_TYPE_NAME, ASTEROID_TYPE_URI

from openapi_server.models.asteroid import Asteroid  # noqa: E501
from openapi_server import util

def asteroids_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Asteroid

    Gets a list of all instances of Asteroid (more information in http://dbpedia.org/ontology/Asteroid) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Asteroid]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ASTEROID_TYPE_URI,
        rdf_type_name=ASTEROID_TYPE_NAME, 
        kls=Asteroid)

def asteroids_id_get(id):  # noqa: E501
    """Get a single Asteroid by its id

    Gets the details of a given Asteroid (more information in http://dbpedia.org/ontology/Asteroid) # noqa: E501

    :param id: The ID of the Asteroid to be retrieved
    :type id: str

    :rtype: Asteroid
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ASTEROID_TYPE_URI,
        rdf_type_name=ASTEROID_TYPE_NAME, 
        kls=Asteroid)
