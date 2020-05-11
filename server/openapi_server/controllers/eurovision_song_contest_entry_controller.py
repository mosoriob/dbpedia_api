import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import EUROVISIONSONGCONTESTENTRY_TYPE_NAME, EUROVISIONSONGCONTESTENTRY_TYPE_URI

from openapi_server.models.eurovision_song_contest_entry import EurovisionSongContestEntry  # noqa: E501
from openapi_server import util

def eurovisionsongcontestentrys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of EurovisionSongContestEntry

    Gets a list of all instances of EurovisionSongContestEntry (more information in http://dbpedia.org/ontology/EurovisionSongContestEntry) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[EurovisionSongContestEntry]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=EUROVISIONSONGCONTESTENTRY_TYPE_URI,
        rdf_type_name=EUROVISIONSONGCONTESTENTRY_TYPE_NAME, 
        kls=EurovisionSongContestEntry)

def eurovisionsongcontestentrys_id_get(id):  # noqa: E501
    """Get a single EurovisionSongContestEntry by its id

    Gets the details of a given EurovisionSongContestEntry (more information in http://dbpedia.org/ontology/EurovisionSongContestEntry) # noqa: E501

    :param id: The ID of the EurovisionSongContestEntry to be retrieved
    :type id: str

    :rtype: EurovisionSongContestEntry
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=EUROVISIONSONGCONTESTENTRY_TYPE_URI,
        rdf_type_name=EUROVISIONSONGCONTESTENTRY_TYPE_NAME, 
        kls=EurovisionSongContestEntry)
