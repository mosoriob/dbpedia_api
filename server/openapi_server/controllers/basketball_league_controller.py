import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BASKETBALLLEAGUE_TYPE_NAME, BASKETBALLLEAGUE_TYPE_URI

from openapi_server.models.basketball_league import BasketballLeague  # noqa: E501
from openapi_server import util

def basketballleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BasketballLeague

    Gets a list of all instances of BasketballLeague (more information in http://dbpedia.org/ontology/BasketballLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BasketballLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BASKETBALLLEAGUE_TYPE_URI,
        rdf_type_name=BASKETBALLLEAGUE_TYPE_NAME, 
        kls=BasketballLeague)

def basketballleagues_id_get(id):  # noqa: E501
    """Get a single BasketballLeague by its id

    Gets the details of a given BasketballLeague (more information in http://dbpedia.org/ontology/BasketballLeague) # noqa: E501

    :param id: The ID of the BasketballLeague to be retrieved
    :type id: str

    :rtype: BasketballLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BASKETBALLLEAGUE_TYPE_URI,
        rdf_type_name=BASKETBALLLEAGUE_TYPE_NAME, 
        kls=BasketballLeague)
