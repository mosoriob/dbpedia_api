import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NATIONALFOOTBALLLEAGUEEVENT_TYPE_NAME, NATIONALFOOTBALLLEAGUEEVENT_TYPE_URI

from openapi_server.models.national_football_league_event import NationalFootballLeagueEvent  # noqa: E501
from openapi_server import util

def nationalfootballleagueevents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NationalFootballLeagueEvent

    Gets a list of all instances of NationalFootballLeagueEvent (more information in http://dbpedia.org/ontology/NationalFootballLeagueEvent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NationalFootballLeagueEvent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NATIONALFOOTBALLLEAGUEEVENT_TYPE_URI,
        rdf_type_name=NATIONALFOOTBALLLEAGUEEVENT_TYPE_NAME, 
        kls=NationalFootballLeagueEvent)

def nationalfootballleagueevents_id_get(id):  # noqa: E501
    """Get a single NationalFootballLeagueEvent by its id

    Gets the details of a given NationalFootballLeagueEvent (more information in http://dbpedia.org/ontology/NationalFootballLeagueEvent) # noqa: E501

    :param id: The ID of the NationalFootballLeagueEvent to be retrieved
    :type id: str

    :rtype: NationalFootballLeagueEvent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NATIONALFOOTBALLLEAGUEEVENT_TYPE_URI,
        rdf_type_name=NATIONALFOOTBALLLEAGUEEVENT_TYPE_NAME, 
        kls=NationalFootballLeagueEvent)
