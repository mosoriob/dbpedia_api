import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GUITARIST_TYPE_NAME, GUITARIST_TYPE_URI

from openapi_server.models.guitarist import Guitarist  # noqa: E501
from openapi_server import util

def guitarists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Guitarist

    Gets a list of all instances of Guitarist (more information in http://dbpedia.org/ontology/Guitarist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Guitarist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GUITARIST_TYPE_URI,
        rdf_type_name=GUITARIST_TYPE_NAME, 
        kls=Guitarist)

def guitarists_id_get(id):  # noqa: E501
    """Get a single Guitarist by its id

    Gets the details of a given Guitarist (more information in http://dbpedia.org/ontology/Guitarist) # noqa: E501

    :param id: The ID of the Guitarist to be retrieved
    :type id: str

    :rtype: Guitarist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GUITARIST_TYPE_URI,
        rdf_type_name=GUITARIST_TYPE_NAME, 
        kls=Guitarist)
