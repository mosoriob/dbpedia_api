import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WATERTOWER_TYPE_NAME, WATERTOWER_TYPE_URI

from openapi_server.models.water_tower import WaterTower  # noqa: E501
from openapi_server import util

def watertowers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of WaterTower

    Gets a list of all instances of WaterTower (more information in http://dbpedia.org/ontology/WaterTower) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[WaterTower]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WATERTOWER_TYPE_URI,
        rdf_type_name=WATERTOWER_TYPE_NAME, 
        kls=WaterTower)

def watertowers_id_get(id):  # noqa: E501
    """Get a single WaterTower by its id

    Gets the details of a given WaterTower (more information in http://dbpedia.org/ontology/WaterTower) # noqa: E501

    :param id: The ID of the WaterTower to be retrieved
    :type id: str

    :rtype: WaterTower
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WATERTOWER_TYPE_URI,
        rdf_type_name=WATERTOWER_TYPE_NAME, 
        kls=WaterTower)
