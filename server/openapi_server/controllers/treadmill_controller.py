import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TREADMILL_TYPE_NAME, TREADMILL_TYPE_URI

from openapi_server.models.treadmill import Treadmill  # noqa: E501
from openapi_server import util

def treadmills_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Treadmill

    Gets a list of all instances of Treadmill (more information in http://dbpedia.org/ontology/Treadmill) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Treadmill]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TREADMILL_TYPE_URI,
        rdf_type_name=TREADMILL_TYPE_NAME, 
        kls=Treadmill)

def treadmills_id_get(id):  # noqa: E501
    """Get a single Treadmill by its id

    Gets the details of a given Treadmill (more information in http://dbpedia.org/ontology/Treadmill) # noqa: E501

    :param id: The ID of the Treadmill to be retrieved
    :type id: str

    :rtype: Treadmill
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TREADMILL_TYPE_URI,
        rdf_type_name=TREADMILL_TYPE_NAME, 
        kls=Treadmill)
