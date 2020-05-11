import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ROMANIASETTLEMENT_TYPE_NAME, ROMANIASETTLEMENT_TYPE_URI

from openapi_server.models.romania_settlement import RomaniaSettlement  # noqa: E501
from openapi_server import util

def romaniasettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RomaniaSettlement

    Gets a list of all instances of RomaniaSettlement (more information in http://dbpedia.org/ontology/RomaniaSettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RomaniaSettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ROMANIASETTLEMENT_TYPE_URI,
        rdf_type_name=ROMANIASETTLEMENT_TYPE_NAME, 
        kls=RomaniaSettlement)

def romaniasettlements_id_get(id):  # noqa: E501
    """Get a single RomaniaSettlement by its id

    Gets the details of a given RomaniaSettlement (more information in http://dbpedia.org/ontology/RomaniaSettlement) # noqa: E501

    :param id: The ID of the RomaniaSettlement to be retrieved
    :type id: str

    :rtype: RomaniaSettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ROMANIASETTLEMENT_TYPE_URI,
        rdf_type_name=ROMANIASETTLEMENT_TYPE_NAME, 
        kls=RomaniaSettlement)
