import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MUSICAL_TYPE_NAME, MUSICAL_TYPE_URI

from openapi_server.models.musical import Musical  # noqa: E501
from openapi_server import util

def musicals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Musical

    Gets a list of all instances of Musical (more information in http://dbpedia.org/ontology/Musical) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Musical]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MUSICAL_TYPE_URI,
        rdf_type_name=MUSICAL_TYPE_NAME, 
        kls=Musical)

def musicals_id_get(id):  # noqa: E501
    """Get a single Musical by its id

    Gets the details of a given Musical (more information in http://dbpedia.org/ontology/Musical) # noqa: E501

    :param id: The ID of the Musical to be retrieved
    :type id: str

    :rtype: Musical
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MUSICAL_TYPE_URI,
        rdf_type_name=MUSICAL_TYPE_NAME, 
        kls=Musical)
