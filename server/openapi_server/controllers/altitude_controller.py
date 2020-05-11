import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ALTITUDE_TYPE_NAME, ALTITUDE_TYPE_URI

from openapi_server.models.altitude import Altitude  # noqa: E501
from openapi_server import util

def altitudes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Altitude

    Gets a list of all instances of Altitude (more information in http://dbpedia.org/ontology/Altitude) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Altitude]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ALTITUDE_TYPE_URI,
        rdf_type_name=ALTITUDE_TYPE_NAME, 
        kls=Altitude)

def altitudes_id_get(id):  # noqa: E501
    """Get a single Altitude by its id

    Gets the details of a given Altitude (more information in http://dbpedia.org/ontology/Altitude) # noqa: E501

    :param id: The ID of the Altitude to be retrieved
    :type id: str

    :rtype: Altitude
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ALTITUDE_TYPE_URI,
        rdf_type_name=ALTITUDE_TYPE_NAME, 
        kls=Altitude)
