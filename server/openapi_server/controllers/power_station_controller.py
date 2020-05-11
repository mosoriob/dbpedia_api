import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POWERSTATION_TYPE_NAME, POWERSTATION_TYPE_URI

from openapi_server.models.power_station import PowerStation  # noqa: E501
from openapi_server import util

def powerstations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PowerStation

    Gets a list of all instances of PowerStation (more information in http://dbpedia.org/ontology/PowerStation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PowerStation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POWERSTATION_TYPE_URI,
        rdf_type_name=POWERSTATION_TYPE_NAME, 
        kls=PowerStation)

def powerstations_id_get(id):  # noqa: E501
    """Get a single PowerStation by its id

    Gets the details of a given PowerStation (more information in http://dbpedia.org/ontology/PowerStation) # noqa: E501

    :param id: The ID of the PowerStation to be retrieved
    :type id: str

    :rtype: PowerStation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POWERSTATION_TYPE_URI,
        rdf_type_name=POWERSTATION_TYPE_NAME, 
        kls=PowerStation)
