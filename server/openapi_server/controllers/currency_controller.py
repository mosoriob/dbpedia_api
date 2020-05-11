import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CURRENCY_TYPE_NAME, CURRENCY_TYPE_URI

from openapi_server.models.currency import Currency  # noqa: E501
from openapi_server import util

def currencys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Currency

    Gets a list of all instances of Currency (more information in http://dbpedia.org/ontology/Currency) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Currency]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CURRENCY_TYPE_URI,
        rdf_type_name=CURRENCY_TYPE_NAME, 
        kls=Currency)

def currencys_id_get(id):  # noqa: E501
    """Get a single Currency by its id

    Gets the details of a given Currency (more information in http://dbpedia.org/ontology/Currency) # noqa: E501

    :param id: The ID of the Currency to be retrieved
    :type id: str

    :rtype: Currency
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CURRENCY_TYPE_URI,
        rdf_type_name=CURRENCY_TYPE_NAME, 
        kls=Currency)
