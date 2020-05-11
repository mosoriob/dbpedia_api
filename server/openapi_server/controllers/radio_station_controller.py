import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RADIOSTATION_TYPE_NAME, RADIOSTATION_TYPE_URI

from openapi_server.models.radio_station import RadioStation  # noqa: E501
from openapi_server import util

def radiostations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RadioStation

    Gets a list of all instances of RadioStation (more information in http://dbpedia.org/ontology/RadioStation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RadioStation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RADIOSTATION_TYPE_URI,
        rdf_type_name=RADIOSTATION_TYPE_NAME, 
        kls=RadioStation)

def radiostations_id_get(id):  # noqa: E501
    """Get a single RadioStation by its id

    Gets the details of a given RadioStation (more information in http://dbpedia.org/ontology/RadioStation) # noqa: E501

    :param id: The ID of the RadioStation to be retrieved
    :type id: str

    :rtype: RadioStation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RADIOSTATION_TYPE_URI,
        rdf_type_name=RADIOSTATION_TYPE_NAME, 
        kls=RadioStation)
