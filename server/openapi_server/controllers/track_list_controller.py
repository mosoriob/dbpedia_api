import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TRACKLIST_TYPE_NAME, TRACKLIST_TYPE_URI

from openapi_server.models.track_list import TrackList  # noqa: E501
from openapi_server import util

def tracklists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TrackList

    Gets a list of all instances of TrackList (more information in http://dbpedia.org/ontology/TrackList) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TrackList]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TRACKLIST_TYPE_URI,
        rdf_type_name=TRACKLIST_TYPE_NAME, 
        kls=TrackList)

def tracklists_id_get(id):  # noqa: E501
    """Get a single TrackList by its id

    Gets the details of a given TrackList (more information in http://dbpedia.org/ontology/TrackList) # noqa: E501

    :param id: The ID of the TrackList to be retrieved
    :type id: str

    :rtype: TrackList
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TRACKLIST_TYPE_URI,
        rdf_type_name=TRACKLIST_TYPE_NAME, 
        kls=TrackList)
