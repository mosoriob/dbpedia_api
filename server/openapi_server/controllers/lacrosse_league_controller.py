import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LACROSSELEAGUE_TYPE_NAME, LACROSSELEAGUE_TYPE_URI

from openapi_server.models.lacrosse_league import LacrosseLeague  # noqa: E501
from openapi_server import util

def lacrosseleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of LacrosseLeague

    Gets a list of all instances of LacrosseLeague (more information in http://dbpedia.org/ontology/LacrosseLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[LacrosseLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LACROSSELEAGUE_TYPE_URI,
        rdf_type_name=LACROSSELEAGUE_TYPE_NAME, 
        kls=LacrosseLeague)

def lacrosseleagues_id_get(id):  # noqa: E501
    """Get a single LacrosseLeague by its id

    Gets the details of a given LacrosseLeague (more information in http://dbpedia.org/ontology/LacrosseLeague) # noqa: E501

    :param id: The ID of the LacrosseLeague to be retrieved
    :type id: str

    :rtype: LacrosseLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LACROSSELEAGUE_TYPE_URI,
        rdf_type_name=LACROSSELEAGUE_TYPE_NAME, 
        kls=LacrosseLeague)
