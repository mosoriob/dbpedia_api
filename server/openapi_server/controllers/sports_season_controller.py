import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPORTSSEASON_TYPE_NAME, SPORTSSEASON_TYPE_URI

from openapi_server.models.sports_season import SportsSeason  # noqa: E501
from openapi_server import util

def sportsseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SportsSeason

    Gets a list of all instances of SportsSeason (more information in http://dbpedia.org/ontology/SportsSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SportsSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPORTSSEASON_TYPE_URI,
        rdf_type_name=SPORTSSEASON_TYPE_NAME, 
        kls=SportsSeason)

def sportsseasons_id_get(id):  # noqa: E501
    """Get a single SportsSeason by its id

    Gets the details of a given SportsSeason (more information in http://dbpedia.org/ontology/SportsSeason) # noqa: E501

    :param id: The ID of the SportsSeason to be retrieved
    :type id: str

    :rtype: SportsSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPORTSSEASON_TYPE_URI,
        rdf_type_name=SPORTSSEASON_TYPE_NAME, 
        kls=SportsSeason)
