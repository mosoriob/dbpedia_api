import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SONGWRITER_TYPE_NAME, SONGWRITER_TYPE_URI

from openapi_server.models.song_writer import SongWriter  # noqa: E501
from openapi_server import util

def songwriters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SongWriter

    Gets a list of all instances of SongWriter (more information in http://dbpedia.org/ontology/SongWriter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SongWriter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SONGWRITER_TYPE_URI,
        rdf_type_name=SONGWRITER_TYPE_NAME, 
        kls=SongWriter)

def songwriters_id_get(id):  # noqa: E501
    """Get a single SongWriter by its id

    Gets the details of a given SongWriter (more information in http://dbpedia.org/ontology/SongWriter) # noqa: E501

    :param id: The ID of the SongWriter to be retrieved
    :type id: str

    :rtype: SongWriter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SONGWRITER_TYPE_URI,
        rdf_type_name=SONGWRITER_TYPE_NAME, 
        kls=SongWriter)
