import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SINGER_TYPE_NAME, SINGER_TYPE_URI

from openapi_server.models.singer import Singer  # noqa: E501
from openapi_server import util

def singers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Singer

    Gets a list of all instances of Singer (more information in http://dbpedia.org/ontology/Singer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Singer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SINGER_TYPE_URI,
        rdf_type_name=SINGER_TYPE_NAME, 
        kls=Singer)

def singers_id_get(id):  # noqa: E501
    """Get a single Singer by its id

    Gets the details of a given Singer (more information in http://dbpedia.org/ontology/Singer) # noqa: E501

    :param id: The ID of the Singer to be retrieved
    :type id: str

    :rtype: Singer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SINGER_TYPE_URI,
        rdf_type_name=SINGER_TYPE_NAME, 
        kls=Singer)
