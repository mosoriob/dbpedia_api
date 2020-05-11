import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CRICKETLEAGUE_TYPE_NAME, CRICKETLEAGUE_TYPE_URI

from openapi_server.models.cricket_league import CricketLeague  # noqa: E501
from openapi_server import util

def cricketleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CricketLeague

    Gets a list of all instances of CricketLeague (more information in http://dbpedia.org/ontology/CricketLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CricketLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CRICKETLEAGUE_TYPE_URI,
        rdf_type_name=CRICKETLEAGUE_TYPE_NAME, 
        kls=CricketLeague)

def cricketleagues_id_get(id):  # noqa: E501
    """Get a single CricketLeague by its id

    Gets the details of a given CricketLeague (more information in http://dbpedia.org/ontology/CricketLeague) # noqa: E501

    :param id: The ID of the CricketLeague to be retrieved
    :type id: str

    :rtype: CricketLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CRICKETLEAGUE_TYPE_URI,
        rdf_type_name=CRICKETLEAGUE_TYPE_NAME, 
        kls=CricketLeague)
