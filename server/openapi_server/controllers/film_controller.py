import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FILM_TYPE_NAME, FILM_TYPE_URI

from openapi_server.models.film import Film  # noqa: E501
from openapi_server import util

def films_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Film

    Gets a list of all instances of Film (more information in http://dbpedia.org/ontology/Film) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Film]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FILM_TYPE_URI,
        rdf_type_name=FILM_TYPE_NAME, 
        kls=Film)

def films_id_get(id):  # noqa: E501
    """Get a single Film by its id

    Gets the details of a given Film (more information in http://dbpedia.org/ontology/Film) # noqa: E501

    :param id: The ID of the Film to be retrieved
    :type id: str

    :rtype: Film
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FILM_TYPE_URI,
        rdf_type_name=FILM_TYPE_NAME, 
        kls=Film)
