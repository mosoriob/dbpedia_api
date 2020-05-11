import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RELIGIOUS_TYPE_NAME, RELIGIOUS_TYPE_URI

from openapi_server.models.religious import Religious  # noqa: E501
from openapi_server import util

def religiouss_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Religious

    Gets a list of all instances of Religious (more information in http://dbpedia.org/ontology/Religious) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Religious]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RELIGIOUS_TYPE_URI,
        rdf_type_name=RELIGIOUS_TYPE_NAME, 
        kls=Religious)

def religiouss_id_get(id):  # noqa: E501
    """Get a single Religious by its id

    Gets the details of a given Religious (more information in http://dbpedia.org/ontology/Religious) # noqa: E501

    :param id: The ID of the Religious to be retrieved
    :type id: str

    :rtype: Religious
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RELIGIOUS_TYPE_URI,
        rdf_type_name=RELIGIOUS_TYPE_NAME, 
        kls=Religious)
