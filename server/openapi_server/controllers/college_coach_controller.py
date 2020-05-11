import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COLLEGECOACH_TYPE_NAME, COLLEGECOACH_TYPE_URI

from openapi_server.models.college_coach import CollegeCoach  # noqa: E501
from openapi_server import util

def collegecoachs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CollegeCoach

    Gets a list of all instances of CollegeCoach (more information in http://dbpedia.org/ontology/CollegeCoach) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CollegeCoach]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COLLEGECOACH_TYPE_URI,
        rdf_type_name=COLLEGECOACH_TYPE_NAME, 
        kls=CollegeCoach)

def collegecoachs_id_get(id):  # noqa: E501
    """Get a single CollegeCoach by its id

    Gets the details of a given CollegeCoach (more information in http://dbpedia.org/ontology/CollegeCoach) # noqa: E501

    :param id: The ID of the CollegeCoach to be retrieved
    :type id: str

    :rtype: CollegeCoach
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COLLEGECOACH_TYPE_URI,
        rdf_type_name=COLLEGECOACH_TYPE_NAME, 
        kls=CollegeCoach)
