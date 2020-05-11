import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORTSEVENT_TYPE_NAME, SPORTSEVENT_TYPE_URI

from openapi_server.models.sports_event import SportsEvent  # noqa: E501
from openapi_server import util

def sportsevents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SportsEvent

    Gets a list of all instances of SportsEvent (more information in http://dbpedia.org/ontology/SportsEvent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SportsEvent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORTSEVENT_TYPE_URI,
        rdf_type_name=SPORTSEVENT_TYPE_NAME, 
        kls=SportsEvent)

def sportsevents_id_get(id):  # noqa: E501
    """Get a single SportsEvent by its id

    Gets the details of a given SportsEvent (more information in http://dbpedia.org/ontology/SportsEvent) # noqa: E501

    :param id: The ID of the SportsEvent to be retrieved
    :type id: str

    :rtype: SportsEvent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORTSEVENT_TYPE_URI,
        rdf_type_name=SPORTSEVENT_TYPE_NAME, 
        kls=SportsEvent)
