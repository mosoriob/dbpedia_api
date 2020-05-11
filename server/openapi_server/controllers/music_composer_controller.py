import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MUSICCOMPOSER_TYPE_NAME, MUSICCOMPOSER_TYPE_URI

from openapi_server.models.music_composer import MusicComposer  # noqa: E501
from openapi_server import util

def musiccomposers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MusicComposer

    Gets a list of all instances of MusicComposer (more information in http://dbpedia.org/ontology/MusicComposer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MusicComposer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MUSICCOMPOSER_TYPE_URI,
        rdf_type_name=MUSICCOMPOSER_TYPE_NAME, 
        kls=MusicComposer)

def musiccomposers_id_get(id):  # noqa: E501
    """Get a single MusicComposer by its id

    Gets the details of a given MusicComposer (more information in http://dbpedia.org/ontology/MusicComposer) # noqa: E501

    :param id: The ID of the MusicComposer to be retrieved
    :type id: str

    :rtype: MusicComposer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MUSICCOMPOSER_TYPE_URI,
        rdf_type_name=MUSICCOMPOSER_TYPE_NAME, 
        kls=MusicComposer)
