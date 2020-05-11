import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MURDERER_TYPE_NAME, MURDERER_TYPE_URI

from openapi_server.models.murderer import Murderer  # noqa: E501
from openapi_server import util

def murderers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Murderer

    Gets a list of all instances of Murderer (more information in http://dbpedia.org/ontology/Murderer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Murderer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MURDERER_TYPE_URI,
        rdf_type_name=MURDERER_TYPE_NAME, 
        kls=Murderer)

def murderers_id_get(id):  # noqa: E501
    """Get a single Murderer by its id

    Gets the details of a given Murderer (more information in http://dbpedia.org/ontology/Murderer) # noqa: E501

    :param id: The ID of the Murderer to be retrieved
    :type id: str

    :rtype: Murderer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MURDERER_TYPE_URI,
        rdf_type_name=MURDERER_TYPE_NAME, 
        kls=Murderer)
