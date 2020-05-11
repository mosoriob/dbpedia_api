import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HISTORICALSETTLEMENT_TYPE_NAME, HISTORICALSETTLEMENT_TYPE_URI

from openapi_server.models.historical_settlement import HistoricalSettlement  # noqa: E501
from openapi_server import util

def historicalsettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HistoricalSettlement

    Gets a list of all instances of HistoricalSettlement (more information in http://dbpedia.org/ontology/HistoricalSettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HistoricalSettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HISTORICALSETTLEMENT_TYPE_URI,
        rdf_type_name=HISTORICALSETTLEMENT_TYPE_NAME, 
        kls=HistoricalSettlement)

def historicalsettlements_id_get(id):  # noqa: E501
    """Get a single HistoricalSettlement by its id

    Gets the details of a given HistoricalSettlement (more information in http://dbpedia.org/ontology/HistoricalSettlement) # noqa: E501

    :param id: The ID of the HistoricalSettlement to be retrieved
    :type id: str

    :rtype: HistoricalSettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HISTORICALSETTLEMENT_TYPE_URI,
        rdf_type_name=HISTORICALSETTLEMENT_TYPE_NAME, 
        kls=HistoricalSettlement)
