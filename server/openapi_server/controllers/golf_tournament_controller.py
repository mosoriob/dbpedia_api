import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GOLFTOURNAMENT_TYPE_NAME, GOLFTOURNAMENT_TYPE_URI

from openapi_server.models.golf_tournament import GolfTournament  # noqa: E501
from openapi_server import util

def golftournaments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GolfTournament

    Gets a list of all instances of GolfTournament (more information in http://dbpedia.org/ontology/GolfTournament) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GolfTournament]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GOLFTOURNAMENT_TYPE_URI,
        rdf_type_name=GOLFTOURNAMENT_TYPE_NAME, 
        kls=GolfTournament)

def golftournaments_id_get(id):  # noqa: E501
    """Get a single GolfTournament by its id

    Gets the details of a given GolfTournament (more information in http://dbpedia.org/ontology/GolfTournament) # noqa: E501

    :param id: The ID of the GolfTournament to be retrieved
    :type id: str

    :rtype: GolfTournament
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GOLFTOURNAMENT_TYPE_URI,
        rdf_type_name=GOLFTOURNAMENT_TYPE_NAME, 
        kls=GolfTournament)
