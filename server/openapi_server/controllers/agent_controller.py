import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AGENT_TYPE_NAME, AGENT_TYPE_URI

from openapi_server.models.agent import Agent  # noqa: E501
from openapi_server import util

def agents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Agent

    Gets a list of all instances of Agent (more information in http://dbpedia.org/ontology/Agent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Agent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AGENT_TYPE_URI,
        rdf_type_name=AGENT_TYPE_NAME, 
        kls=Agent)

def agents_id_get(id):  # noqa: E501
    """Get a single Agent by its id

    Gets the details of a given Agent (more information in http://dbpedia.org/ontology/Agent) # noqa: E501

    :param id: The ID of the Agent to be retrieved
    :type id: str

    :rtype: Agent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AGENT_TYPE_URI,
        rdf_type_name=AGENT_TYPE_NAME, 
        kls=Agent)
