import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DISTRICTWATERBOARD_TYPE_NAME, DISTRICTWATERBOARD_TYPE_URI

from openapi_server.models.district_water_board import DistrictWaterBoard  # noqa: E501
from openapi_server import util

def districtwaterboards_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of DistrictWaterBoard

    Gets a list of all instances of DistrictWaterBoard (more information in http://dbpedia.org/ontology/DistrictWaterBoard) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[DistrictWaterBoard]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DISTRICTWATERBOARD_TYPE_URI,
        rdf_type_name=DISTRICTWATERBOARD_TYPE_NAME, 
        kls=DistrictWaterBoard)

def districtwaterboards_id_get(id):  # noqa: E501
    """Get a single DistrictWaterBoard by its id

    Gets the details of a given DistrictWaterBoard (more information in http://dbpedia.org/ontology/DistrictWaterBoard) # noqa: E501

    :param id: The ID of the DistrictWaterBoard to be retrieved
    :type id: str

    :rtype: DistrictWaterBoard
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DISTRICTWATERBOARD_TYPE_URI,
        rdf_type_name=DISTRICTWATERBOARD_TYPE_NAME, 
        kls=DistrictWaterBoard)
