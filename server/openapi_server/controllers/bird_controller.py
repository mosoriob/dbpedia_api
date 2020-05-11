import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BIRD_TYPE_NAME, BIRD_TYPE_URI

from openapi_server.models.bird import Bird  # noqa: E501
from openapi_server import util

def birds_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Bird

    Gets a list of all instances of Bird (more information in http://dbpedia.org/ontology/Bird) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Bird]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BIRD_TYPE_URI,
        rdf_type_name=BIRD_TYPE_NAME, 
        kls=Bird)

def birds_id_get(id):  # noqa: E501
    """Get a single Bird by its id

    Gets the details of a given Bird (more information in http://dbpedia.org/ontology/Bird) # noqa: E501

    :param id: The ID of the Bird to be retrieved
    :type id: str

    :rtype: Bird
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BIRD_TYPE_URI,
        rdf_type_name=BIRD_TYPE_NAME, 
        kls=Bird)
