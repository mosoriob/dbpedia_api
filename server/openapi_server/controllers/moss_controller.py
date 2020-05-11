import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOSS_TYPE_NAME, MOSS_TYPE_URI

from openapi_server.models.moss import Moss  # noqa: E501
from openapi_server import util

def mosss_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Moss

    Gets a list of all instances of Moss (more information in http://dbpedia.org/ontology/Moss) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Moss]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOSS_TYPE_URI,
        rdf_type_name=MOSS_TYPE_NAME, 
        kls=Moss)

def mosss_id_get(id):  # noqa: E501
    """Get a single Moss by its id

    Gets the details of a given Moss (more information in http://dbpedia.org/ontology/Moss) # noqa: E501

    :param id: The ID of the Moss to be retrieved
    :type id: str

    :rtype: Moss
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOSS_TYPE_URI,
        rdf_type_name=MOSS_TYPE_NAME, 
        kls=Moss)
