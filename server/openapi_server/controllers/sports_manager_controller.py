import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORTSMANAGER_TYPE_NAME, SPORTSMANAGER_TYPE_URI

from openapi_server.models.sports_manager import SportsManager  # noqa: E501
from openapi_server import util

def sportsmanagers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SportsManager

    Gets a list of all instances of SportsManager (more information in http://dbpedia.org/ontology/SportsManager) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SportsManager]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORTSMANAGER_TYPE_URI,
        rdf_type_name=SPORTSMANAGER_TYPE_NAME, 
        kls=SportsManager)

def sportsmanagers_id_get(id):  # noqa: E501
    """Get a single SportsManager by its id

    Gets the details of a given SportsManager (more information in http://dbpedia.org/ontology/SportsManager) # noqa: E501

    :param id: The ID of the SportsManager to be retrieved
    :type id: str

    :rtype: SportsManager
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORTSMANAGER_TYPE_URI,
        rdf_type_name=SPORTSMANAGER_TYPE_NAME, 
        kls=SportsManager)
