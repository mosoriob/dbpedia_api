import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CAMERA_TYPE_NAME, CAMERA_TYPE_URI

from openapi_server.models.camera import Camera  # noqa: E501
from openapi_server import util

def cameras_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Camera

    Gets a list of all instances of Camera (more information in http://dbpedia.org/ontology/Camera) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Camera]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CAMERA_TYPE_URI,
        rdf_type_name=CAMERA_TYPE_NAME, 
        kls=Camera)

def cameras_id_get(id):  # noqa: E501
    """Get a single Camera by its id

    Gets the details of a given Camera (more information in http://dbpedia.org/ontology/Camera) # noqa: E501

    :param id: The ID of the Camera to be retrieved
    :type id: str

    :rtype: Camera
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CAMERA_TYPE_URI,
        rdf_type_name=CAMERA_TYPE_NAME, 
        kls=Camera)
