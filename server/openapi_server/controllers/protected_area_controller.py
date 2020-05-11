import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PROTECTEDAREA_TYPE_NAME, PROTECTEDAREA_TYPE_URI

from openapi_server.models.protected_area import ProtectedArea  # noqa: E501
from openapi_server import util

def protectedareas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ProtectedArea

    Gets a list of all instances of ProtectedArea (more information in http://dbpedia.org/ontology/ProtectedArea) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ProtectedArea]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PROTECTEDAREA_TYPE_URI,
        rdf_type_name=PROTECTEDAREA_TYPE_NAME, 
        kls=ProtectedArea)

def protectedareas_id_get(id):  # noqa: E501
    """Get a single ProtectedArea by its id

    Gets the details of a given ProtectedArea (more information in http://dbpedia.org/ontology/ProtectedArea) # noqa: E501

    :param id: The ID of the ProtectedArea to be retrieved
    :type id: str

    :rtype: ProtectedArea
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PROTECTEDAREA_TYPE_URI,
        rdf_type_name=PROTECTEDAREA_TYPE_NAME, 
        kls=ProtectedArea)
