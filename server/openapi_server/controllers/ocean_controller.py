import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import OCEAN_TYPE_NAME, OCEAN_TYPE_URI

from openapi_server.models.ocean import Ocean  # noqa: E501
from openapi_server import util

def oceans_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Ocean

    Gets a list of all instances of Ocean (more information in http://dbpedia.org/ontology/Ocean) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Ocean]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=OCEAN_TYPE_URI,
        rdf_type_name=OCEAN_TYPE_NAME, 
        kls=Ocean)

def oceans_id_get(id):  # noqa: E501
    """Get a single Ocean by its id

    Gets the details of a given Ocean (more information in http://dbpedia.org/ontology/Ocean) # noqa: E501

    :param id: The ID of the Ocean to be retrieved
    :type id: str

    :rtype: Ocean
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=OCEAN_TYPE_URI,
        rdf_type_name=OCEAN_TYPE_NAME, 
        kls=Ocean)
