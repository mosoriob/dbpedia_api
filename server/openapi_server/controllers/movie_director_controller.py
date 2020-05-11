import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOVIEDIRECTOR_TYPE_NAME, MOVIEDIRECTOR_TYPE_URI

from openapi_server.models.movie_director import MovieDirector  # noqa: E501
from openapi_server import util

def moviedirectors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MovieDirector

    Gets a list of all instances of MovieDirector (more information in http://dbpedia.org/ontology/MovieDirector) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MovieDirector]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOVIEDIRECTOR_TYPE_URI,
        rdf_type_name=MOVIEDIRECTOR_TYPE_NAME, 
        kls=MovieDirector)

def moviedirectors_id_get(id):  # noqa: E501
    """Get a single MovieDirector by its id

    Gets the details of a given MovieDirector (more information in http://dbpedia.org/ontology/MovieDirector) # noqa: E501

    :param id: The ID of the MovieDirector to be retrieved
    :type id: str

    :rtype: MovieDirector
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOVIEDIRECTOR_TYPE_URI,
        rdf_type_name=MOVIEDIRECTOR_TYPE_NAME, 
        kls=MovieDirector)
