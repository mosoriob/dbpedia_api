import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FICTIONALCHARACTER_TYPE_NAME, FICTIONALCHARACTER_TYPE_URI

from openapi_server.models.fictional_character import FictionalCharacter  # noqa: E501
from openapi_server import util

def fictionalcharacters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of FictionalCharacter

    Gets a list of all instances of FictionalCharacter (more information in http://dbpedia.org/ontology/FictionalCharacter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[FictionalCharacter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FICTIONALCHARACTER_TYPE_URI,
        rdf_type_name=FICTIONALCHARACTER_TYPE_NAME, 
        kls=FictionalCharacter)

def fictionalcharacters_id_get(id):  # noqa: E501
    """Get a single FictionalCharacter by its id

    Gets the details of a given FictionalCharacter (more information in http://dbpedia.org/ontology/FictionalCharacter) # noqa: E501

    :param id: The ID of the FictionalCharacter to be retrieved
    :type id: str

    :rtype: FictionalCharacter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FICTIONALCHARACTER_TYPE_URI,
        rdf_type_name=FICTIONALCHARACTER_TYPE_NAME, 
        kls=FictionalCharacter)
