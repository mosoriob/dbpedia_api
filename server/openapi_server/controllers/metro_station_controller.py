import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import METROSTATION_TYPE_NAME, METROSTATION_TYPE_URI

from openapi_server.models.metro_station import MetroStation  # noqa: E501
from openapi_server import util

def metrostations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MetroStation

    Gets a list of all instances of MetroStation (more information in http://dbpedia.org/ontology/MetroStation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MetroStation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=METROSTATION_TYPE_URI,
        rdf_type_name=METROSTATION_TYPE_NAME, 
        kls=MetroStation)

def metrostations_id_get(id):  # noqa: E501
    """Get a single MetroStation by its id

    Gets the details of a given MetroStation (more information in http://dbpedia.org/ontology/MetroStation) # noqa: E501

    :param id: The ID of the MetroStation to be retrieved
    :type id: str

    :rtype: MetroStation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=METROSTATION_TYPE_URI,
        rdf_type_name=METROSTATION_TYPE_NAME, 
        kls=MetroStation)
