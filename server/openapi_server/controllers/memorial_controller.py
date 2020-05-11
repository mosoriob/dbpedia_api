import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MEMORIAL_TYPE_NAME, MEMORIAL_TYPE_URI

from openapi_server.models.memorial import Memorial  # noqa: E501
from openapi_server import util

def memorials_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Memorial

    Gets a list of all instances of Memorial (more information in http://dbpedia.org/ontology/Memorial) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Memorial]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MEMORIAL_TYPE_URI,
        rdf_type_name=MEMORIAL_TYPE_NAME, 
        kls=Memorial)

def memorials_id_get(id):  # noqa: E501
    """Get a single Memorial by its id

    Gets the details of a given Memorial (more information in http://dbpedia.org/ontology/Memorial) # noqa: E501

    :param id: The ID of the Memorial to be retrieved
    :type id: str

    :rtype: Memorial
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MEMORIAL_TYPE_URI,
        rdf_type_name=MEMORIAL_TYPE_NAME, 
        kls=Memorial)
