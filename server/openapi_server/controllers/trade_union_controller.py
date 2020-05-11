import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TRADEUNION_TYPE_NAME, TRADEUNION_TYPE_URI

from openapi_server.models.trade_union import TradeUnion  # noqa: E501
from openapi_server import util

def tradeunions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TradeUnion

    Gets a list of all instances of TradeUnion (more information in http://dbpedia.org/ontology/TradeUnion) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TradeUnion]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TRADEUNION_TYPE_URI,
        rdf_type_name=TRADEUNION_TYPE_NAME, 
        kls=TradeUnion)

def tradeunions_id_get(id):  # noqa: E501
    """Get a single TradeUnion by its id

    Gets the details of a given TradeUnion (more information in http://dbpedia.org/ontology/TradeUnion) # noqa: E501

    :param id: The ID of the TradeUnion to be retrieved
    :type id: str

    :rtype: TradeUnion
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TRADEUNION_TYPE_URI,
        rdf_type_name=TRADEUNION_TYPE_NAME, 
        kls=TradeUnion)
