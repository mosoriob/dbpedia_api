import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import STAR_TYPE_NAME, STAR_TYPE_URI

from openapi_server.models.star import Star  # noqa: E501
from openapi_server import util

def stars_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Star

    Gets a list of all instances of Star (more information in http://dbpedia.org/ontology/Star) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Star]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=STAR_TYPE_URI,
        rdf_type_name=STAR_TYPE_NAME, 
        kls=Star)

def stars_id_get(id):  # noqa: E501
    """Get a single Star by its id

    Gets the details of a given Star (more information in http://dbpedia.org/ontology/Star) # noqa: E501

    :param id: The ID of the Star to be retrieved
    :type id: str

    :rtype: Star
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=STAR_TYPE_URI,
        rdf_type_name=STAR_TYPE_NAME, 
        kls=Star)
