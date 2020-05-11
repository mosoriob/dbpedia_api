import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOTORCYCLERIDER_TYPE_NAME, MOTORCYCLERIDER_TYPE_URI

from openapi_server.models.motorcycle_rider import MotorcycleRider  # noqa: E501
from openapi_server import util

def motorcycleriders_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MotorcycleRider

    Gets a list of all instances of MotorcycleRider (more information in http://dbpedia.org/ontology/MotorcycleRider) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MotorcycleRider]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOTORCYCLERIDER_TYPE_URI,
        rdf_type_name=MOTORCYCLERIDER_TYPE_NAME, 
        kls=MotorcycleRider)

def motorcycleriders_id_get(id):  # noqa: E501
    """Get a single MotorcycleRider by its id

    Gets the details of a given MotorcycleRider (more information in http://dbpedia.org/ontology/MotorcycleRider) # noqa: E501

    :param id: The ID of the MotorcycleRider to be retrieved
    :type id: str

    :rtype: MotorcycleRider
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOTORCYCLERIDER_TYPE_URI,
        rdf_type_name=MOTORCYCLERIDER_TYPE_NAME, 
        kls=MotorcycleRider)
