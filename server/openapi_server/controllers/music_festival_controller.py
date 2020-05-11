import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MUSICFESTIVAL_TYPE_NAME, MUSICFESTIVAL_TYPE_URI

from openapi_server.models.music_festival import MusicFestival  # noqa: E501
from openapi_server import util

def musicfestivals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MusicFestival

    Gets a list of all instances of MusicFestival (more information in http://dbpedia.org/ontology/MusicFestival) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MusicFestival]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MUSICFESTIVAL_TYPE_URI,
        rdf_type_name=MUSICFESTIVAL_TYPE_NAME, 
        kls=MusicFestival)

def musicfestivals_id_get(id):  # noqa: E501
    """Get a single MusicFestival by its id

    Gets the details of a given MusicFestival (more information in http://dbpedia.org/ontology/MusicFestival) # noqa: E501

    :param id: The ID of the MusicFestival to be retrieved
    :type id: str

    :rtype: MusicFestival
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MUSICFESTIVAL_TYPE_URI,
        rdf_type_name=MUSICFESTIVAL_TYPE_NAME, 
        kls=MusicFestival)
