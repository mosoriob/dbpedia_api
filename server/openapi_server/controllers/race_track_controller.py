import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RACETRACK_TYPE_NAME, RACETRACK_TYPE_URI

from openapi_server.models.race_track import RaceTrack  # noqa: E501
from openapi_server import util

def racetracks_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RaceTrack

    Gets a list of all instances of RaceTrack (more information in http://dbpedia.org/ontology/RaceTrack) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RaceTrack]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RACETRACK_TYPE_URI,
        rdf_type_name=RACETRACK_TYPE_NAME, 
        kls=RaceTrack)

def racetracks_id_get(id):  # noqa: E501
    """Get a single RaceTrack by its id

    Gets the details of a given RaceTrack (more information in http://dbpedia.org/ontology/RaceTrack) # noqa: E501

    :param id: The ID of the RaceTrack to be retrieved
    :type id: str

    :rtype: RaceTrack
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RACETRACK_TYPE_URI,
        rdf_type_name=RACETRACK_TYPE_NAME, 
        kls=RaceTrack)
