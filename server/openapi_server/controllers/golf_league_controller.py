import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GOLFLEAGUE_TYPE_NAME, GOLFLEAGUE_TYPE_URI

from openapi_server.models.golf_league import GolfLeague  # noqa: E501
from openapi_server import util

def golfleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GolfLeague

    Gets a list of all instances of GolfLeague (more information in http://dbpedia.org/ontology/GolfLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GolfLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GOLFLEAGUE_TYPE_URI,
        rdf_type_name=GOLFLEAGUE_TYPE_NAME, 
        kls=GolfLeague)

def golfleagues_id_get(id):  # noqa: E501
    """Get a single GolfLeague by its id

    Gets the details of a given GolfLeague (more information in http://dbpedia.org/ontology/GolfLeague) # noqa: E501

    :param id: The ID of the GolfLeague to be retrieved
    :type id: str

    :rtype: GolfLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GOLFLEAGUE_TYPE_URI,
        rdf_type_name=GOLFLEAGUE_TYPE_NAME, 
        kls=GolfLeague)
