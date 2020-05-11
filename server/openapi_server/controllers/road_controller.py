import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ROAD_TYPE_NAME, ROAD_TYPE_URI

from openapi_server.models.road import Road  # noqa: E501
from openapi_server import util

def roads_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Road

    Gets a list of all instances of Road (more information in http://dbpedia.org/ontology/Road) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Road]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ROAD_TYPE_URI,
        rdf_type_name=ROAD_TYPE_NAME, 
        kls=Road)

def roads_id_get(id):  # noqa: E501
    """Get a single Road by its id

    Gets the details of a given Road (more information in http://dbpedia.org/ontology/Road) # noqa: E501

    :param id: The ID of the Road to be retrieved
    :type id: str

    :rtype: Road
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ROAD_TYPE_URI,
        rdf_type_name=ROAD_TYPE_NAME, 
        kls=Road)
