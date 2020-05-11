import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PAINTBALLLEAGUE_TYPE_NAME, PAINTBALLLEAGUE_TYPE_URI

from openapi_server.models.paintball_league import PaintballLeague  # noqa: E501
from openapi_server import util

def paintballleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PaintballLeague

    Gets a list of all instances of PaintballLeague (more information in http://dbpedia.org/ontology/PaintballLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PaintballLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PAINTBALLLEAGUE_TYPE_URI,
        rdf_type_name=PAINTBALLLEAGUE_TYPE_NAME, 
        kls=PaintballLeague)

def paintballleagues_id_get(id):  # noqa: E501
    """Get a single PaintballLeague by its id

    Gets the details of a given PaintballLeague (more information in http://dbpedia.org/ontology/PaintballLeague) # noqa: E501

    :param id: The ID of the PaintballLeague to be retrieved
    :type id: str

    :rtype: PaintballLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PAINTBALLLEAGUE_TYPE_URI,
        rdf_type_name=PAINTBALLLEAGUE_TYPE_NAME, 
        kls=PaintballLeague)
