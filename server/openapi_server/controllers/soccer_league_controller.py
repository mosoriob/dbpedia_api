import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOCCERLEAGUE_TYPE_NAME, SOCCERLEAGUE_TYPE_URI

from openapi_server.models.soccer_league import SoccerLeague  # noqa: E501
from openapi_server import util

def soccerleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoccerLeague

    Gets a list of all instances of SoccerLeague (more information in http://dbpedia.org/ontology/SoccerLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoccerLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOCCERLEAGUE_TYPE_URI,
        rdf_type_name=SOCCERLEAGUE_TYPE_NAME, 
        kls=SoccerLeague)

def soccerleagues_id_get(id):  # noqa: E501
    """Get a single SoccerLeague by its id

    Gets the details of a given SoccerLeague (more information in http://dbpedia.org/ontology/SoccerLeague) # noqa: E501

    :param id: The ID of the SoccerLeague to be retrieved
    :type id: str

    :rtype: SoccerLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOCCERLEAGUE_TYPE_URI,
        rdf_type_name=SOCCERLEAGUE_TYPE_NAME, 
        kls=SoccerLeague)
