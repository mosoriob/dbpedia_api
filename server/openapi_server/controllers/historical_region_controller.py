import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HISTORICALREGION_TYPE_NAME, HISTORICALREGION_TYPE_URI

from openapi_server.models.historical_region import HistoricalRegion  # noqa: E501
from openapi_server import util

def historicalregions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HistoricalRegion

    Gets a list of all instances of HistoricalRegion (more information in http://dbpedia.org/ontology/HistoricalRegion) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HistoricalRegion]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HISTORICALREGION_TYPE_URI,
        rdf_type_name=HISTORICALREGION_TYPE_NAME, 
        kls=HistoricalRegion)

def historicalregions_id_get(id):  # noqa: E501
    """Get a single HistoricalRegion by its id

    Gets the details of a given HistoricalRegion (more information in http://dbpedia.org/ontology/HistoricalRegion) # noqa: E501

    :param id: The ID of the HistoricalRegion to be retrieved
    :type id: str

    :rtype: HistoricalRegion
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HISTORICALREGION_TYPE_URI,
        rdf_type_name=HISTORICALREGION_TYPE_NAME, 
        kls=HistoricalRegion)
