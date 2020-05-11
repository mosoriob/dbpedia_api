import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PRODUCER_TYPE_NAME, PRODUCER_TYPE_URI

from openapi_server.models.producer import Producer  # noqa: E501
from openapi_server import util

def producers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Producer

    Gets a list of all instances of Producer (more information in http://dbpedia.org/ontology/Producer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Producer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PRODUCER_TYPE_URI,
        rdf_type_name=PRODUCER_TYPE_NAME, 
        kls=Producer)

def producers_id_get(id):  # noqa: E501
    """Get a single Producer by its id

    Gets the details of a given Producer (more information in http://dbpedia.org/ontology/Producer) # noqa: E501

    :param id: The ID of the Producer to be retrieved
    :type id: str

    :rtype: Producer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PRODUCER_TYPE_URI,
        rdf_type_name=PRODUCER_TYPE_NAME, 
        kls=Producer)
