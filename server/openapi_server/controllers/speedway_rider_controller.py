import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPEEDWAYRIDER_TYPE_NAME, SPEEDWAYRIDER_TYPE_URI

from openapi_server.models.speedway_rider import SpeedwayRider  # noqa: E501
from openapi_server import util

def speedwayriders_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SpeedwayRider

    Gets a list of all instances of SpeedwayRider (more information in http://dbpedia.org/ontology/SpeedwayRider) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SpeedwayRider]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPEEDWAYRIDER_TYPE_URI,
        rdf_type_name=SPEEDWAYRIDER_TYPE_NAME, 
        kls=SpeedwayRider)

def speedwayriders_id_get(id):  # noqa: E501
    """Get a single SpeedwayRider by its id

    Gets the details of a given SpeedwayRider (more information in http://dbpedia.org/ontology/SpeedwayRider) # noqa: E501

    :param id: The ID of the SpeedwayRider to be retrieved
    :type id: str

    :rtype: SpeedwayRider
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPEEDWAYRIDER_TYPE_URI,
        rdf_type_name=SPEEDWAYRIDER_TYPE_NAME, 
        kls=SpeedwayRider)
