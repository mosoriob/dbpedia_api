import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TIMEPERIOD_TYPE_NAME, TIMEPERIOD_TYPE_URI

from openapi_server.models.time_period import TimePeriod  # noqa: E501
from openapi_server import util

def timeperiods_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TimePeriod

    Gets a list of all instances of TimePeriod (more information in http://dbpedia.org/ontology/TimePeriod) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TimePeriod]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TIMEPERIOD_TYPE_URI,
        rdf_type_name=TIMEPERIOD_TYPE_NAME, 
        kls=TimePeriod)

def timeperiods_id_get(id):  # noqa: E501
    """Get a single TimePeriod by its id

    Gets the details of a given TimePeriod (more information in http://dbpedia.org/ontology/TimePeriod) # noqa: E501

    :param id: The ID of the TimePeriod to be retrieved
    :type id: str

    :rtype: TimePeriod
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TIMEPERIOD_TYPE_URI,
        rdf_type_name=TIMEPERIOD_TYPE_NAME, 
        kls=TimePeriod)
