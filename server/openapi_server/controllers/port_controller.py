import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PORT_TYPE_NAME, PORT_TYPE_URI

from openapi_server.models.port import Port  # noqa: E501
from openapi_server import util

def ports_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Port

    Gets a list of all instances of Port (more information in http://dbpedia.org/ontology/Port) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Port]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PORT_TYPE_URI,
        rdf_type_name=PORT_TYPE_NAME, 
        kls=Port)

def ports_id_get(id):  # noqa: E501
    """Get a single Port by its id

    Gets the details of a given Port (more information in http://dbpedia.org/ontology/Port) # noqa: E501

    :param id: The ID of the Port to be retrieved
    :type id: str

    :rtype: Port
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PORT_TYPE_URI,
        rdf_type_name=PORT_TYPE_NAME, 
        kls=Port)
