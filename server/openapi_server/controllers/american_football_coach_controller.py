import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AMERICANFOOTBALLCOACH_TYPE_NAME, AMERICANFOOTBALLCOACH_TYPE_URI

from openapi_server.models.american_football_coach import AmericanFootballCoach  # noqa: E501
from openapi_server import util

def americanfootballcoachs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AmericanFootballCoach

    Gets a list of all instances of AmericanFootballCoach (more information in http://dbpedia.org/ontology/AmericanFootballCoach) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AmericanFootballCoach]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AMERICANFOOTBALLCOACH_TYPE_URI,
        rdf_type_name=AMERICANFOOTBALLCOACH_TYPE_NAME, 
        kls=AmericanFootballCoach)

def americanfootballcoachs_id_get(id):  # noqa: E501
    """Get a single AmericanFootballCoach by its id

    Gets the details of a given AmericanFootballCoach (more information in http://dbpedia.org/ontology/AmericanFootballCoach) # noqa: E501

    :param id: The ID of the AmericanFootballCoach to be retrieved
    :type id: str

    :rtype: AmericanFootballCoach
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AMERICANFOOTBALLCOACH_TYPE_URI,
        rdf_type_name=AMERICANFOOTBALLCOACH_TYPE_NAME, 
        kls=AmericanFootballCoach)
