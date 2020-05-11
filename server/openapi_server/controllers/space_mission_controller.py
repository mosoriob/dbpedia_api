import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPACEMISSION_TYPE_NAME, SPACEMISSION_TYPE_URI

from openapi_server.models.space_mission import SpaceMission  # noqa: E501
from openapi_server import util

def spacemissions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SpaceMission

    Gets a list of all instances of SpaceMission (more information in http://dbpedia.org/ontology/SpaceMission) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SpaceMission]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPACEMISSION_TYPE_URI,
        rdf_type_name=SPACEMISSION_TYPE_NAME, 
        kls=SpaceMission)

def spacemissions_id_get(id):  # noqa: E501
    """Get a single SpaceMission by its id

    Gets the details of a given SpaceMission (more information in http://dbpedia.org/ontology/SpaceMission) # noqa: E501

    :param id: The ID of the SpaceMission to be retrieved
    :type id: str

    :rtype: SpaceMission
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPACEMISSION_TYPE_URI,
        rdf_type_name=SPACEMISSION_TYPE_NAME, 
        kls=SpaceMission)
