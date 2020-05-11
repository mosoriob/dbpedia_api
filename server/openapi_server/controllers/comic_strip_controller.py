import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COMICSTRIP_TYPE_NAME, COMICSTRIP_TYPE_URI

from openapi_server.models.comic_strip import ComicStrip  # noqa: E501
from openapi_server import util

def comicstrips_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ComicStrip

    Gets a list of all instances of ComicStrip (more information in http://dbpedia.org/ontology/ComicStrip) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ComicStrip]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COMICSTRIP_TYPE_URI,
        rdf_type_name=COMICSTRIP_TYPE_NAME, 
        kls=ComicStrip)

def comicstrips_id_get(id):  # noqa: E501
    """Get a single ComicStrip by its id

    Gets the details of a given ComicStrip (more information in http://dbpedia.org/ontology/ComicStrip) # noqa: E501

    :param id: The ID of the ComicStrip to be retrieved
    :type id: str

    :rtype: ComicStrip
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COMICSTRIP_TYPE_URI,
        rdf_type_name=COMICSTRIP_TYPE_NAME, 
        kls=ComicStrip)
