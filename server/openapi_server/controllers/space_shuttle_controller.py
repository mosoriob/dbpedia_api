import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPACESHUTTLE_TYPE_NAME, SPACESHUTTLE_TYPE_URI

from openapi_server.models.space_shuttle import SpaceShuttle  # noqa: E501
from openapi_server import util

def spaceshuttles_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SpaceShuttle

    Gets a list of all instances of SpaceShuttle (more information in http://dbpedia.org/ontology/SpaceShuttle) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SpaceShuttle]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPACESHUTTLE_TYPE_URI,
        rdf_type_name=SPACESHUTTLE_TYPE_NAME, 
        kls=SpaceShuttle)

def spaceshuttles_id_get(id):  # noqa: E501
    """Get a single SpaceShuttle by its id

    Gets the details of a given SpaceShuttle (more information in http://dbpedia.org/ontology/SpaceShuttle) # noqa: E501

    :param id: The ID of the SpaceShuttle to be retrieved
    :type id: str

    :rtype: SpaceShuttle
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPACESHUTTLE_TYPE_URI,
        rdf_type_name=SPACESHUTTLE_TYPE_NAME, 
        kls=SpaceShuttle)
