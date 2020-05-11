import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SCREENWRITER_TYPE_NAME, SCREENWRITER_TYPE_URI

from openapi_server.models.screen_writer import ScreenWriter  # noqa: E501
from openapi_server import util

def screenwriters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ScreenWriter

    Gets a list of all instances of ScreenWriter (more information in http://dbpedia.org/ontology/ScreenWriter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ScreenWriter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SCREENWRITER_TYPE_URI,
        rdf_type_name=SCREENWRITER_TYPE_NAME, 
        kls=ScreenWriter)

def screenwriters_id_get(id):  # noqa: E501
    """Get a single ScreenWriter by its id

    Gets the details of a given ScreenWriter (more information in http://dbpedia.org/ontology/ScreenWriter) # noqa: E501

    :param id: The ID of the ScreenWriter to be retrieved
    :type id: str

    :rtype: ScreenWriter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SCREENWRITER_TYPE_URI,
        rdf_type_name=SCREENWRITER_TYPE_NAME, 
        kls=ScreenWriter)
