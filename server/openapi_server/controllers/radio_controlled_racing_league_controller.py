import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RADIOCONTROLLEDRACINGLEAGUE_TYPE_NAME, RADIOCONTROLLEDRACINGLEAGUE_TYPE_URI

from openapi_server.models.radio_controlled_racing_league import RadioControlledRacingLeague  # noqa: E501
from openapi_server import util

def radiocontrolledracingleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RadioControlledRacingLeague

    Gets a list of all instances of RadioControlledRacingLeague (more information in http://dbpedia.org/ontology/RadioControlledRacingLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RadioControlledRacingLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RADIOCONTROLLEDRACINGLEAGUE_TYPE_URI,
        rdf_type_name=RADIOCONTROLLEDRACINGLEAGUE_TYPE_NAME, 
        kls=RadioControlledRacingLeague)

def radiocontrolledracingleagues_id_get(id):  # noqa: E501
    """Get a single RadioControlledRacingLeague by its id

    Gets the details of a given RadioControlledRacingLeague (more information in http://dbpedia.org/ontology/RadioControlledRacingLeague) # noqa: E501

    :param id: The ID of the RadioControlledRacingLeague to be retrieved
    :type id: str

    :rtype: RadioControlledRacingLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RADIOCONTROLLEDRACINGLEAGUE_TYPE_URI,
        rdf_type_name=RADIOCONTROLLEDRACINGLEAGUE_TYPE_NAME, 
        kls=RadioControlledRacingLeague)
