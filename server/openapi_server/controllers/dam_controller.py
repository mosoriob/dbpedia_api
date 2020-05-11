import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DAM_TYPE_NAME, DAM_TYPE_URI

from openapi_server.models.dam import Dam  # noqa: E501
from openapi_server import util

def dams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Dam

    Gets a list of all instances of Dam (more information in http://dbpedia.org/ontology/Dam) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Dam]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DAM_TYPE_URI,
        rdf_type_name=DAM_TYPE_NAME, 
        kls=Dam)

def dams_id_get(id):  # noqa: E501
    """Get a single Dam by its id

    Gets the details of a given Dam (more information in http://dbpedia.org/ontology/Dam) # noqa: E501

    :param id: The ID of the Dam to be retrieved
    :type id: str

    :rtype: Dam
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DAM_TYPE_URI,
        rdf_type_name=DAM_TYPE_NAME, 
        kls=Dam)
