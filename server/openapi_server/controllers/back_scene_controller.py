import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BACKSCENE_TYPE_NAME, BACKSCENE_TYPE_URI

from openapi_server.models.back_scene import BackScene  # noqa: E501
from openapi_server import util

def backscenes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BackScene

    Gets a list of all instances of BackScene (more information in http://dbpedia.org/ontology/BackScene) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BackScene]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BACKSCENE_TYPE_URI,
        rdf_type_name=BACKSCENE_TYPE_NAME, 
        kls=BackScene)

def backscenes_id_get(id):  # noqa: E501
    """Get a single BackScene by its id

    Gets the details of a given BackScene (more information in http://dbpedia.org/ontology/BackScene) # noqa: E501

    :param id: The ID of the BackScene to be retrieved
    :type id: str

    :rtype: BackScene
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BACKSCENE_TYPE_URI,
        rdf_type_name=BACKSCENE_TYPE_NAME, 
        kls=BackScene)
