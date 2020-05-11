import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HOTSPRING_TYPE_NAME, HOTSPRING_TYPE_URI

from openapi_server.models.hot_spring import HotSpring  # noqa: E501
from openapi_server import util

def hotsprings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HotSpring

    Gets a list of all instances of HotSpring (more information in http://dbpedia.org/ontology/HotSpring) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HotSpring]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HOTSPRING_TYPE_URI,
        rdf_type_name=HOTSPRING_TYPE_NAME, 
        kls=HotSpring)

def hotsprings_id_get(id):  # noqa: E501
    """Get a single HotSpring by its id

    Gets the details of a given HotSpring (more information in http://dbpedia.org/ontology/HotSpring) # noqa: E501

    :param id: The ID of the HotSpring to be retrieved
    :type id: str

    :rtype: HotSpring
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HOTSPRING_TYPE_URI,
        rdf_type_name=HOTSPRING_TYPE_NAME, 
        kls=HotSpring)
