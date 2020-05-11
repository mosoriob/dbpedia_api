import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TELEVISIONEPISODE_TYPE_NAME, TELEVISIONEPISODE_TYPE_URI

from openapi_server.models.television_episode import TelevisionEpisode  # noqa: E501
from openapi_server import util

def televisionepisodes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TelevisionEpisode

    Gets a list of all instances of TelevisionEpisode (more information in http://dbpedia.org/ontology/TelevisionEpisode) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TelevisionEpisode]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TELEVISIONEPISODE_TYPE_URI,
        rdf_type_name=TELEVISIONEPISODE_TYPE_NAME, 
        kls=TelevisionEpisode)

def televisionepisodes_id_get(id):  # noqa: E501
    """Get a single TelevisionEpisode by its id

    Gets the details of a given TelevisionEpisode (more information in http://dbpedia.org/ontology/TelevisionEpisode) # noqa: E501

    :param id: The ID of the TelevisionEpisode to be retrieved
    :type id: str

    :rtype: TelevisionEpisode
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TELEVISIONEPISODE_TYPE_URI,
        rdf_type_name=TELEVISIONEPISODE_TYPE_NAME, 
        kls=TelevisionEpisode)
