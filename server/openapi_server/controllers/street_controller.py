import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import STREET_TYPE_NAME, STREET_TYPE_URI

from openapi_server.models.street import Street  # noqa: E501
from openapi_server import util

def streets_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Street

    Gets a list of all instances of Street (more information in http://dbpedia.org/ontology/Street) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Street]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=STREET_TYPE_URI,
        rdf_type_name=STREET_TYPE_NAME, 
        kls=Street)

def streets_id_get(id):  # noqa: E501
    """Get a single Street by its id

    Gets the details of a given Street (more information in http://dbpedia.org/ontology/Street) # noqa: E501

    :param id: The ID of the Street to be retrieved
    :type id: str

    :rtype: Street
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=STREET_TYPE_URI,
        rdf_type_name=STREET_TYPE_NAME, 
        kls=Street)
