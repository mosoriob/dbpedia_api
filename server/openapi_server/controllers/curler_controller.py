import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CURLER_TYPE_NAME, CURLER_TYPE_URI

from openapi_server.models.curler import Curler  # noqa: E501
from openapi_server import util

def curlers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Curler

    Gets a list of all instances of Curler (more information in http://dbpedia.org/ontology/Curler) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Curler]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CURLER_TYPE_URI,
        rdf_type_name=CURLER_TYPE_NAME, 
        kls=Curler)

def curlers_id_get(id):  # noqa: E501
    """Get a single Curler by its id

    Gets the details of a given Curler (more information in http://dbpedia.org/ontology/Curler) # noqa: E501

    :param id: The ID of the Curler to be retrieved
    :type id: str

    :rtype: Curler
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CURLER_TYPE_URI,
        rdf_type_name=CURLER_TYPE_NAME, 
        kls=Curler)
