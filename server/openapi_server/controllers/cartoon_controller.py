import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CARTOON_TYPE_NAME, CARTOON_TYPE_URI

from openapi_server.models.cartoon import Cartoon  # noqa: E501
from openapi_server import util

def cartoons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Cartoon

    Gets a list of all instances of Cartoon (more information in http://dbpedia.org/ontology/Cartoon) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Cartoon]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CARTOON_TYPE_URI,
        rdf_type_name=CARTOON_TYPE_NAME, 
        kls=Cartoon)

def cartoons_id_get(id):  # noqa: E501
    """Get a single Cartoon by its id

    Gets the details of a given Cartoon (more information in http://dbpedia.org/ontology/Cartoon) # noqa: E501

    :param id: The ID of the Cartoon to be retrieved
    :type id: str

    :rtype: Cartoon
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CARTOON_TYPE_URI,
        rdf_type_name=CARTOON_TYPE_NAME, 
        kls=Cartoon)
