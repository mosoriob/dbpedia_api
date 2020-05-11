import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import JOCKEY_TYPE_NAME, JOCKEY_TYPE_URI

from openapi_server.models.jockey import Jockey  # noqa: E501
from openapi_server import util

def jockeys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Jockey

    Gets a list of all instances of Jockey (more information in http://dbpedia.org/ontology/Jockey) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Jockey]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=JOCKEY_TYPE_URI,
        rdf_type_name=JOCKEY_TYPE_NAME, 
        kls=Jockey)

def jockeys_id_get(id):  # noqa: E501
    """Get a single Jockey by its id

    Gets the details of a given Jockey (more information in http://dbpedia.org/ontology/Jockey) # noqa: E501

    :param id: The ID of the Jockey to be retrieved
    :type id: str

    :rtype: Jockey
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=JOCKEY_TYPE_URI,
        rdf_type_name=JOCKEY_TYPE_NAME, 
        kls=Jockey)
