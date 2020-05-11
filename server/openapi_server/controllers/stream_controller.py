import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import STREAM_TYPE_NAME, STREAM_TYPE_URI

from openapi_server.models.stream import Stream  # noqa: E501
from openapi_server import util

def streams_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Stream

    Gets a list of all instances of Stream (more information in http://dbpedia.org/ontology/Stream) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Stream]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=STREAM_TYPE_URI,
        rdf_type_name=STREAM_TYPE_NAME, 
        kls=Stream)

def streams_id_get(id):  # noqa: E501
    """Get a single Stream by its id

    Gets the details of a given Stream (more information in http://dbpedia.org/ontology/Stream) # noqa: E501

    :param id: The ID of the Stream to be retrieved
    :type id: str

    :rtype: Stream
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=STREAM_TYPE_URI,
        rdf_type_name=STREAM_TYPE_NAME, 
        kls=Stream)
