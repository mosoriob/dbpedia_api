import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TOURNAMENT_TYPE_NAME, TOURNAMENT_TYPE_URI

from openapi_server.models.tournament import Tournament  # noqa: E501
from openapi_server import util

def tournaments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Tournament

    Gets a list of all instances of Tournament (more information in http://dbpedia.org/ontology/Tournament) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Tournament]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TOURNAMENT_TYPE_URI,
        rdf_type_name=TOURNAMENT_TYPE_NAME, 
        kls=Tournament)

def tournaments_id_get(id):  # noqa: E501
    """Get a single Tournament by its id

    Gets the details of a given Tournament (more information in http://dbpedia.org/ontology/Tournament) # noqa: E501

    :param id: The ID of the Tournament to be retrieved
    :type id: str

    :rtype: Tournament
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TOURNAMENT_TYPE_URI,
        rdf_type_name=TOURNAMENT_TYPE_NAME, 
        kls=Tournament)
