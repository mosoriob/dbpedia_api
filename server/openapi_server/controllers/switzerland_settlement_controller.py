import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SWITZERLANDSETTLEMENT_TYPE_NAME, SWITZERLANDSETTLEMENT_TYPE_URI

from openapi_server.models.switzerland_settlement import SwitzerlandSettlement  # noqa: E501
from openapi_server import util

def switzerlandsettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SwitzerlandSettlement

    Gets a list of all instances of SwitzerlandSettlement (more information in http://dbpedia.org/ontology/SwitzerlandSettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SwitzerlandSettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SWITZERLANDSETTLEMENT_TYPE_URI,
        rdf_type_name=SWITZERLANDSETTLEMENT_TYPE_NAME, 
        kls=SwitzerlandSettlement)

def switzerlandsettlements_id_get(id):  # noqa: E501
    """Get a single SwitzerlandSettlement by its id

    Gets the details of a given SwitzerlandSettlement (more information in http://dbpedia.org/ontology/SwitzerlandSettlement) # noqa: E501

    :param id: The ID of the SwitzerlandSettlement to be retrieved
    :type id: str

    :rtype: SwitzerlandSettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SWITZERLANDSETTLEMENT_TYPE_URI,
        rdf_type_name=SWITZERLANDSETTLEMENT_TYPE_NAME, 
        kls=SwitzerlandSettlement)
