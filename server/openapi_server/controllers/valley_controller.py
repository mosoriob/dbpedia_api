import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VALLEY_TYPE_NAME, VALLEY_TYPE_URI

from openapi_server.models.valley import Valley  # noqa: E501
from openapi_server import util

def valleys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Valley

    Gets a list of all instances of Valley (more information in http://dbpedia.org/ontology/Valley) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Valley]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VALLEY_TYPE_URI,
        rdf_type_name=VALLEY_TYPE_NAME, 
        kls=Valley)

def valleys_id_get(id):  # noqa: E501
    """Get a single Valley by its id

    Gets the details of a given Valley (more information in http://dbpedia.org/ontology/Valley) # noqa: E501

    :param id: The ID of the Valley to be retrieved
    :type id: str

    :rtype: Valley
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VALLEY_TYPE_URI,
        rdf_type_name=VALLEY_TYPE_NAME, 
        kls=Valley)
