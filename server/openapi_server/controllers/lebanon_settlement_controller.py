import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LEBANONSETTLEMENT_TYPE_NAME, LEBANONSETTLEMENT_TYPE_URI

from openapi_server.models.lebanon_settlement import LebanonSettlement  # noqa: E501
from openapi_server import util

def lebanonsettlements_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of LebanonSettlement

    Gets a list of all instances of LebanonSettlement (more information in http://dbpedia.org/ontology/LebanonSettlement) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[LebanonSettlement]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LEBANONSETTLEMENT_TYPE_URI,
        rdf_type_name=LEBANONSETTLEMENT_TYPE_NAME, 
        kls=LebanonSettlement)

def lebanonsettlements_id_get(id):  # noqa: E501
    """Get a single LebanonSettlement by its id

    Gets the details of a given LebanonSettlement (more information in http://dbpedia.org/ontology/LebanonSettlement) # noqa: E501

    :param id: The ID of the LebanonSettlement to be retrieved
    :type id: str

    :rtype: LebanonSettlement
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LEBANONSETTLEMENT_TYPE_URI,
        rdf_type_name=LEBANONSETTLEMENT_TYPE_NAME, 
        kls=LebanonSettlement)
