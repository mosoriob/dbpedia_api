import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PRIEST_TYPE_NAME, PRIEST_TYPE_URI

from openapi_server.models.priest import Priest  # noqa: E501
from openapi_server import util

def priests_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Priest

    Gets a list of all instances of Priest (more information in http://dbpedia.org/ontology/Priest) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Priest]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PRIEST_TYPE_URI,
        rdf_type_name=PRIEST_TYPE_NAME, 
        kls=Priest)

def priests_id_get(id):  # noqa: E501
    """Get a single Priest by its id

    Gets the details of a given Priest (more information in http://dbpedia.org/ontology/Priest) # noqa: E501

    :param id: The ID of the Priest to be retrieved
    :type id: str

    :rtype: Priest
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PRIEST_TYPE_URI,
        rdf_type_name=PRIEST_TYPE_NAME, 
        kls=Priest)
