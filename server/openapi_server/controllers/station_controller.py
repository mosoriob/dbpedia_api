import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import STATION_TYPE_NAME, STATION_TYPE_URI

from openapi_server.models.station import Station  # noqa: E501
from openapi_server import util

def stations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Station

    Gets a list of all instances of Station (more information in http://dbpedia.org/ontology/Station) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Station]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=STATION_TYPE_URI,
        rdf_type_name=STATION_TYPE_NAME, 
        kls=Station)

def stations_id_get(id):  # noqa: E501
    """Get a single Station by its id

    Gets the details of a given Station (more information in http://dbpedia.org/ontology/Station) # noqa: E501

    :param id: The ID of the Station to be retrieved
    :type id: str

    :rtype: Station
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=STATION_TYPE_URI,
        rdf_type_name=STATION_TYPE_NAME, 
        kls=Station)
