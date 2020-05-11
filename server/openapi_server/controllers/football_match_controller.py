import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FOOTBALLMATCH_TYPE_NAME, FOOTBALLMATCH_TYPE_URI

from openapi_server.models.football_match import FootballMatch  # noqa: E501
from openapi_server import util

def footballmatchs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FootballMatch

    Gets a list of all instances of FootballMatch (more information in http://dbpedia.org/ontology/FootballMatch) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FootballMatch]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FOOTBALLMATCH_TYPE_URI,
        rdf_type_name=FOOTBALLMATCH_TYPE_NAME, 
        kls=FootballMatch)

def footballmatchs_id_get(id):  # noqa: E501
    """Get a single FootballMatch by its id

    Gets the details of a given FootballMatch (more information in http://dbpedia.org/ontology/FootballMatch) # noqa: E501

    :param id: The ID of the FootballMatch to be retrieved
    :type id: str

    :rtype: FootballMatch
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FOOTBALLMATCH_TYPE_URI,
        rdf_type_name=FOOTBALLMATCH_TYPE_NAME, 
        kls=FootballMatch)
