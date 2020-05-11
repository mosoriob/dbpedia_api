import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GROSSDOMESTICPRODUCTPERCAPITA_TYPE_NAME, GROSSDOMESTICPRODUCTPERCAPITA_TYPE_URI

from openapi_server.models.gross_domestic_product_per_capita import GrossDomesticProductPerCapita  # noqa: E501
from openapi_server import util

def grossdomesticproductpercapitas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GrossDomesticProductPerCapita

    Gets a list of all instances of GrossDomesticProductPerCapita (more information in http://dbpedia.org/ontology/GrossDomesticProductPerCapita) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GrossDomesticProductPerCapita]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GROSSDOMESTICPRODUCTPERCAPITA_TYPE_URI,
        rdf_type_name=GROSSDOMESTICPRODUCTPERCAPITA_TYPE_NAME, 
        kls=GrossDomesticProductPerCapita)

def grossdomesticproductpercapitas_id_get(id):  # noqa: E501
    """Get a single GrossDomesticProductPerCapita by its id

    Gets the details of a given GrossDomesticProductPerCapita (more information in http://dbpedia.org/ontology/GrossDomesticProductPerCapita) # noqa: E501

    :param id: The ID of the GrossDomesticProductPerCapita to be retrieved
    :type id: str

    :rtype: GrossDomesticProductPerCapita
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GROSSDOMESTICPRODUCTPERCAPITA_TYPE_URI,
        rdf_type_name=GROSSDOMESTICPRODUCTPERCAPITA_TYPE_NAME, 
        kls=GrossDomesticProductPerCapita)
