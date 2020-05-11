import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GNETOPHYTES_TYPE_NAME, GNETOPHYTES_TYPE_URI

from openapi_server.models.gnetophytes import Gnetophytes  # noqa: E501
from openapi_server import util

def gnetophytess_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Gnetophytes

    Gets a list of all instances of Gnetophytes (more information in http://dbpedia.org/ontology/Gnetophytes) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Gnetophytes]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GNETOPHYTES_TYPE_URI,
        rdf_type_name=GNETOPHYTES_TYPE_NAME, 
        kls=Gnetophytes)

def gnetophytess_id_get(id):  # noqa: E501
    """Get a single Gnetophytes by its id

    Gets the details of a given Gnetophytes (more information in http://dbpedia.org/ontology/Gnetophytes) # noqa: E501

    :param id: The ID of the Gnetophytes to be retrieved
    :type id: str

    :rtype: Gnetophytes
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GNETOPHYTES_TYPE_URI,
        rdf_type_name=GNETOPHYTES_TYPE_NAME, 
        kls=Gnetophytes)
