import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DEVICE_TYPE_NAME, DEVICE_TYPE_URI

from openapi_server.models.device import Device  # noqa: E501
from openapi_server import util

def devices_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Device

    Gets a list of all instances of Device (more information in http://dbpedia.org/ontology/Device) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Device]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DEVICE_TYPE_URI,
        rdf_type_name=DEVICE_TYPE_NAME, 
        kls=Device)

def devices_id_get(id):  # noqa: E501
    """Get a single Device by its id

    Gets the details of a given Device (more information in http://dbpedia.org/ontology/Device) # noqa: E501

    :param id: The ID of the Device to be retrieved
    :type id: str

    :rtype: Device
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DEVICE_TYPE_URI,
        rdf_type_name=DEVICE_TYPE_NAME, 
        kls=Device)
