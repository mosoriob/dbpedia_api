import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PERSONALEVENT_TYPE_NAME, PERSONALEVENT_TYPE_URI

from openapi_server.models.personal_event import PersonalEvent  # noqa: E501
from openapi_server import util

def personalevents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PersonalEvent

    Gets a list of all instances of PersonalEvent (more information in http://dbpedia.org/ontology/PersonalEvent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PersonalEvent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PERSONALEVENT_TYPE_URI,
        rdf_type_name=PERSONALEVENT_TYPE_NAME, 
        kls=PersonalEvent)

def personalevents_id_get(id):  # noqa: E501
    """Get a single PersonalEvent by its id

    Gets the details of a given PersonalEvent (more information in http://dbpedia.org/ontology/PersonalEvent) # noqa: E501

    :param id: The ID of the PersonalEvent to be retrieved
    :type id: str

    :rtype: PersonalEvent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PERSONALEVENT_TYPE_URI,
        rdf_type_name=PERSONALEVENT_TYPE_NAME, 
        kls=PersonalEvent)
