import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DRAMA_TYPE_NAME, DRAMA_TYPE_URI

from openapi_server.models.drama import Drama  # noqa: E501
from openapi_server import util

def dramas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Drama

    Gets a list of all instances of Drama (more information in http://dbpedia.org/ontology/Drama) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Drama]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DRAMA_TYPE_URI,
        rdf_type_name=DRAMA_TYPE_NAME, 
        kls=Drama)

def dramas_id_get(id):  # noqa: E501
    """Get a single Drama by its id

    Gets the details of a given Drama (more information in http://dbpedia.org/ontology/Drama) # noqa: E501

    :param id: The ID of the Drama to be retrieved
    :type id: str

    :rtype: Drama
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DRAMA_TYPE_URI,
        rdf_type_name=DRAMA_TYPE_NAME, 
        kls=Drama)
