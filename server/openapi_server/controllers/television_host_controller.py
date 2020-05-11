import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TELEVISIONHOST_TYPE_NAME, TELEVISIONHOST_TYPE_URI

from openapi_server.models.television_host import TelevisionHost  # noqa: E501
from openapi_server import util

def televisionhosts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TelevisionHost

    Gets a list of all instances of TelevisionHost (more information in http://dbpedia.org/ontology/TelevisionHost) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TelevisionHost]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TELEVISIONHOST_TYPE_URI,
        rdf_type_name=TELEVISIONHOST_TYPE_NAME, 
        kls=TelevisionHost)

def televisionhosts_id_get(id):  # noqa: E501
    """Get a single TelevisionHost by its id

    Gets the details of a given TelevisionHost (more information in http://dbpedia.org/ontology/TelevisionHost) # noqa: E501

    :param id: The ID of the TelevisionHost to be retrieved
    :type id: str

    :rtype: TelevisionHost
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TELEVISIONHOST_TYPE_URI,
        rdf_type_name=TELEVISIONHOST_TYPE_NAME, 
        kls=TelevisionHost)
