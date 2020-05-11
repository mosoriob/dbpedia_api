import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GYMNAST_TYPE_NAME, GYMNAST_TYPE_URI

from openapi_server.models.gymnast import Gymnast  # noqa: E501
from openapi_server import util

def gymnasts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Gymnast

    Gets a list of all instances of Gymnast (more information in http://dbpedia.org/ontology/Gymnast) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Gymnast]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GYMNAST_TYPE_URI,
        rdf_type_name=GYMNAST_TYPE_NAME, 
        kls=Gymnast)

def gymnasts_id_get(id):  # noqa: E501
    """Get a single Gymnast by its id

    Gets the details of a given Gymnast (more information in http://dbpedia.org/ontology/Gymnast) # noqa: E501

    :param id: The ID of the Gymnast to be retrieved
    :type id: str

    :rtype: Gymnast
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GYMNAST_TYPE_URI,
        rdf_type_name=GYMNAST_TYPE_NAME, 
        kls=Gymnast)
