import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import IMAGE_TYPE_NAME, IMAGE_TYPE_URI

from openapi_server.models.image import Image  # noqa: E501
from openapi_server import util

def images_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Image

    Gets a list of all instances of Image (more information in http://dbpedia.org/ontology/Image) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Image]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)

def images_id_get(id):  # noqa: E501
    """Get a single Image by its id

    Gets the details of a given Image (more information in http://dbpedia.org/ontology/Image) # noqa: E501

    :param id: The ID of the Image to be retrieved
    :type id: str

    :rtype: Image
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=IMAGE_TYPE_URI,
        rdf_type_name=IMAGE_TYPE_NAME, 
        kls=Image)
