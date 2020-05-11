import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RADIOHOST_TYPE_NAME, RADIOHOST_TYPE_URI

from openapi_server.models.radio_host import RadioHost  # noqa: E501
from openapi_server import util

def radiohosts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RadioHost

    Gets a list of all instances of RadioHost (more information in http://dbpedia.org/ontology/RadioHost) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RadioHost]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RADIOHOST_TYPE_URI,
        rdf_type_name=RADIOHOST_TYPE_NAME, 
        kls=RadioHost)

def radiohosts_id_get(id):  # noqa: E501
    """Get a single RadioHost by its id

    Gets the details of a given RadioHost (more information in http://dbpedia.org/ontology/RadioHost) # noqa: E501

    :param id: The ID of the RadioHost to be retrieved
    :type id: str

    :rtype: RadioHost
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RADIOHOST_TYPE_URI,
        rdf_type_name=RADIOHOST_TYPE_NAME, 
        kls=RadioHost)
