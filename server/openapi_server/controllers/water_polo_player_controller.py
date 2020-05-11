import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WATERPOLOPLAYER_TYPE_NAME, WATERPOLOPLAYER_TYPE_URI

from openapi_server.models.water_polo_player import WaterPoloPlayer  # noqa: E501
from openapi_server import util

def waterpoloplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of WaterPoloPlayer

    Gets a list of all instances of WaterPoloPlayer (more information in http://dbpedia.org/ontology/WaterPoloPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[WaterPoloPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WATERPOLOPLAYER_TYPE_URI,
        rdf_type_name=WATERPOLOPLAYER_TYPE_NAME, 
        kls=WaterPoloPlayer)

def waterpoloplayers_id_get(id):  # noqa: E501
    """Get a single WaterPoloPlayer by its id

    Gets the details of a given WaterPoloPlayer (more information in http://dbpedia.org/ontology/WaterPoloPlayer) # noqa: E501

    :param id: The ID of the WaterPoloPlayer to be retrieved
    :type id: str

    :rtype: WaterPoloPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WATERPOLOPLAYER_TYPE_URI,
        rdf_type_name=WATERPOLOPLAYER_TYPE_NAME, 
        kls=WaterPoloPlayer)
