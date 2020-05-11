import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CURLINGLEAGUE_TYPE_NAME, CURLINGLEAGUE_TYPE_URI

from openapi_server.models.curling_league import CurlingLeague  # noqa: E501
from openapi_server import util

def curlingleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CurlingLeague

    Gets a list of all instances of CurlingLeague (more information in http://dbpedia.org/ontology/CurlingLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CurlingLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CURLINGLEAGUE_TYPE_URI,
        rdf_type_name=CURLINGLEAGUE_TYPE_NAME, 
        kls=CurlingLeague)

def curlingleagues_id_get(id):  # noqa: E501
    """Get a single CurlingLeague by its id

    Gets the details of a given CurlingLeague (more information in http://dbpedia.org/ontology/CurlingLeague) # noqa: E501

    :param id: The ID of the CurlingLeague to be retrieved
    :type id: str

    :rtype: CurlingLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CURLINGLEAGUE_TYPE_URI,
        rdf_type_name=CURLINGLEAGUE_TYPE_NAME, 
        kls=CurlingLeague)
