import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOUND_TYPE_NAME, SOUND_TYPE_URI

from openapi_server.models.sound import Sound  # noqa: E501
from openapi_server import util

def sounds_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Sound

    Gets a list of all instances of Sound (more information in http://dbpedia.org/ontology/Sound) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Sound]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOUND_TYPE_URI,
        rdf_type_name=SOUND_TYPE_NAME, 
        kls=Sound)

def sounds_id_get(id):  # noqa: E501
    """Get a single Sound by its id

    Gets the details of a given Sound (more information in http://dbpedia.org/ontology/Sound) # noqa: E501

    :param id: The ID of the Sound to be retrieved
    :type id: str

    :rtype: Sound
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOUND_TYPE_URI,
        rdf_type_name=SOUND_TYPE_NAME, 
        kls=Sound)
