import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import REFEREE_TYPE_NAME, REFEREE_TYPE_URI

from openapi_server.models.referee import Referee  # noqa: E501
from openapi_server import util

def referees_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Referee

    Gets a list of all instances of Referee (more information in http://dbpedia.org/ontology/Referee) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Referee]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=REFEREE_TYPE_URI,
        rdf_type_name=REFEREE_TYPE_NAME, 
        kls=Referee)

def referees_id_get(id):  # noqa: E501
    """Get a single Referee by its id

    Gets the details of a given Referee (more information in http://dbpedia.org/ontology/Referee) # noqa: E501

    :param id: The ID of the Referee to be retrieved
    :type id: str

    :rtype: Referee
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=REFEREE_TYPE_URI,
        rdf_type_name=REFEREE_TYPE_NAME, 
        kls=Referee)
