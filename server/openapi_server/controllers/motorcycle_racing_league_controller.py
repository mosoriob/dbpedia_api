import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOTORCYCLERACINGLEAGUE_TYPE_NAME, MOTORCYCLERACINGLEAGUE_TYPE_URI

from openapi_server.models.motorcycle_racing_league import MotorcycleRacingLeague  # noqa: E501
from openapi_server import util

def motorcycleracingleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MotorcycleRacingLeague

    Gets a list of all instances of MotorcycleRacingLeague (more information in http://dbpedia.org/ontology/MotorcycleRacingLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MotorcycleRacingLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOTORCYCLERACINGLEAGUE_TYPE_URI,
        rdf_type_name=MOTORCYCLERACINGLEAGUE_TYPE_NAME, 
        kls=MotorcycleRacingLeague)

def motorcycleracingleagues_id_get(id):  # noqa: E501
    """Get a single MotorcycleRacingLeague by its id

    Gets the details of a given MotorcycleRacingLeague (more information in http://dbpedia.org/ontology/MotorcycleRacingLeague) # noqa: E501

    :param id: The ID of the MotorcycleRacingLeague to be retrieved
    :type id: str

    :rtype: MotorcycleRacingLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOTORCYCLERACINGLEAGUE_TYPE_URI,
        rdf_type_name=MOTORCYCLERACINGLEAGUE_TYPE_NAME, 
        kls=MotorcycleRacingLeague)
