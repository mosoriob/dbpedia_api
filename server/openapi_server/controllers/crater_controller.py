import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CRATER_TYPE_NAME, CRATER_TYPE_URI

from openapi_server.models.crater import Crater  # noqa: E501
from openapi_server import util

def craters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Crater

    Gets a list of all instances of Crater (more information in http://dbpedia.org/ontology/Crater) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Crater]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CRATER_TYPE_URI,
        rdf_type_name=CRATER_TYPE_NAME, 
        kls=Crater)

def craters_id_get(id):  # noqa: E501
    """Get a single Crater by its id

    Gets the details of a given Crater (more information in http://dbpedia.org/ontology/Crater) # noqa: E501

    :param id: The ID of the Crater to be retrieved
    :type id: str

    :rtype: Crater
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CRATER_TYPE_URI,
        rdf_type_name=CRATER_TYPE_NAME, 
        kls=Crater)
