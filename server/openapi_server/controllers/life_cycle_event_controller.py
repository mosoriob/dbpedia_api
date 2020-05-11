import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LIFECYCLEEVENT_TYPE_NAME, LIFECYCLEEVENT_TYPE_URI

from openapi_server.models.life_cycle_event import LifeCycleEvent  # noqa: E501
from openapi_server import util

def lifecycleevents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of LifeCycleEvent

    Gets a list of all instances of LifeCycleEvent (more information in http://dbpedia.org/ontology/LifeCycleEvent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[LifeCycleEvent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LIFECYCLEEVENT_TYPE_URI,
        rdf_type_name=LIFECYCLEEVENT_TYPE_NAME, 
        kls=LifeCycleEvent)

def lifecycleevents_id_get(id):  # noqa: E501
    """Get a single LifeCycleEvent by its id

    Gets the details of a given LifeCycleEvent (more information in http://dbpedia.org/ontology/LifeCycleEvent) # noqa: E501

    :param id: The ID of the LifeCycleEvent to be retrieved
    :type id: str

    :rtype: LifeCycleEvent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LIFECYCLEEVENT_TYPE_URI,
        rdf_type_name=LIFECYCLEEVENT_TYPE_NAME, 
        kls=LifeCycleEvent)
