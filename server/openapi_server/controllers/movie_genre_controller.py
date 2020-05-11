import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOVIEGENRE_TYPE_NAME, MOVIEGENRE_TYPE_URI

from openapi_server.models.movie_genre import MovieGenre  # noqa: E501
from openapi_server import util

def moviegenres_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MovieGenre

    Gets a list of all instances of MovieGenre (more information in http://dbpedia.org/ontology/MovieGenre) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MovieGenre]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOVIEGENRE_TYPE_URI,
        rdf_type_name=MOVIEGENRE_TYPE_NAME, 
        kls=MovieGenre)

def moviegenres_id_get(id):  # noqa: E501
    """Get a single MovieGenre by its id

    Gets the details of a given MovieGenre (more information in http://dbpedia.org/ontology/MovieGenre) # noqa: E501

    :param id: The ID of the MovieGenre to be retrieved
    :type id: str

    :rtype: MovieGenre
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOVIEGENRE_TYPE_URI,
        rdf_type_name=MOVIEGENRE_TYPE_NAME, 
        kls=MovieGenre)
