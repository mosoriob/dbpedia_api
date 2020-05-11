import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PLAYBOYPLAYMATE_TYPE_NAME, PLAYBOYPLAYMATE_TYPE_URI

from openapi_server.models.playboy_playmate import PlayboyPlaymate  # noqa: E501
from openapi_server import util

def playboyplaymates_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PlayboyPlaymate

    Gets a list of all instances of PlayboyPlaymate (more information in http://dbpedia.org/ontology/PlayboyPlaymate) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PlayboyPlaymate]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PLAYBOYPLAYMATE_TYPE_URI,
        rdf_type_name=PLAYBOYPLAYMATE_TYPE_NAME, 
        kls=PlayboyPlaymate)

def playboyplaymates_id_get(id):  # noqa: E501
    """Get a single PlayboyPlaymate by its id

    Gets the details of a given PlayboyPlaymate (more information in http://dbpedia.org/ontology/PlayboyPlaymate) # noqa: E501

    :param id: The ID of the PlayboyPlaymate to be retrieved
    :type id: str

    :rtype: PlayboyPlaymate
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PLAYBOYPLAYMATE_TYPE_URI,
        rdf_type_name=PLAYBOYPLAYMATE_TYPE_NAME, 
        kls=PlayboyPlaymate)
