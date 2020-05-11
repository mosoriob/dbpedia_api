import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VOLLEYBALLLEAGUE_TYPE_NAME, VOLLEYBALLLEAGUE_TYPE_URI

from openapi_server.models.volleyball_league import VolleyballLeague  # noqa: E501
from openapi_server import util

def volleyballleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of VolleyballLeague

    Gets a list of all instances of VolleyballLeague (more information in http://dbpedia.org/ontology/VolleyballLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[VolleyballLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VOLLEYBALLLEAGUE_TYPE_URI,
        rdf_type_name=VOLLEYBALLLEAGUE_TYPE_NAME, 
        kls=VolleyballLeague)

def volleyballleagues_id_get(id):  # noqa: E501
    """Get a single VolleyballLeague by its id

    Gets the details of a given VolleyballLeague (more information in http://dbpedia.org/ontology/VolleyballLeague) # noqa: E501

    :param id: The ID of the VolleyballLeague to be retrieved
    :type id: str

    :rtype: VolleyballLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VOLLEYBALLLEAGUE_TYPE_URI,
        rdf_type_name=VOLLEYBALLLEAGUE_TYPE_NAME, 
        kls=VolleyballLeague)
