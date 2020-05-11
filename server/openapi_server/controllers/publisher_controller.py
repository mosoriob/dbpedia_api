import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PUBLISHER_TYPE_NAME, PUBLISHER_TYPE_URI

from openapi_server.models.publisher import Publisher  # noqa: E501
from openapi_server import util

def publishers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Publisher

    Gets a list of all instances of Publisher (more information in http://dbpedia.org/ontology/Publisher) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Publisher]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PUBLISHER_TYPE_URI,
        rdf_type_name=PUBLISHER_TYPE_NAME, 
        kls=Publisher)

def publishers_id_get(id):  # noqa: E501
    """Get a single Publisher by its id

    Gets the details of a given Publisher (more information in http://dbpedia.org/ontology/Publisher) # noqa: E501

    :param id: The ID of the Publisher to be retrieved
    :type id: str

    :rtype: Publisher
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PUBLISHER_TYPE_URI,
        rdf_type_name=PUBLISHER_TYPE_NAME, 
        kls=Publisher)
