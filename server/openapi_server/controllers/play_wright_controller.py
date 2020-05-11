import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PLAYWRIGHT_TYPE_NAME, PLAYWRIGHT_TYPE_URI

from openapi_server.models.play_wright import PlayWright  # noqa: E501
from openapi_server import util

def playwrights_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PlayWright

    Gets a list of all instances of PlayWright (more information in http://dbpedia.org/ontology/PlayWright) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PlayWright]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PLAYWRIGHT_TYPE_URI,
        rdf_type_name=PLAYWRIGHT_TYPE_NAME, 
        kls=PlayWright)

def playwrights_id_get(id):  # noqa: E501
    """Get a single PlayWright by its id

    Gets the details of a given PlayWright (more information in http://dbpedia.org/ontology/PlayWright) # noqa: E501

    :param id: The ID of the PlayWright to be retrieved
    :type id: str

    :rtype: PlayWright
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PLAYWRIGHT_TYPE_URI,
        rdf_type_name=PLAYWRIGHT_TYPE_NAME, 
        kls=PlayWright)
