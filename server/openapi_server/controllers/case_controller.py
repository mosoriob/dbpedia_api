import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CASE_TYPE_NAME, CASE_TYPE_URI

from openapi_server.models.case import Case  # noqa: E501
from openapi_server import util

def cases_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Case

    Gets a list of all instances of Case (more information in http://dbpedia.org/ontology/Case) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Case]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CASE_TYPE_URI,
        rdf_type_name=CASE_TYPE_NAME, 
        kls=Case)

def cases_id_get(id):  # noqa: E501
    """Get a single Case by its id

    Gets the details of a given Case (more information in http://dbpedia.org/ontology/Case) # noqa: E501

    :param id: The ID of the Case to be retrieved
    :type id: str

    :rtype: Case
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CASE_TYPE_URI,
        rdf_type_name=CASE_TYPE_NAME, 
        kls=Case)
