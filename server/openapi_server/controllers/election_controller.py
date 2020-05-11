import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ELECTION_TYPE_NAME, ELECTION_TYPE_URI

from openapi_server.models.election import Election  # noqa: E501
from openapi_server import util

def elections_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Election

    Gets a list of all instances of Election (more information in http://dbpedia.org/ontology/Election) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Election]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ELECTION_TYPE_URI,
        rdf_type_name=ELECTION_TYPE_NAME, 
        kls=Election)

def elections_id_get(id):  # noqa: E501
    """Get a single Election by its id

    Gets the details of a given Election (more information in http://dbpedia.org/ontology/Election) # noqa: E501

    :param id: The ID of the Election to be retrieved
    :type id: str

    :rtype: Election
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ELECTION_TYPE_URI,
        rdf_type_name=ELECTION_TYPE_NAME, 
        kls=Election)
