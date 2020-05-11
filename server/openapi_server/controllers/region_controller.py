import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import REGION_TYPE_NAME, REGION_TYPE_URI

from openapi_server.models.region import Region  # noqa: E501
from openapi_server import util

def regions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Region

    Gets a list of all instances of Region (more information in http://dbpedia.org/ontology/Region) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Region]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)

def regions_id_get(id):  # noqa: E501
    """Get a single Region by its id

    Gets the details of a given Region (more information in http://dbpedia.org/ontology/Region) # noqa: E501

    :param id: The ID of the Region to be retrieved
    :type id: str

    :rtype: Region
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=REGION_TYPE_URI,
        rdf_type_name=REGION_TYPE_NAME, 
        kls=Region)
