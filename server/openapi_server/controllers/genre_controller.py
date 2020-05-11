import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GENRE_TYPE_NAME, GENRE_TYPE_URI

from openapi_server.models.genre import Genre  # noqa: E501
from openapi_server import util

def genres_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Genre

    Gets a list of all instances of Genre (more information in http://dbpedia.org/ontology/Genre) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Genre]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GENRE_TYPE_URI,
        rdf_type_name=GENRE_TYPE_NAME, 
        kls=Genre)

def genres_id_get(id):  # noqa: E501
    """Get a single Genre by its id

    Gets the details of a given Genre (more information in http://dbpedia.org/ontology/Genre) # noqa: E501

    :param id: The ID of the Genre to be retrieved
    :type id: str

    :rtype: Genre
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GENRE_TYPE_URI,
        rdf_type_name=GENRE_TYPE_NAME, 
        kls=Genre)
