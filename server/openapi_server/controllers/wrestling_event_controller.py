import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WRESTLINGEVENT_TYPE_NAME, WRESTLINGEVENT_TYPE_URI

from openapi_server.models.wrestling_event import WrestlingEvent  # noqa: E501
from openapi_server import util

def wrestlingevents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of WrestlingEvent

    Gets a list of all instances of WrestlingEvent (more information in http://dbpedia.org/ontology/WrestlingEvent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[WrestlingEvent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WRESTLINGEVENT_TYPE_URI,
        rdf_type_name=WRESTLINGEVENT_TYPE_NAME, 
        kls=WrestlingEvent)

def wrestlingevents_id_get(id):  # noqa: E501
    """Get a single WrestlingEvent by its id

    Gets the details of a given WrestlingEvent (more information in http://dbpedia.org/ontology/WrestlingEvent) # noqa: E501

    :param id: The ID of the WrestlingEvent to be retrieved
    :type id: str

    :rtype: WrestlingEvent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WRESTLINGEVENT_TYPE_URI,
        rdf_type_name=WRESTLINGEVENT_TYPE_NAME, 
        kls=WrestlingEvent)
