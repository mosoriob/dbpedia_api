import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SWARM_TYPE_NAME, SWARM_TYPE_URI

from openapi_server.models.swarm import Swarm  # noqa: E501
from openapi_server import util

def swarms_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Swarm

    Gets a list of all instances of Swarm (more information in http://dbpedia.org/ontology/Swarm) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Swarm]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SWARM_TYPE_URI,
        rdf_type_name=SWARM_TYPE_NAME, 
        kls=Swarm)

def swarms_id_get(id):  # noqa: E501
    """Get a single Swarm by its id

    Gets the details of a given Swarm (more information in http://dbpedia.org/ontology/Swarm) # noqa: E501

    :param id: The ID of the Swarm to be retrieved
    :type id: str

    :rtype: Swarm
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SWARM_TYPE_URI,
        rdf_type_name=SWARM_TYPE_NAME, 
        kls=Swarm)
