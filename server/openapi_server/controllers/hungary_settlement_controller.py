import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HUNGARYSETTLEMENT_TYPE_NAME, HUNGARYSETTLEMENT_TYPE_URI

from openapi_server.models.hungary_settlement import HungarySettlement  # noqa: E501
from openapi_server import util

def hungarysettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HungarySettlement

    Gets a list of all instances of HungarySettlement (more information in http://dbpedia.org/ontology/HungarySettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HungarySettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HUNGARYSETTLEMENT_TYPE_URI,
        rdf_type_name=HUNGARYSETTLEMENT_TYPE_NAME, 
        kls=HungarySettlement)

def hungarysettlements_id_get(id):  # noqa: E501
    """Get a single HungarySettlement by its id

    Gets the details of a given HungarySettlement (more information in http://dbpedia.org/ontology/HungarySettlement) # noqa: E501

    :param id: The ID of the HungarySettlement to be retrieved
    :type id: str

    :rtype: HungarySettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HUNGARYSETTLEMENT_TYPE_URI,
        rdf_type_name=HUNGARYSETTLEMENT_TYPE_NAME, 
        kls=HungarySettlement)
