import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COACH_TYPE_NAME, COACH_TYPE_URI

from openapi_server.models.coach import Coach  # noqa: E501
from openapi_server import util

def coachs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Coach

    Gets a list of all instances of Coach (more information in http://dbpedia.org/ontology/Coach) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Coach]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COACH_TYPE_URI,
        rdf_type_name=COACH_TYPE_NAME, 
        kls=Coach)

def coachs_id_get(id):  # noqa: E501
    """Get a single Coach by its id

    Gets the details of a given Coach (more information in http://dbpedia.org/ontology/Coach) # noqa: E501

    :param id: The ID of the Coach to be retrieved
    :type id: str

    :rtype: Coach
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COACH_TYPE_URI,
        rdf_type_name=COACH_TYPE_NAME, 
        kls=Coach)
