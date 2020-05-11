import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DEPARTMENT_TYPE_NAME, DEPARTMENT_TYPE_URI

from openapi_server.models.department import Department  # noqa: E501
from openapi_server import util

def departments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Department

    Gets a list of all instances of Department (more information in http://dbpedia.org/ontology/Department) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Department]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DEPARTMENT_TYPE_URI,
        rdf_type_name=DEPARTMENT_TYPE_NAME, 
        kls=Department)

def departments_id_get(id):  # noqa: E501
    """Get a single Department by its id

    Gets the details of a given Department (more information in http://dbpedia.org/ontology/Department) # noqa: E501

    :param id: The ID of the Department to be retrieved
    :type id: str

    :rtype: Department
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DEPARTMENT_TYPE_URI,
        rdf_type_name=DEPARTMENT_TYPE_NAME, 
        kls=Department)
