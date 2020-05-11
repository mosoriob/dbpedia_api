import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPACESTATION_TYPE_NAME, SPACESTATION_TYPE_URI

from openapi_server.models.space_station import SpaceStation  # noqa: E501
from openapi_server import util

def spacestations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SpaceStation

    Gets a list of all instances of SpaceStation (more information in http://dbpedia.org/ontology/SpaceStation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SpaceStation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPACESTATION_TYPE_URI,
        rdf_type_name=SPACESTATION_TYPE_NAME, 
        kls=SpaceStation)

def spacestations_id_get(id):  # noqa: E501
    """Get a single SpaceStation by its id

    Gets the details of a given SpaceStation (more information in http://dbpedia.org/ontology/SpaceStation) # noqa: E501

    :param id: The ID of the SpaceStation to be retrieved
    :type id: str

    :rtype: SpaceStation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPACESTATION_TYPE_URI,
        rdf_type_name=SPACESTATION_TYPE_NAME, 
        kls=SpaceStation)
