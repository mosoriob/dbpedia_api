import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOVINGIMAGE_TYPE_NAME, MOVINGIMAGE_TYPE_URI

from openapi_server.models.moving_image import MovingImage  # noqa: E501
from openapi_server import util

def movingimages_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MovingImage

    Gets a list of all instances of MovingImage (more information in http://dbpedia.org/ontology/MovingImage) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MovingImage]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOVINGIMAGE_TYPE_URI,
        rdf_type_name=MOVINGIMAGE_TYPE_NAME, 
        kls=MovingImage)

def movingimages_id_get(id):  # noqa: E501
    """Get a single MovingImage by its id

    Gets the details of a given MovingImage (more information in http://dbpedia.org/ontology/MovingImage) # noqa: E501

    :param id: The ID of the MovingImage to be retrieved
    :type id: str

    :rtype: MovingImage
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOVINGIMAGE_TYPE_URI,
        rdf_type_name=MOVINGIMAGE_TYPE_NAME, 
        kls=MovingImage)
