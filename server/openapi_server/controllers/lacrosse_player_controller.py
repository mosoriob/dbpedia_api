import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LACROSSEPLAYER_TYPE_NAME, LACROSSEPLAYER_TYPE_URI

from openapi_server.models.lacrosse_player import LacrossePlayer  # noqa: E501
from openapi_server import util

def lacrosseplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of LacrossePlayer

    Gets a list of all instances of LacrossePlayer (more information in http://dbpedia.org/ontology/LacrossePlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[LacrossePlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LACROSSEPLAYER_TYPE_URI,
        rdf_type_name=LACROSSEPLAYER_TYPE_NAME, 
        kls=LacrossePlayer)

def lacrosseplayers_id_get(id):  # noqa: E501
    """Get a single LacrossePlayer by its id

    Gets the details of a given LacrossePlayer (more information in http://dbpedia.org/ontology/LacrossePlayer) # noqa: E501

    :param id: The ID of the LacrossePlayer to be retrieved
    :type id: str

    :rtype: LacrossePlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LACROSSEPLAYER_TYPE_URI,
        rdf_type_name=LACROSSEPLAYER_TYPE_NAME, 
        kls=LacrossePlayer)
