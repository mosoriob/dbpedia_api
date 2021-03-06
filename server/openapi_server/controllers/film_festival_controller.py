import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FILMFESTIVAL_TYPE_NAME, FILMFESTIVAL_TYPE_URI

from openapi_server.models.film_festival import FilmFestival  # noqa: E501
from openapi_server import util

def filmfestivals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FilmFestival

    Gets a list of all instances of FilmFestival (more information in http://dbpedia.org/ontology/FilmFestival) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FilmFestival]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FILMFESTIVAL_TYPE_URI,
        rdf_type_name=FILMFESTIVAL_TYPE_NAME, 
        kls=FilmFestival)

def filmfestivals_id_get(id):  # noqa: E501
    """Get a single FilmFestival by its id

    Gets the details of a given FilmFestival (more information in http://dbpedia.org/ontology/FilmFestival) # noqa: E501

    :param id: The ID of the FilmFestival to be retrieved
    :type id: str

    :rtype: FilmFestival
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FILMFESTIVAL_TYPE_URI,
        rdf_type_name=FILMFESTIVAL_TYPE_NAME, 
        kls=FilmFestival)
