import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SNOOKERWORLDRANKING_TYPE_NAME, SNOOKERWORLDRANKING_TYPE_URI

from openapi_server.models.snooker_world_ranking import SnookerWorldRanking  # noqa: E501
from openapi_server import util

def snookerworldrankings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SnookerWorldRanking

    Gets a list of all instances of SnookerWorldRanking (more information in http://dbpedia.org/ontology/SnookerWorldRanking) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SnookerWorldRanking]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SNOOKERWORLDRANKING_TYPE_URI,
        rdf_type_name=SNOOKERWORLDRANKING_TYPE_NAME, 
        kls=SnookerWorldRanking)

def snookerworldrankings_id_get(id):  # noqa: E501
    """Get a single SnookerWorldRanking by its id

    Gets the details of a given SnookerWorldRanking (more information in http://dbpedia.org/ontology/SnookerWorldRanking) # noqa: E501

    :param id: The ID of the SnookerWorldRanking to be retrieved
    :type id: str

    :rtype: SnookerWorldRanking
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SNOOKERWORLDRANKING_TYPE_URI,
        rdf_type_name=SNOOKERWORLDRANKING_TYPE_NAME, 
        kls=SnookerWorldRanking)
