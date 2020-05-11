import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PHILOSOPHER_TYPE_NAME, PHILOSOPHER_TYPE_URI

from openapi_server.models.philosopher import Philosopher  # noqa: E501
from openapi_server import util

def philosophers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Philosopher

    Gets a list of all instances of Philosopher (more information in http://dbpedia.org/ontology/Philosopher) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Philosopher]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PHILOSOPHER_TYPE_URI,
        rdf_type_name=PHILOSOPHER_TYPE_NAME, 
        kls=Philosopher)

def philosophers_id_get(id):  # noqa: E501
    """Get a single Philosopher by its id

    Gets the details of a given Philosopher (more information in http://dbpedia.org/ontology/Philosopher) # noqa: E501

    :param id: The ID of the Philosopher to be retrieved
    :type id: str

    :rtype: Philosopher
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PHILOSOPHER_TYPE_URI,
        rdf_type_name=PHILOSOPHER_TYPE_NAME, 
        kls=Philosopher)
