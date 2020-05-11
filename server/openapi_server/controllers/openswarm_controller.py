import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import OPENSWARM_TYPE_NAME, OPENSWARM_TYPE_URI

from openapi_server.models.openswarm import Openswarm  # noqa: E501
from openapi_server import util

def openswarms_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of openswarm

    Gets a list of all instances of openswarm (more information in http://dbpedia.org/ontology/openswarm) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Openswarm]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=OPENSWARM_TYPE_URI,
        rdf_type_name=OPENSWARM_TYPE_NAME, 
        kls=Openswarm)

def openswarms_id_get(id):  # noqa: E501
    """Get a single openswarm by its id

    Gets the details of a given openswarm (more information in http://dbpedia.org/ontology/openswarm) # noqa: E501

    :param id: The ID of the openswarm to be retrieved
    :type id: str

    :rtype: Openswarm
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=OPENSWARM_TYPE_URI,
        rdf_type_name=OPENSWARM_TYPE_NAME, 
        kls=Openswarm)
