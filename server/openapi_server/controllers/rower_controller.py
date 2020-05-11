import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ROWER_TYPE_NAME, ROWER_TYPE_URI

from openapi_server.models.rower import Rower  # noqa: E501
from openapi_server import util

def rowers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Rower

    Gets a list of all instances of Rower (more information in http://dbpedia.org/ontology/Rower) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Rower]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ROWER_TYPE_URI,
        rdf_type_name=ROWER_TYPE_NAME, 
        kls=Rower)

def rowers_id_get(id):  # noqa: E501
    """Get a single Rower by its id

    Gets the details of a given Rower (more information in http://dbpedia.org/ontology/Rower) # noqa: E501

    :param id: The ID of the Rower to be retrieved
    :type id: str

    :rtype: Rower
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ROWER_TYPE_URI,
        rdf_type_name=ROWER_TYPE_NAME, 
        kls=Rower)
