import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GERMANSETTLEMENT_TYPE_NAME, GERMANSETTLEMENT_TYPE_URI

from openapi_server.models.german_settlement import GermanSettlement  # noqa: E501
from openapi_server import util

def germansettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GermanSettlement

    Gets a list of all instances of GermanSettlement (more information in http://dbpedia.org/ontology/GermanSettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GermanSettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GERMANSETTLEMENT_TYPE_URI,
        rdf_type_name=GERMANSETTLEMENT_TYPE_NAME, 
        kls=GermanSettlement)

def germansettlements_id_get(id):  # noqa: E501
    """Get a single GermanSettlement by its id

    Gets the details of a given GermanSettlement (more information in http://dbpedia.org/ontology/GermanSettlement) # noqa: E501

    :param id: The ID of the GermanSettlement to be retrieved
    :type id: str

    :rtype: GermanSettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GERMANSETTLEMENT_TYPE_URI,
        rdf_type_name=GERMANSETTLEMENT_TYPE_NAME, 
        kls=GermanSettlement)
