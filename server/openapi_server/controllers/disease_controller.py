import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DISEASE_TYPE_NAME, DISEASE_TYPE_URI

from openapi_server.models.disease import Disease  # noqa: E501
from openapi_server import util

def diseases_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Disease

    Gets a list of all instances of Disease (more information in http://dbpedia.org/ontology/Disease) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Disease]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DISEASE_TYPE_URI,
        rdf_type_name=DISEASE_TYPE_NAME, 
        kls=Disease)

def diseases_id_get(id):  # noqa: E501
    """Get a single Disease by its id

    Gets the details of a given Disease (more information in http://dbpedia.org/ontology/Disease) # noqa: E501

    :param id: The ID of the Disease to be retrieved
    :type id: str

    :rtype: Disease
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DISEASE_TYPE_URI,
        rdf_type_name=DISEASE_TYPE_NAME, 
        kls=Disease)
