import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import OLYMPICEVENT_TYPE_NAME, OLYMPICEVENT_TYPE_URI

from openapi_server.models.olympic_event import OlympicEvent  # noqa: E501
from openapi_server import util

def olympicevents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of OlympicEvent

    Gets a list of all instances of OlympicEvent (more information in http://dbpedia.org/ontology/OlympicEvent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[OlympicEvent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=OLYMPICEVENT_TYPE_URI,
        rdf_type_name=OLYMPICEVENT_TYPE_NAME, 
        kls=OlympicEvent)

def olympicevents_id_get(id):  # noqa: E501
    """Get a single OlympicEvent by its id

    Gets the details of a given OlympicEvent (more information in http://dbpedia.org/ontology/OlympicEvent) # noqa: E501

    :param id: The ID of the OlympicEvent to be retrieved
    :type id: str

    :rtype: OlympicEvent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=OLYMPICEVENT_TYPE_URI,
        rdf_type_name=OLYMPICEVENT_TYPE_NAME, 
        kls=OlympicEvent)
