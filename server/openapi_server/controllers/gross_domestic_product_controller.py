import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GROSSDOMESTICPRODUCT_TYPE_NAME, GROSSDOMESTICPRODUCT_TYPE_URI

from openapi_server.models.gross_domestic_product import GrossDomesticProduct  # noqa: E501
from openapi_server import util

def grossdomesticproducts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GrossDomesticProduct

    Gets a list of all instances of GrossDomesticProduct (more information in http://dbpedia.org/ontology/GrossDomesticProduct) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GrossDomesticProduct]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GROSSDOMESTICPRODUCT_TYPE_URI,
        rdf_type_name=GROSSDOMESTICPRODUCT_TYPE_NAME, 
        kls=GrossDomesticProduct)

def grossdomesticproducts_id_get(id):  # noqa: E501
    """Get a single GrossDomesticProduct by its id

    Gets the details of a given GrossDomesticProduct (more information in http://dbpedia.org/ontology/GrossDomesticProduct) # noqa: E501

    :param id: The ID of the GrossDomesticProduct to be retrieved
    :type id: str

    :rtype: GrossDomesticProduct
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GROSSDOMESTICPRODUCT_TYPE_URI,
        rdf_type_name=GROSSDOMESTICPRODUCT_TYPE_NAME, 
        kls=GrossDomesticProduct)
