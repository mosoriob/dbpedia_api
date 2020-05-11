import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BOWLINGLEAGUE_TYPE_NAME, BOWLINGLEAGUE_TYPE_URI

from openapi_server.models.bowling_league import BowlingLeague  # noqa: E501
from openapi_server import util

def bowlingleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BowlingLeague

    Gets a list of all instances of BowlingLeague (more information in http://dbpedia.org/ontology/BowlingLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BowlingLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BOWLINGLEAGUE_TYPE_URI,
        rdf_type_name=BOWLINGLEAGUE_TYPE_NAME, 
        kls=BowlingLeague)

def bowlingleagues_id_get(id):  # noqa: E501
    """Get a single BowlingLeague by its id

    Gets the details of a given BowlingLeague (more information in http://dbpedia.org/ontology/BowlingLeague) # noqa: E501

    :param id: The ID of the BowlingLeague to be retrieved
    :type id: str

    :rtype: BowlingLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BOWLINGLEAGUE_TYPE_URI,
        rdf_type_name=BOWLINGLEAGUE_TYPE_NAME, 
        kls=BowlingLeague)
