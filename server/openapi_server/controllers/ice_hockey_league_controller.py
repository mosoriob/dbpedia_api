import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ICEHOCKEYLEAGUE_TYPE_NAME, ICEHOCKEYLEAGUE_TYPE_URI

from openapi_server.models.ice_hockey_league import IceHockeyLeague  # noqa: E501
from openapi_server import util

def icehockeyleagues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of IceHockeyLeague

    Gets a list of all instances of IceHockeyLeague (more information in http://dbpedia.org/ontology/IceHockeyLeague) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[IceHockeyLeague]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ICEHOCKEYLEAGUE_TYPE_URI,
        rdf_type_name=ICEHOCKEYLEAGUE_TYPE_NAME, 
        kls=IceHockeyLeague)

def icehockeyleagues_id_get(id):  # noqa: E501
    """Get a single IceHockeyLeague by its id

    Gets the details of a given IceHockeyLeague (more information in http://dbpedia.org/ontology/IceHockeyLeague) # noqa: E501

    :param id: The ID of the IceHockeyLeague to be retrieved
    :type id: str

    :rtype: IceHockeyLeague
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ICEHOCKEYLEAGUE_TYPE_URI,
        rdf_type_name=ICEHOCKEYLEAGUE_TYPE_NAME, 
        kls=IceHockeyLeague)
