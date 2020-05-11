import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HANDBALLLEAGUE_TYPE_NAME, HANDBALLLEAGUE_TYPE_URI

from openapi_server.models.handball_league import HandballLeague  # noqa: E501
from openapi_server import util

def handballleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HandballLeague

    Gets a list of all instances of HandballLeague (more information in http://dbpedia.org/ontology/HandballLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HandballLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HANDBALLLEAGUE_TYPE_URI,
        rdf_type_name=HANDBALLLEAGUE_TYPE_NAME, 
        kls=HandballLeague)

def handballleagues_id_get(id):  # noqa: E501
    """Get a single HandballLeague by its id

    Gets the details of a given HandballLeague (more information in http://dbpedia.org/ontology/HandballLeague) # noqa: E501

    :param id: The ID of the HandballLeague to be retrieved
    :type id: str

    :rtype: HandballLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HANDBALLLEAGUE_TYPE_URI,
        rdf_type_name=HANDBALLLEAGUE_TYPE_NAME, 
        kls=HandballLeague)
