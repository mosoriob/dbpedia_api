import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOFTBALLLEAGUE_TYPE_NAME, SOFTBALLLEAGUE_TYPE_URI

from openapi_server.models.softball_league import SoftballLeague  # noqa: E501
from openapi_server import util

def softballleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoftballLeague

    Gets a list of all instances of SoftballLeague (more information in http://dbpedia.org/ontology/SoftballLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoftballLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOFTBALLLEAGUE_TYPE_URI,
        rdf_type_name=SOFTBALLLEAGUE_TYPE_NAME, 
        kls=SoftballLeague)

def softballleagues_id_get(id):  # noqa: E501
    """Get a single SoftballLeague by its id

    Gets the details of a given SoftballLeague (more information in http://dbpedia.org/ontology/SoftballLeague) # noqa: E501

    :param id: The ID of the SoftballLeague to be retrieved
    :type id: str

    :rtype: SoftballLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOFTBALLLEAGUE_TYPE_URI,
        rdf_type_name=SOFTBALLLEAGUE_TYPE_NAME, 
        kls=SoftballLeague)
