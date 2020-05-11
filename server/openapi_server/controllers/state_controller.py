import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import STATE_TYPE_NAME, STATE_TYPE_URI

from openapi_server.models.state import State  # noqa: E501
from openapi_server import util

def states_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of State

    Gets a list of all instances of State (more information in http://dbpedia.org/ontology/State) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[State]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=STATE_TYPE_URI,
        rdf_type_name=STATE_TYPE_NAME, 
        kls=State)

def states_id_get(id):  # noqa: E501
    """Get a single State by its id

    Gets the details of a given State (more information in http://dbpedia.org/ontology/State) # noqa: E501

    :param id: The ID of the State to be retrieved
    :type id: str

    :rtype: State
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=STATE_TYPE_URI,
        rdf_type_name=STATE_TYPE_NAME, 
        kls=State)
