import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VOICEACTOR_TYPE_NAME, VOICEACTOR_TYPE_URI

from openapi_server.models.voice_actor import VoiceActor  # noqa: E501
from openapi_server import util

def voiceactors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of VoiceActor

    Gets a list of all instances of VoiceActor (more information in http://dbpedia.org/ontology/VoiceActor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[VoiceActor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VOICEACTOR_TYPE_URI,
        rdf_type_name=VOICEACTOR_TYPE_NAME, 
        kls=VoiceActor)

def voiceactors_id_get(id):  # noqa: E501
    """Get a single VoiceActor by its id

    Gets the details of a given VoiceActor (more information in http://dbpedia.org/ontology/VoiceActor) # noqa: E501

    :param id: The ID of the VoiceActor to be retrieved
    :type id: str

    :rtype: VoiceActor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VOICEACTOR_TYPE_URI,
        rdf_type_name=VOICEACTOR_TYPE_NAME, 
        kls=VoiceActor)
