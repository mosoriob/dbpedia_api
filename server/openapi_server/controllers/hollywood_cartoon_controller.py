import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HOLLYWOODCARTOON_TYPE_NAME, HOLLYWOODCARTOON_TYPE_URI

from openapi_server.models.hollywood_cartoon import HollywoodCartoon  # noqa: E501
from openapi_server import util

def hollywoodcartoons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HollywoodCartoon

    Gets a list of all instances of HollywoodCartoon (more information in http://dbpedia.org/ontology/HollywoodCartoon) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HollywoodCartoon]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HOLLYWOODCARTOON_TYPE_URI,
        rdf_type_name=HOLLYWOODCARTOON_TYPE_NAME, 
        kls=HollywoodCartoon)

def hollywoodcartoons_id_get(id):  # noqa: E501
    """Get a single HollywoodCartoon by its id

    Gets the details of a given HollywoodCartoon (more information in http://dbpedia.org/ontology/HollywoodCartoon) # noqa: E501

    :param id: The ID of the HollywoodCartoon to be retrieved
    :type id: str

    :rtype: HollywoodCartoon
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HOLLYWOODCARTOON_TYPE_URI,
        rdf_type_name=HOLLYWOODCARTOON_TYPE_NAME, 
        kls=HollywoodCartoon)
