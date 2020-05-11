import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORT_TYPE_NAME, SPORT_TYPE_URI

from openapi_server.models.sport import Sport  # noqa: E501
from openapi_server import util

def sports_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Sport

    Gets a list of all instances of Sport (more information in http://dbpedia.org/ontology/Sport) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Sport]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORT_TYPE_URI,
        rdf_type_name=SPORT_TYPE_NAME, 
        kls=Sport)

def sports_id_get(id):  # noqa: E501
    """Get a single Sport by its id

    Gets the details of a given Sport (more information in http://dbpedia.org/ontology/Sport) # noqa: E501

    :param id: The ID of the Sport to be retrieved
    :type id: str

    :rtype: Sport
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORT_TYPE_URI,
        rdf_type_name=SPORT_TYPE_NAME, 
        kls=Sport)
