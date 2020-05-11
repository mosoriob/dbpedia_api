import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HISTORICALDISTRICT_TYPE_NAME, HISTORICALDISTRICT_TYPE_URI

from openapi_server.models.historical_district import HistoricalDistrict  # noqa: E501
from openapi_server import util

def historicaldistricts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HistoricalDistrict

    Gets a list of all instances of HistoricalDistrict (more information in http://dbpedia.org/ontology/HistoricalDistrict) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HistoricalDistrict]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HISTORICALDISTRICT_TYPE_URI,
        rdf_type_name=HISTORICALDISTRICT_TYPE_NAME, 
        kls=HistoricalDistrict)

def historicaldistricts_id_get(id):  # noqa: E501
    """Get a single HistoricalDistrict by its id

    Gets the details of a given HistoricalDistrict (more information in http://dbpedia.org/ontology/HistoricalDistrict) # noqa: E501

    :param id: The ID of the HistoricalDistrict to be retrieved
    :type id: str

    :rtype: HistoricalDistrict
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HISTORICALDISTRICT_TYPE_URI,
        rdf_type_name=HISTORICALDISTRICT_TYPE_NAME, 
        kls=HistoricalDistrict)
