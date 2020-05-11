import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HISTORICALPROVINCE_TYPE_NAME, HISTORICALPROVINCE_TYPE_URI

from openapi_server.models.historical_province import HistoricalProvince  # noqa: E501
from openapi_server import util

def historicalprovinces_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HistoricalProvince

    Gets a list of all instances of HistoricalProvince (more information in http://dbpedia.org/ontology/HistoricalProvince) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HistoricalProvince]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HISTORICALPROVINCE_TYPE_URI,
        rdf_type_name=HISTORICALPROVINCE_TYPE_NAME, 
        kls=HistoricalProvince)

def historicalprovinces_id_get(id):  # noqa: E501
    """Get a single HistoricalProvince by its id

    Gets the details of a given HistoricalProvince (more information in http://dbpedia.org/ontology/HistoricalProvince) # noqa: E501

    :param id: The ID of the HistoricalProvince to be retrieved
    :type id: str

    :rtype: HistoricalProvince
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HISTORICALPROVINCE_TYPE_URI,
        rdf_type_name=HISTORICALPROVINCE_TYPE_NAME, 
        kls=HistoricalProvince)
