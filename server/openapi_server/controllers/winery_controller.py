import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WINERY_TYPE_NAME, WINERY_TYPE_URI

from openapi_server.models.winery import Winery  # noqa: E501
from openapi_server import util

def winerys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Winery

    Gets a list of all instances of Winery (more information in http://dbpedia.org/ontology/Winery) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Winery]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WINERY_TYPE_URI,
        rdf_type_name=WINERY_TYPE_NAME, 
        kls=Winery)

def winerys_id_get(id):  # noqa: E501
    """Get a single Winery by its id

    Gets the details of a given Winery (more information in http://dbpedia.org/ontology/Winery) # noqa: E501

    :param id: The ID of the Winery to be retrieved
    :type id: str

    :rtype: Winery
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WINERY_TYPE_URI,
        rdf_type_name=WINERY_TYPE_NAME, 
        kls=Winery)
