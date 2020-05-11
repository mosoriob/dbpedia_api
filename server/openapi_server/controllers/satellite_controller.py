import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SATELLITE_TYPE_NAME, SATELLITE_TYPE_URI

from openapi_server.models.satellite import Satellite  # noqa: E501
from openapi_server import util

def satellites_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Satellite

    Gets a list of all instances of Satellite (more information in http://dbpedia.org/ontology/Satellite) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Satellite]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SATELLITE_TYPE_URI,
        rdf_type_name=SATELLITE_TYPE_NAME, 
        kls=Satellite)

def satellites_id_get(id):  # noqa: E501
    """Get a single Satellite by its id

    Gets the details of a given Satellite (more information in http://dbpedia.org/ontology/Satellite) # noqa: E501

    :param id: The ID of the Satellite to be retrieved
    :type id: str

    :rtype: Satellite
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SATELLITE_TYPE_URI,
        rdf_type_name=SATELLITE_TYPE_NAME, 
        kls=Satellite)
