import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import THEATRE_TYPE_NAME, THEATRE_TYPE_URI

from openapi_server.models.theatre import Theatre  # noqa: E501
from openapi_server import util

def theatres_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Theatre

    Gets a list of all instances of Theatre (more information in http://dbpedia.org/ontology/Theatre) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Theatre]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=THEATRE_TYPE_URI,
        rdf_type_name=THEATRE_TYPE_NAME, 
        kls=Theatre)

def theatres_id_get(id):  # noqa: E501
    """Get a single Theatre by its id

    Gets the details of a given Theatre (more information in http://dbpedia.org/ontology/Theatre) # noqa: E501

    :param id: The ID of the Theatre to be retrieved
    :type id: str

    :rtype: Theatre
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=THEATRE_TYPE_URI,
        rdf_type_name=THEATRE_TYPE_NAME, 
        kls=Theatre)
