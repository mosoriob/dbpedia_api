import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RESUME_TYPE_NAME, RESUME_TYPE_URI

from openapi_server.models.resume import Resume  # noqa: E501
from openapi_server import util

def resumes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Resume

    Gets a list of all instances of Resume (more information in http://dbpedia.org/ontology/Resume) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Resume]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RESUME_TYPE_URI,
        rdf_type_name=RESUME_TYPE_NAME, 
        kls=Resume)

def resumes_id_get(id):  # noqa: E501
    """Get a single Resume by its id

    Gets the details of a given Resume (more information in http://dbpedia.org/ontology/Resume) # noqa: E501

    :param id: The ID of the Resume to be retrieved
    :type id: str

    :rtype: Resume
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RESUME_TYPE_URI,
        rdf_type_name=RESUME_TYPE_NAME, 
        kls=Resume)
