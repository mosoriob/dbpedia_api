import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WATERRIDE_TYPE_NAME, WATERRIDE_TYPE_URI

from openapi_server.models.water_ride import WaterRide  # noqa: E501
from openapi_server import util

def waterrides_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of WaterRide

    Gets a list of all instances of WaterRide (more information in http://dbpedia.org/ontology/WaterRide) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[WaterRide]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WATERRIDE_TYPE_URI,
        rdf_type_name=WATERRIDE_TYPE_NAME, 
        kls=WaterRide)

def waterrides_id_get(id):  # noqa: E501
    """Get a single WaterRide by its id

    Gets the details of a given WaterRide (more information in http://dbpedia.org/ontology/WaterRide) # noqa: E501

    :param id: The ID of the WaterRide to be retrieved
    :type id: str

    :rtype: WaterRide
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WATERRIDE_TYPE_URI,
        rdf_type_name=WATERRIDE_TYPE_NAME, 
        kls=WaterRide)
