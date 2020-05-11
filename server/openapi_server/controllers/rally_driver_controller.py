import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RALLYDRIVER_TYPE_NAME, RALLYDRIVER_TYPE_URI

from openapi_server.models.rally_driver import RallyDriver  # noqa: E501
from openapi_server import util

def rallydrivers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RallyDriver

    Gets a list of all instances of RallyDriver (more information in http://dbpedia.org/ontology/RallyDriver) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RallyDriver]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RALLYDRIVER_TYPE_URI,
        rdf_type_name=RALLYDRIVER_TYPE_NAME, 
        kls=RallyDriver)

def rallydrivers_id_get(id):  # noqa: E501
    """Get a single RallyDriver by its id

    Gets the details of a given RallyDriver (more information in http://dbpedia.org/ontology/RallyDriver) # noqa: E501

    :param id: The ID of the RallyDriver to be retrieved
    :type id: str

    :rtype: RallyDriver
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RALLYDRIVER_TYPE_URI,
        rdf_type_name=RALLYDRIVER_TYPE_NAME, 
        kls=RallyDriver)
