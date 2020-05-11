import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LUNARCRATER_TYPE_NAME, LUNARCRATER_TYPE_URI

from openapi_server.models.lunar_crater import LunarCrater  # noqa: E501
from openapi_server import util

def lunarcraters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of LunarCrater

    Gets a list of all instances of LunarCrater (more information in http://dbpedia.org/ontology/LunarCrater) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[LunarCrater]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LUNARCRATER_TYPE_URI,
        rdf_type_name=LUNARCRATER_TYPE_NAME, 
        kls=LunarCrater)

def lunarcraters_id_get(id):  # noqa: E501
    """Get a single LunarCrater by its id

    Gets the details of a given LunarCrater (more information in http://dbpedia.org/ontology/LunarCrater) # noqa: E501

    :param id: The ID of the LunarCrater to be retrieved
    :type id: str

    :rtype: LunarCrater
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LUNARCRATER_TYPE_URI,
        rdf_type_name=LUNARCRATER_TYPE_NAME, 
        kls=LunarCrater)
