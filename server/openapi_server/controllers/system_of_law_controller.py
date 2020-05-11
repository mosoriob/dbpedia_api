import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SYSTEMOFLAW_TYPE_NAME, SYSTEMOFLAW_TYPE_URI

from openapi_server.models.system_of_law import SystemOfLaw  # noqa: E501
from openapi_server import util

def systemoflaws_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SystemOfLaw

    Gets a list of all instances of SystemOfLaw (more information in http://dbpedia.org/ontology/SystemOfLaw) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SystemOfLaw]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SYSTEMOFLAW_TYPE_URI,
        rdf_type_name=SYSTEMOFLAW_TYPE_NAME, 
        kls=SystemOfLaw)

def systemoflaws_id_get(id):  # noqa: E501
    """Get a single SystemOfLaw by its id

    Gets the details of a given SystemOfLaw (more information in http://dbpedia.org/ontology/SystemOfLaw) # noqa: E501

    :param id: The ID of the SystemOfLaw to be retrieved
    :type id: str

    :rtype: SystemOfLaw
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SYSTEMOFLAW_TYPE_URI,
        rdf_type_name=SYSTEMOFLAW_TYPE_NAME, 
        kls=SystemOfLaw)
