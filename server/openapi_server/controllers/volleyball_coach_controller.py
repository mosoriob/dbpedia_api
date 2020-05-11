import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VOLLEYBALLCOACH_TYPE_NAME, VOLLEYBALLCOACH_TYPE_URI

from openapi_server.models.volleyball_coach import VolleyballCoach  # noqa: E501
from openapi_server import util

def volleyballcoachs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of VolleyballCoach

    Gets a list of all instances of VolleyballCoach (more information in http://dbpedia.org/ontology/VolleyballCoach) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[VolleyballCoach]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VOLLEYBALLCOACH_TYPE_URI,
        rdf_type_name=VOLLEYBALLCOACH_TYPE_NAME, 
        kls=VolleyballCoach)

def volleyballcoachs_id_get(id):  # noqa: E501
    """Get a single VolleyballCoach by its id

    Gets the details of a given VolleyballCoach (more information in http://dbpedia.org/ontology/VolleyballCoach) # noqa: E501

    :param id: The ID of the VolleyballCoach to be retrieved
    :type id: str

    :rtype: VolleyballCoach
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VOLLEYBALLCOACH_TYPE_URI,
        rdf_type_name=VOLLEYBALLCOACH_TYPE_NAME, 
        kls=VolleyballCoach)
