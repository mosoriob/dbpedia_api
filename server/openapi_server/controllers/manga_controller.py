import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MANGA_TYPE_NAME, MANGA_TYPE_URI

from openapi_server.models.manga import Manga  # noqa: E501
from openapi_server import util

def mangas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Manga

    Gets a list of all instances of Manga (more information in http://dbpedia.org/ontology/Manga) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Manga]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MANGA_TYPE_URI,
        rdf_type_name=MANGA_TYPE_NAME, 
        kls=Manga)

def mangas_id_get(id):  # noqa: E501
    """Get a single Manga by its id

    Gets the details of a given Manga (more information in http://dbpedia.org/ontology/Manga) # noqa: E501

    :param id: The ID of the Manga to be retrieved
    :type id: str

    :rtype: Manga
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MANGA_TYPE_URI,
        rdf_type_name=MANGA_TYPE_NAME, 
        kls=Manga)
