import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MINERAL_TYPE_NAME, MINERAL_TYPE_URI

from openapi_server.models.mineral import Mineral  # noqa: E501
from openapi_server import util

def minerals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Mineral

    Gets a list of all instances of Mineral (more information in http://dbpedia.org/ontology/Mineral) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Mineral]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MINERAL_TYPE_URI,
        rdf_type_name=MINERAL_TYPE_NAME, 
        kls=Mineral)

def minerals_id_get(id):  # noqa: E501
    """Get a single Mineral by its id

    Gets the details of a given Mineral (more information in http://dbpedia.org/ontology/Mineral) # noqa: E501

    :param id: The ID of the Mineral to be retrieved
    :type id: str

    :rtype: Mineral
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MINERAL_TYPE_URI,
        rdf_type_name=MINERAL_TYPE_NAME, 
        kls=Mineral)
