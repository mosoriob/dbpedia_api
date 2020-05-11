import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VICEPRESIDENT_TYPE_NAME, VICEPRESIDENT_TYPE_URI

from openapi_server.models.vice_president import VicePresident  # noqa: E501
from openapi_server import util

def vicepresidents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of VicePresident

    Gets a list of all instances of VicePresident (more information in http://dbpedia.org/ontology/VicePresident) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[VicePresident]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VICEPRESIDENT_TYPE_URI,
        rdf_type_name=VICEPRESIDENT_TYPE_NAME, 
        kls=VicePresident)

def vicepresidents_id_get(id):  # noqa: E501
    """Get a single VicePresident by its id

    Gets the details of a given VicePresident (more information in http://dbpedia.org/ontology/VicePresident) # noqa: E501

    :param id: The ID of the VicePresident to be retrieved
    :type id: str

    :rtype: VicePresident
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VICEPRESIDENT_TYPE_URI,
        rdf_type_name=VICEPRESIDENT_TYPE_NAME, 
        kls=VicePresident)
