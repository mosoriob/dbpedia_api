import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PLAY_TYPE_NAME, PLAY_TYPE_URI

from openapi_server.models.play import Play  # noqa: E501
from openapi_server import util

def plays_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Play

    Gets a list of all instances of Play (more information in http://dbpedia.org/ontology/Play) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Play]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PLAY_TYPE_URI,
        rdf_type_name=PLAY_TYPE_NAME, 
        kls=Play)

def plays_id_get(id):  # noqa: E501
    """Get a single Play by its id

    Gets the details of a given Play (more information in http://dbpedia.org/ontology/Play) # noqa: E501

    :param id: The ID of the Play to be retrieved
    :type id: str

    :rtype: Play
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PLAY_TYPE_URI,
        rdf_type_name=PLAY_TYPE_NAME, 
        kls=Play)
