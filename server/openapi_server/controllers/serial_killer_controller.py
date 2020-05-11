import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SERIALKILLER_TYPE_NAME, SERIALKILLER_TYPE_URI

from openapi_server.models.serial_killer import SerialKiller  # noqa: E501
from openapi_server import util

def serialkillers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SerialKiller

    Gets a list of all instances of SerialKiller (more information in http://dbpedia.org/ontology/SerialKiller) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SerialKiller]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SERIALKILLER_TYPE_URI,
        rdf_type_name=SERIALKILLER_TYPE_NAME, 
        kls=SerialKiller)

def serialkillers_id_get(id):  # noqa: E501
    """Get a single SerialKiller by its id

    Gets the details of a given SerialKiller (more information in http://dbpedia.org/ontology/SerialKiller) # noqa: E501

    :param id: The ID of the SerialKiller to be retrieved
    :type id: str

    :rtype: SerialKiller
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SERIALKILLER_TYPE_URI,
        rdf_type_name=SERIALKILLER_TYPE_NAME, 
        kls=SerialKiller)
