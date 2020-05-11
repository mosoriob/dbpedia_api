import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CASTLE_TYPE_NAME, CASTLE_TYPE_URI

from openapi_server.models.castle import Castle  # noqa: E501
from openapi_server import util

def castles_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Castle

    Gets a list of all instances of Castle (more information in http://dbpedia.org/ontology/Castle) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Castle]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CASTLE_TYPE_URI,
        rdf_type_name=CASTLE_TYPE_NAME, 
        kls=Castle)

def castles_id_get(id):  # noqa: E501
    """Get a single Castle by its id

    Gets the details of a given Castle (more information in http://dbpedia.org/ontology/Castle) # noqa: E501

    :param id: The ID of the Castle to be retrieved
    :type id: str

    :rtype: Castle
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CASTLE_TYPE_URI,
        rdf_type_name=CASTLE_TYPE_NAME, 
        kls=Castle)
