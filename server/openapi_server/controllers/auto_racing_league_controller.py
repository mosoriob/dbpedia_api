import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AUTORACINGLEAGUE_TYPE_NAME, AUTORACINGLEAGUE_TYPE_URI

from openapi_server.models.auto_racing_league import AutoRacingLeague  # noqa: E501
from openapi_server import util

def autoracingleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AutoRacingLeague

    Gets a list of all instances of AutoRacingLeague (more information in http://dbpedia.org/ontology/AutoRacingLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AutoRacingLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AUTORACINGLEAGUE_TYPE_URI,
        rdf_type_name=AUTORACINGLEAGUE_TYPE_NAME, 
        kls=AutoRacingLeague)

def autoracingleagues_id_get(id):  # noqa: E501
    """Get a single AutoRacingLeague by its id

    Gets the details of a given AutoRacingLeague (more information in http://dbpedia.org/ontology/AutoRacingLeague) # noqa: E501

    :param id: The ID of the AutoRacingLeague to be retrieved
    :type id: str

    :rtype: AutoRacingLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AUTORACINGLEAGUE_TYPE_URI,
        rdf_type_name=AUTORACINGLEAGUE_TYPE_NAME, 
        kls=AutoRacingLeague)
