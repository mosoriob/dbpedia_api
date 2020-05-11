import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POLOLEAGUE_TYPE_NAME, POLOLEAGUE_TYPE_URI

from openapi_server.models.polo_league import PoloLeague  # noqa: E501
from openapi_server import util

def pololeagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PoloLeague

    Gets a list of all instances of PoloLeague (more information in http://dbpedia.org/ontology/PoloLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PoloLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POLOLEAGUE_TYPE_URI,
        rdf_type_name=POLOLEAGUE_TYPE_NAME, 
        kls=PoloLeague)

def pololeagues_id_get(id):  # noqa: E501
    """Get a single PoloLeague by its id

    Gets the details of a given PoloLeague (more information in http://dbpedia.org/ontology/PoloLeague) # noqa: E501

    :param id: The ID of the PoloLeague to be retrieved
    :type id: str

    :rtype: PoloLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POLOLEAGUE_TYPE_URI,
        rdf_type_name=POLOLEAGUE_TYPE_NAME, 
        kls=PoloLeague)
