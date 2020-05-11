import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GOVERNMENTTYPE_TYPE_NAME, GOVERNMENTTYPE_TYPE_URI

from openapi_server.models.government_type import GovernmentType  # noqa: E501
from openapi_server import util

def governmenttypes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GovernmentType

    Gets a list of all instances of GovernmentType (more information in http://dbpedia.org/ontology/GovernmentType) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GovernmentType]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GOVERNMENTTYPE_TYPE_URI,
        rdf_type_name=GOVERNMENTTYPE_TYPE_NAME, 
        kls=GovernmentType)

def governmenttypes_id_get(id):  # noqa: E501
    """Get a single GovernmentType by its id

    Gets the details of a given GovernmentType (more information in http://dbpedia.org/ontology/GovernmentType) # noqa: E501

    :param id: The ID of the GovernmentType to be retrieved
    :type id: str

    :rtype: GovernmentType
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GOVERNMENTTYPE_TYPE_URI,
        rdf_type_name=GOVERNMENTTYPE_TYPE_NAME, 
        kls=GovernmentType)
