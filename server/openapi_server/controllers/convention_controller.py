import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CONVENTION_TYPE_NAME, CONVENTION_TYPE_URI

from openapi_server.models.convention import Convention  # noqa: E501
from openapi_server import util

def conventions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Convention

    Gets a list of all instances of Convention (more information in http://dbpedia.org/ontology/Convention) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Convention]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CONVENTION_TYPE_URI,
        rdf_type_name=CONVENTION_TYPE_NAME, 
        kls=Convention)

def conventions_id_get(id):  # noqa: E501
    """Get a single Convention by its id

    Gets the details of a given Convention (more information in http://dbpedia.org/ontology/Convention) # noqa: E501

    :param id: The ID of the Convention to be retrieved
    :type id: str

    :rtype: Convention
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CONVENTION_TYPE_URI,
        rdf_type_name=CONVENTION_TYPE_NAME, 
        kls=Convention)
