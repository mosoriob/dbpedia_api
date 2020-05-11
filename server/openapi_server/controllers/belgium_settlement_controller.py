import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BELGIUMSETTLEMENT_TYPE_NAME, BELGIUMSETTLEMENT_TYPE_URI

from openapi_server.models.belgium_settlement import BelgiumSettlement  # noqa: E501
from openapi_server import util

def belgiumsettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BelgiumSettlement

    Gets a list of all instances of BelgiumSettlement (more information in http://dbpedia.org/ontology/BelgiumSettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BelgiumSettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BELGIUMSETTLEMENT_TYPE_URI,
        rdf_type_name=BELGIUMSETTLEMENT_TYPE_NAME, 
        kls=BelgiumSettlement)

def belgiumsettlements_id_get(id):  # noqa: E501
    """Get a single BelgiumSettlement by its id

    Gets the details of a given BelgiumSettlement (more information in http://dbpedia.org/ontology/BelgiumSettlement) # noqa: E501

    :param id: The ID of the BelgiumSettlement to be retrieved
    :type id: str

    :rtype: BelgiumSettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BELGIUMSETTLEMENT_TYPE_URI,
        rdf_type_name=BELGIUMSETTLEMENT_TYPE_NAME, 
        kls=BelgiumSettlement)
