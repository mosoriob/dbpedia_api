import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOAPCHARACTER_TYPE_NAME, SOAPCHARACTER_TYPE_URI

from openapi_server.models.soap_character import SoapCharacter  # noqa: E501
from openapi_server import util

def soapcharacters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoapCharacter

    Gets a list of all instances of SoapCharacter (more information in http://dbpedia.org/ontology/SoapCharacter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoapCharacter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOAPCHARACTER_TYPE_URI,
        rdf_type_name=SOAPCHARACTER_TYPE_NAME, 
        kls=SoapCharacter)

def soapcharacters_id_get(id):  # noqa: E501
    """Get a single SoapCharacter by its id

    Gets the details of a given SoapCharacter (more information in http://dbpedia.org/ontology/SoapCharacter) # noqa: E501

    :param id: The ID of the SoapCharacter to be retrieved
    :type id: str

    :rtype: SoapCharacter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOAPCHARACTER_TYPE_URI,
        rdf_type_name=SOAPCHARACTER_TYPE_NAME, 
        kls=SoapCharacter)
