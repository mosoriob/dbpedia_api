import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HISTORICALPERIOD_TYPE_NAME, HISTORICALPERIOD_TYPE_URI

from openapi_server.models.historical_period import HistoricalPeriod  # noqa: E501
from openapi_server import util

def historicalperiods_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HistoricalPeriod

    Gets a list of all instances of HistoricalPeriod (more information in http://dbpedia.org/ontology/HistoricalPeriod) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HistoricalPeriod]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HISTORICALPERIOD_TYPE_URI,
        rdf_type_name=HISTORICALPERIOD_TYPE_NAME, 
        kls=HistoricalPeriod)

def historicalperiods_id_get(id):  # noqa: E501
    """Get a single HistoricalPeriod by its id

    Gets the details of a given HistoricalPeriod (more information in http://dbpedia.org/ontology/HistoricalPeriod) # noqa: E501

    :param id: The ID of the HistoricalPeriod to be retrieved
    :type id: str

    :rtype: HistoricalPeriod
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HISTORICALPERIOD_TYPE_URI,
        rdf_type_name=HISTORICALPERIOD_TYPE_NAME, 
        kls=HistoricalPeriod)
