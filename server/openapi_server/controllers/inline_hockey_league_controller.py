import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import INLINEHOCKEYLEAGUE_TYPE_NAME, INLINEHOCKEYLEAGUE_TYPE_URI

from openapi_server.models.inline_hockey_league import InlineHockeyLeague  # noqa: E501
from openapi_server import util

def inlinehockeyleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of InlineHockeyLeague

    Gets a list of all instances of InlineHockeyLeague (more information in http://dbpedia.org/ontology/InlineHockeyLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[InlineHockeyLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=INLINEHOCKEYLEAGUE_TYPE_URI,
        rdf_type_name=INLINEHOCKEYLEAGUE_TYPE_NAME, 
        kls=InlineHockeyLeague)

def inlinehockeyleagues_id_get(id):  # noqa: E501
    """Get a single InlineHockeyLeague by its id

    Gets the details of a given InlineHockeyLeague (more information in http://dbpedia.org/ontology/InlineHockeyLeague) # noqa: E501

    :param id: The ID of the InlineHockeyLeague to be retrieved
    :type id: str

    :rtype: InlineHockeyLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=INLINEHOCKEYLEAGUE_TYPE_URI,
        rdf_type_name=INLINEHOCKEYLEAGUE_TYPE_NAME, 
        kls=InlineHockeyLeague)
