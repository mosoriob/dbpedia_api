import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SHRINE_TYPE_NAME, SHRINE_TYPE_URI

from openapi_server.models.shrine import Shrine  # noqa: E501
from openapi_server import util

def shrines_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Shrine

    Gets a list of all instances of Shrine (more information in http://dbpedia.org/ontology/Shrine) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Shrine]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SHRINE_TYPE_URI,
        rdf_type_name=SHRINE_TYPE_NAME, 
        kls=Shrine)

def shrines_id_get(id):  # noqa: E501
    """Get a single Shrine by its id

    Gets the details of a given Shrine (more information in http://dbpedia.org/ontology/Shrine) # noqa: E501

    :param id: The ID of the Shrine to be retrieved
    :type id: str

    :rtype: Shrine
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SHRINE_TYPE_URI,
        rdf_type_name=SHRINE_TYPE_NAME, 
        kls=Shrine)
