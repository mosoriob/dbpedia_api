import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CYCLINGLEAGUE_TYPE_NAME, CYCLINGLEAGUE_TYPE_URI

from openapi_server.models.cycling_league import CyclingLeague  # noqa: E501
from openapi_server import util

def cyclingleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CyclingLeague

    Gets a list of all instances of CyclingLeague (more information in http://dbpedia.org/ontology/CyclingLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CyclingLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CYCLINGLEAGUE_TYPE_URI,
        rdf_type_name=CYCLINGLEAGUE_TYPE_NAME, 
        kls=CyclingLeague)

def cyclingleagues_id_get(id):  # noqa: E501
    """Get a single CyclingLeague by its id

    Gets the details of a given CyclingLeague (more information in http://dbpedia.org/ontology/CyclingLeague) # noqa: E501

    :param id: The ID of the CyclingLeague to be retrieved
    :type id: str

    :rtype: CyclingLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CYCLINGLEAGUE_TYPE_URI,
        rdf_type_name=CYCLINGLEAGUE_TYPE_NAME, 
        kls=CyclingLeague)
