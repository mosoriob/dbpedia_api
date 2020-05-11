import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORTCOMPETITIONRESULT_TYPE_NAME, SPORTCOMPETITIONRESULT_TYPE_URI

from openapi_server.models.sport_competition_result import SportCompetitionResult  # noqa: E501
from openapi_server import util

def sportcompetitionresults_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SportCompetitionResult

    Gets a list of all instances of SportCompetitionResult (more information in http://dbpedia.org/ontology/SportCompetitionResult) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SportCompetitionResult]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORTCOMPETITIONRESULT_TYPE_URI,
        rdf_type_name=SPORTCOMPETITIONRESULT_TYPE_NAME, 
        kls=SportCompetitionResult)

def sportcompetitionresults_id_get(id):  # noqa: E501
    """Get a single SportCompetitionResult by its id

    Gets the details of a given SportCompetitionResult (more information in http://dbpedia.org/ontology/SportCompetitionResult) # noqa: E501

    :param id: The ID of the SportCompetitionResult to be retrieved
    :type id: str

    :rtype: SportCompetitionResult
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORTCOMPETITIONRESULT_TYPE_URI,
        rdf_type_name=SPORTCOMPETITIONRESULT_TYPE_NAME, 
        kls=SportCompetitionResult)
