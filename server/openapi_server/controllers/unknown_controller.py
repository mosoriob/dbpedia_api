import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import UNKNOWN_TYPE_NAME, UNKNOWN_TYPE_URI

from openapi_server.models.unknown import Unknown  # noqa: E501
from openapi_server import util

def unknowns_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Unknown

    Gets a list of all instances of Unknown (more information in http://dbpedia.org/ontology/Unknown) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Unknown]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=UNKNOWN_TYPE_URI,
        rdf_type_name=UNKNOWN_TYPE_NAME, 
        kls=Unknown)

def unknowns_id_get(id):  # noqa: E501
    """Get a single Unknown by its id

    Gets the details of a given Unknown (more information in http://dbpedia.org/ontology/Unknown) # noqa: E501

    :param id: The ID of the Unknown to be retrieved
    :type id: str

    :rtype: Unknown
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=UNKNOWN_TYPE_URI,
        rdf_type_name=UNKNOWN_TYPE_NAME, 
        kls=Unknown)
