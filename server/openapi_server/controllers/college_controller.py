import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COLLEGE_TYPE_NAME, COLLEGE_TYPE_URI

from openapi_server.models.college import College  # noqa: E501
from openapi_server import util

def colleges_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of College

    Gets a list of all instances of College (more information in http://dbpedia.org/ontology/College) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[College]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COLLEGE_TYPE_URI,
        rdf_type_name=COLLEGE_TYPE_NAME, 
        kls=College)

def colleges_id_get(id):  # noqa: E501
    """Get a single College by its id

    Gets the details of a given College (more information in http://dbpedia.org/ontology/College) # noqa: E501

    :param id: The ID of the College to be retrieved
    :type id: str

    :rtype: College
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COLLEGE_TYPE_URI,
        rdf_type_name=COLLEGE_TYPE_NAME, 
        kls=College)
