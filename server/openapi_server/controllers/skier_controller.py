import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SKIER_TYPE_NAME, SKIER_TYPE_URI

from openapi_server.models.skier import Skier  # noqa: E501
from openapi_server import util

def skiers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Skier

    Gets a list of all instances of Skier (more information in http://dbpedia.org/ontology/Skier) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Skier]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SKIER_TYPE_URI,
        rdf_type_name=SKIER_TYPE_NAME, 
        kls=Skier)

def skiers_id_get(id):  # noqa: E501
    """Get a single Skier by its id

    Gets the details of a given Skier (more information in http://dbpedia.org/ontology/Skier) # noqa: E501

    :param id: The ID of the Skier to be retrieved
    :type id: str

    :rtype: Skier
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SKIER_TYPE_URI,
        rdf_type_name=SKIER_TYPE_NAME, 
        kls=Skier)
