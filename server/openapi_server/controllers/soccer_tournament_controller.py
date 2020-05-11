import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOCCERTOURNAMENT_TYPE_NAME, SOCCERTOURNAMENT_TYPE_URI

from openapi_server.models.soccer_tournament import SoccerTournament  # noqa: E501
from openapi_server import util

def soccertournaments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoccerTournament

    Gets a list of all instances of SoccerTournament (more information in http://dbpedia.org/ontology/SoccerTournament) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoccerTournament]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOCCERTOURNAMENT_TYPE_URI,
        rdf_type_name=SOCCERTOURNAMENT_TYPE_NAME, 
        kls=SoccerTournament)

def soccertournaments_id_get(id):  # noqa: E501
    """Get a single SoccerTournament by its id

    Gets the details of a given SoccerTournament (more information in http://dbpedia.org/ontology/SoccerTournament) # noqa: E501

    :param id: The ID of the SoccerTournament to be retrieved
    :type id: str

    :rtype: SoccerTournament
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOCCERTOURNAMENT_TYPE_URI,
        rdf_type_name=SOCCERTOURNAMENT_TYPE_NAME, 
        kls=SoccerTournament)
