import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOUNTAINPASS_TYPE_NAME, MOUNTAINPASS_TYPE_URI

from openapi_server.models.mountain_pass import MountainPass  # noqa: E501
from openapi_server import util

def mountainpasss_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MountainPass

    Gets a list of all instances of MountainPass (more information in http://dbpedia.org/ontology/MountainPass) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MountainPass]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOUNTAINPASS_TYPE_URI,
        rdf_type_name=MOUNTAINPASS_TYPE_NAME, 
        kls=MountainPass)

def mountainpasss_id_get(id):  # noqa: E501
    """Get a single MountainPass by its id

    Gets the details of a given MountainPass (more information in http://dbpedia.org/ontology/MountainPass) # noqa: E501

    :param id: The ID of the MountainPass to be retrieved
    :type id: str

    :rtype: MountainPass
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOUNTAINPASS_TYPE_URI,
        rdf_type_name=MOUNTAINPASS_TYPE_NAME, 
        kls=MountainPass)
