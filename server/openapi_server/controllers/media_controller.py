import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MEDIA_TYPE_NAME, MEDIA_TYPE_URI

from openapi_server.models.media import Media  # noqa: E501
from openapi_server import util

def medias_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Media

    Gets a list of all instances of Media (more information in http://dbpedia.org/ontology/Media) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Media]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MEDIA_TYPE_URI,
        rdf_type_name=MEDIA_TYPE_NAME, 
        kls=Media)

def medias_id_get(id):  # noqa: E501
    """Get a single Media by its id

    Gets the details of a given Media (more information in http://dbpedia.org/ontology/Media) # noqa: E501

    :param id: The ID of the Media to be retrieved
    :type id: str

    :rtype: Media
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MEDIA_TYPE_URI,
        rdf_type_name=MEDIA_TYPE_NAME, 
        kls=Media)
