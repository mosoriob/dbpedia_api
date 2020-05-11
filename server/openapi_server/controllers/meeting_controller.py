import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MEETING_TYPE_NAME, MEETING_TYPE_URI

from openapi_server.models.meeting import Meeting  # noqa: E501
from openapi_server import util

def meetings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Meeting

    Gets a list of all instances of Meeting (more information in http://dbpedia.org/ontology/Meeting) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Meeting]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MEETING_TYPE_URI,
        rdf_type_name=MEETING_TYPE_NAME, 
        kls=Meeting)

def meetings_id_get(id):  # noqa: E501
    """Get a single Meeting by its id

    Gets the details of a given Meeting (more information in http://dbpedia.org/ontology/Meeting) # noqa: E501

    :param id: The ID of the Meeting to be retrieved
    :type id: str

    :rtype: Meeting
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MEETING_TYPE_URI,
        rdf_type_name=MEETING_TYPE_NAME, 
        kls=Meeting)
