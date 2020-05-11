import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import REFERENCE_TYPE_NAME, REFERENCE_TYPE_URI

from openapi_server.models.reference import Reference  # noqa: E501
from openapi_server import util

def references_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Reference

    Gets a list of all instances of Reference (more information in http://dbpedia.org/ontology/Reference) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Reference]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=REFERENCE_TYPE_URI,
        rdf_type_name=REFERENCE_TYPE_NAME, 
        kls=Reference)

def references_id_get(id):  # noqa: E501
    """Get a single Reference by its id

    Gets the details of a given Reference (more information in http://dbpedia.org/ontology/Reference) # noqa: E501

    :param id: The ID of the Reference to be retrieved
    :type id: str

    :rtype: Reference
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=REFERENCE_TYPE_URI,
        rdf_type_name=REFERENCE_TYPE_NAME, 
        kls=Reference)
