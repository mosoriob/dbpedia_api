import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WINEREGION_TYPE_NAME, WINEREGION_TYPE_URI

from openapi_server.models.wine_region import WineRegion  # noqa: E501
from openapi_server import util

def wineregions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of WineRegion

    Gets a list of all instances of WineRegion (more information in http://dbpedia.org/ontology/WineRegion) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[WineRegion]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WINEREGION_TYPE_URI,
        rdf_type_name=WINEREGION_TYPE_NAME, 
        kls=WineRegion)

def wineregions_id_get(id):  # noqa: E501
    """Get a single WineRegion by its id

    Gets the details of a given WineRegion (more information in http://dbpedia.org/ontology/WineRegion) # noqa: E501

    :param id: The ID of the WineRegion to be retrieved
    :type id: str

    :rtype: WineRegion
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WINEREGION_TYPE_URI,
        rdf_type_name=WINEREGION_TYPE_NAME, 
        kls=WineRegion)
