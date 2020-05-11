import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import EVENT_TYPE_NAME, EVENT_TYPE_URI

from openapi_server.models.event import Event  # noqa: E501
from openapi_server import util

def events_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Event

    Gets a list of all instances of Event (more information in http://dbpedia.org/ontology/Event) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Event]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=EVENT_TYPE_URI,
        rdf_type_name=EVENT_TYPE_NAME, 
        kls=Event)

def events_id_get(id):  # noqa: E501
    """Get a single Event by its id

    Gets the details of a given Event (more information in http://dbpedia.org/ontology/Event) # noqa: E501

    :param id: The ID of the Event to be retrieved
    :type id: str

    :rtype: Event
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=EVENT_TYPE_URI,
        rdf_type_name=EVENT_TYPE_NAME, 
        kls=Event)
