import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NOBLEFAMILY_TYPE_NAME, NOBLEFAMILY_TYPE_URI

from openapi_server.models.noble_family import NobleFamily  # noqa: E501
from openapi_server import util

def noblefamilys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NobleFamily

    Gets a list of all instances of NobleFamily (more information in http://dbpedia.org/ontology/NobleFamily) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NobleFamily]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NOBLEFAMILY_TYPE_URI,
        rdf_type_name=NOBLEFAMILY_TYPE_NAME, 
        kls=NobleFamily)

def noblefamilys_id_get(id):  # noqa: E501
    """Get a single NobleFamily by its id

    Gets the details of a given NobleFamily (more information in http://dbpedia.org/ontology/NobleFamily) # noqa: E501

    :param id: The ID of the NobleFamily to be retrieved
    :type id: str

    :rtype: NobleFamily
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NOBLEFAMILY_TYPE_URI,
        rdf_type_name=NOBLEFAMILY_TYPE_NAME, 
        kls=NobleFamily)
