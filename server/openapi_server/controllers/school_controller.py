import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SCHOOL_TYPE_NAME, SCHOOL_TYPE_URI

from openapi_server.models.school import School  # noqa: E501
from openapi_server import util

def schools_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of School

    Gets a list of all instances of School (more information in http://dbpedia.org/ontology/School) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[School]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SCHOOL_TYPE_URI,
        rdf_type_name=SCHOOL_TYPE_NAME, 
        kls=School)

def schools_id_get(id):  # noqa: E501
    """Get a single School by its id

    Gets the details of a given School (more information in http://dbpedia.org/ontology/School) # noqa: E501

    :param id: The ID of the School to be retrieved
    :type id: str

    :rtype: School
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SCHOOL_TYPE_URI,
        rdf_type_name=SCHOOL_TYPE_NAME, 
        kls=School)
