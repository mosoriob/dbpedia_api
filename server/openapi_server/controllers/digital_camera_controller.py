import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DIGITALCAMERA_TYPE_NAME, DIGITALCAMERA_TYPE_URI

from openapi_server.models.digital_camera import DigitalCamera  # noqa: E501
from openapi_server import util

def digitalcameras_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of DigitalCamera

    Gets a list of all instances of DigitalCamera (more information in http://dbpedia.org/ontology/DigitalCamera) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[DigitalCamera]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DIGITALCAMERA_TYPE_URI,
        rdf_type_name=DIGITALCAMERA_TYPE_NAME, 
        kls=DigitalCamera)

def digitalcameras_id_get(id):  # noqa: E501
    """Get a single DigitalCamera by its id

    Gets the details of a given DigitalCamera (more information in http://dbpedia.org/ontology/DigitalCamera) # noqa: E501

    :param id: The ID of the DigitalCamera to be retrieved
    :type id: str

    :rtype: DigitalCamera
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DIGITALCAMERA_TYPE_URI,
        rdf_type_name=DIGITALCAMERA_TYPE_NAME, 
        kls=DigitalCamera)
