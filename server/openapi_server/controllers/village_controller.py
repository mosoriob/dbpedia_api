import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VILLAGE_TYPE_NAME, VILLAGE_TYPE_URI

from openapi_server.models.village import Village  # noqa: E501
from openapi_server import util

def villages_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Village

    Gets a list of all instances of Village (more information in http://dbpedia.org/ontology/Village) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Village]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VILLAGE_TYPE_URI,
        rdf_type_name=VILLAGE_TYPE_NAME, 
        kls=Village)

def villages_id_get(id):  # noqa: E501
    """Get a single Village by its id

    Gets the details of a given Village (more information in http://dbpedia.org/ontology/Village) # noqa: E501

    :param id: The ID of the Village to be retrieved
    :type id: str

    :rtype: Village
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VILLAGE_TYPE_URI,
        rdf_type_name=VILLAGE_TYPE_NAME, 
        kls=Village)
