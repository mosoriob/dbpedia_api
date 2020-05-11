import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ENGINEER_TYPE_NAME, ENGINEER_TYPE_URI

from openapi_server.models.engineer import Engineer  # noqa: E501
from openapi_server import util

def engineers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Engineer

    Gets a list of all instances of Engineer (more information in http://dbpedia.org/ontology/Engineer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Engineer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ENGINEER_TYPE_URI,
        rdf_type_name=ENGINEER_TYPE_NAME, 
        kls=Engineer)

def engineers_id_get(id):  # noqa: E501
    """Get a single Engineer by its id

    Gets the details of a given Engineer (more information in http://dbpedia.org/ontology/Engineer) # noqa: E501

    :param id: The ID of the Engineer to be retrieved
    :type id: str

    :rtype: Engineer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ENGINEER_TYPE_URI,
        rdf_type_name=ENGINEER_TYPE_NAME, 
        kls=Engineer)
