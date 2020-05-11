import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ROLLERCOASTER_TYPE_NAME, ROLLERCOASTER_TYPE_URI

from openapi_server.models.roller_coaster import RollerCoaster  # noqa: E501
from openapi_server import util

def rollercoasters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RollerCoaster

    Gets a list of all instances of RollerCoaster (more information in http://dbpedia.org/ontology/RollerCoaster) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RollerCoaster]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ROLLERCOASTER_TYPE_URI,
        rdf_type_name=ROLLERCOASTER_TYPE_NAME, 
        kls=RollerCoaster)

def rollercoasters_id_get(id):  # noqa: E501
    """Get a single RollerCoaster by its id

    Gets the details of a given RollerCoaster (more information in http://dbpedia.org/ontology/RollerCoaster) # noqa: E501

    :param id: The ID of the RollerCoaster to be retrieved
    :type id: str

    :rtype: RollerCoaster
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ROLLERCOASTER_TYPE_URI,
        rdf_type_name=ROLLERCOASTER_TYPE_NAME, 
        kls=RollerCoaster)
