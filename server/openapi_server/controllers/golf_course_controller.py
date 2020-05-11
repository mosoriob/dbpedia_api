import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GOLFCOURSE_TYPE_NAME, GOLFCOURSE_TYPE_URI

from openapi_server.models.golf_course import GolfCourse  # noqa: E501
from openapi_server import util

def golfcourses_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GolfCourse

    Gets a list of all instances of GolfCourse (more information in http://dbpedia.org/ontology/GolfCourse) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GolfCourse]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GOLFCOURSE_TYPE_URI,
        rdf_type_name=GOLFCOURSE_TYPE_NAME, 
        kls=GolfCourse)

def golfcourses_id_get(id):  # noqa: E501
    """Get a single GolfCourse by its id

    Gets the details of a given GolfCourse (more information in http://dbpedia.org/ontology/GolfCourse) # noqa: E501

    :param id: The ID of the GolfCourse to be retrieved
    :type id: str

    :rtype: GolfCourse
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GOLFCOURSE_TYPE_URI,
        rdf_type_name=GOLFCOURSE_TYPE_NAME, 
        kls=GolfCourse)
