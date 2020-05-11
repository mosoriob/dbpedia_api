import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HOST_TYPE_NAME, HOST_TYPE_URI

from openapi_server.models.host import Host  # noqa: E501
from openapi_server import util

def hosts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Host

    Gets a list of all instances of Host (more information in http://dbpedia.org/ontology/Host) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Host]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HOST_TYPE_URI,
        rdf_type_name=HOST_TYPE_NAME, 
        kls=Host)

def hosts_id_get(id):  # noqa: E501
    """Get a single Host by its id

    Gets the details of a given Host (more information in http://dbpedia.org/ontology/Host) # noqa: E501

    :param id: The ID of the Host to be retrieved
    :type id: str

    :rtype: Host
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HOST_TYPE_URI,
        rdf_type_name=HOST_TYPE_NAME, 
        kls=Host)
