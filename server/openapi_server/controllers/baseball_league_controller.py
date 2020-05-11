import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BASEBALLLEAGUE_TYPE_NAME, BASEBALLLEAGUE_TYPE_URI

from openapi_server.models.baseball_league import BaseballLeague  # noqa: E501
from openapi_server import util

def baseballleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BaseballLeague

    Gets a list of all instances of BaseballLeague (more information in http://dbpedia.org/ontology/BaseballLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BaseballLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BASEBALLLEAGUE_TYPE_URI,
        rdf_type_name=BASEBALLLEAGUE_TYPE_NAME, 
        kls=BaseballLeague)

def baseballleagues_id_get(id):  # noqa: E501
    """Get a single BaseballLeague by its id

    Gets the details of a given BaseballLeague (more information in http://dbpedia.org/ontology/BaseballLeague) # noqa: E501

    :param id: The ID of the BaseballLeague to be retrieved
    :type id: str

    :rtype: BaseballLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BASEBALLLEAGUE_TYPE_URI,
        rdf_type_name=BASEBALLLEAGUE_TYPE_NAME, 
        kls=BaseballLeague)
