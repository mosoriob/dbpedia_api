import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AUSTRIANSETTLEMENT_TYPE_NAME, AUSTRIANSETTLEMENT_TYPE_URI

from openapi_server.models.austrian_settlement import AustrianSettlement  # noqa: E501
from openapi_server import util

def austriansettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AustrianSettlement

    Gets a list of all instances of AustrianSettlement (more information in http://dbpedia.org/ontology/AustrianSettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AustrianSettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AUSTRIANSETTLEMENT_TYPE_URI,
        rdf_type_name=AUSTRIANSETTLEMENT_TYPE_NAME, 
        kls=AustrianSettlement)

def austriansettlements_id_get(id):  # noqa: E501
    """Get a single AustrianSettlement by its id

    Gets the details of a given AustrianSettlement (more information in http://dbpedia.org/ontology/AustrianSettlement) # noqa: E501

    :param id: The ID of the AustrianSettlement to be retrieved
    :type id: str

    :rtype: AustrianSettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AUSTRIANSETTLEMENT_TYPE_URI,
        rdf_type_name=AUSTRIANSETTLEMENT_TYPE_NAME, 
        kls=AustrianSettlement)
