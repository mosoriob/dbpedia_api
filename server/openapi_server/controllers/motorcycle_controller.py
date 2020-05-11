import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOTORCYCLE_TYPE_NAME, MOTORCYCLE_TYPE_URI

from openapi_server.models.motorcycle import Motorcycle  # noqa: E501
from openapi_server import util

def motorcycles_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Motorcycle

    Gets a list of all instances of Motorcycle (more information in http://dbpedia.org/ontology/Motorcycle) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Motorcycle]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOTORCYCLE_TYPE_URI,
        rdf_type_name=MOTORCYCLE_TYPE_NAME, 
        kls=Motorcycle)

def motorcycles_id_get(id):  # noqa: E501
    """Get a single Motorcycle by its id

    Gets the details of a given Motorcycle (more information in http://dbpedia.org/ontology/Motorcycle) # noqa: E501

    :param id: The ID of the Motorcycle to be retrieved
    :type id: str

    :rtype: Motorcycle
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOTORCYCLE_TYPE_URI,
        rdf_type_name=MOTORCYCLE_TYPE_NAME, 
        kls=Motorcycle)
