import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CLERICALORDER_TYPE_NAME, CLERICALORDER_TYPE_URI

from openapi_server.models.clerical_order import ClericalOrder  # noqa: E501
from openapi_server import util

def clericalorders_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ClericalOrder

    Gets a list of all instances of ClericalOrder (more information in http://dbpedia.org/ontology/ClericalOrder) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ClericalOrder]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CLERICALORDER_TYPE_URI,
        rdf_type_name=CLERICALORDER_TYPE_NAME, 
        kls=ClericalOrder)

def clericalorders_id_get(id):  # noqa: E501
    """Get a single ClericalOrder by its id

    Gets the details of a given ClericalOrder (more information in http://dbpedia.org/ontology/ClericalOrder) # noqa: E501

    :param id: The ID of the ClericalOrder to be retrieved
    :type id: str

    :rtype: ClericalOrder
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CLERICALORDER_TYPE_URI,
        rdf_type_name=CLERICALORDER_TYPE_NAME, 
        kls=ClericalOrder)
