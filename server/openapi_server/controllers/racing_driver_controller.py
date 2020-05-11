import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RACINGDRIVER_TYPE_NAME, RACINGDRIVER_TYPE_URI

from openapi_server.models.racing_driver import RacingDriver  # noqa: E501
from openapi_server import util

def racingdrivers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RacingDriver

    Gets a list of all instances of RacingDriver (more information in http://dbpedia.org/ontology/RacingDriver) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RacingDriver]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RACINGDRIVER_TYPE_URI,
        rdf_type_name=RACINGDRIVER_TYPE_NAME, 
        kls=RacingDriver)

def racingdrivers_id_get(id):  # noqa: E501
    """Get a single RacingDriver by its id

    Gets the details of a given RacingDriver (more information in http://dbpedia.org/ontology/RacingDriver) # noqa: E501

    :param id: The ID of the RacingDriver to be retrieved
    :type id: str

    :rtype: RacingDriver
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RACINGDRIVER_TYPE_URI,
        rdf_type_name=RACINGDRIVER_TYPE_NAME, 
        kls=RacingDriver)
