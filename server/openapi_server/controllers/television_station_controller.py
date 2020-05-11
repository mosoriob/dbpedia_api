import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TELEVISIONSTATION_TYPE_NAME, TELEVISIONSTATION_TYPE_URI

from openapi_server.models.television_station import TelevisionStation  # noqa: E501
from openapi_server import util

def televisionstations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TelevisionStation

    Gets a list of all instances of TelevisionStation (more information in http://dbpedia.org/ontology/TelevisionStation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TelevisionStation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TELEVISIONSTATION_TYPE_URI,
        rdf_type_name=TELEVISIONSTATION_TYPE_NAME, 
        kls=TelevisionStation)

def televisionstations_id_get(id):  # noqa: E501
    """Get a single TelevisionStation by its id

    Gets the details of a given TelevisionStation (more information in http://dbpedia.org/ontology/TelevisionStation) # noqa: E501

    :param id: The ID of the TelevisionStation to be retrieved
    :type id: str

    :rtype: TelevisionStation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TELEVISIONSTATION_TYPE_URI,
        rdf_type_name=TELEVISIONSTATION_TYPE_NAME, 
        kls=TelevisionStation)
