import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BRAIN_TYPE_NAME, BRAIN_TYPE_URI

from openapi_server.models.brain import Brain  # noqa: E501
from openapi_server import util

def brains_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Brain

    Gets a list of all instances of Brain (more information in http://dbpedia.org/ontology/Brain) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Brain]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BRAIN_TYPE_URI,
        rdf_type_name=BRAIN_TYPE_NAME, 
        kls=Brain)

def brains_id_get(id):  # noqa: E501
    """Get a single Brain by its id

    Gets the details of a given Brain (more information in http://dbpedia.org/ontology/Brain) # noqa: E501

    :param id: The ID of the Brain to be retrieved
    :type id: str

    :rtype: Brain
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BRAIN_TYPE_URI,
        rdf_type_name=BRAIN_TYPE_NAME, 
        kls=Brain)
