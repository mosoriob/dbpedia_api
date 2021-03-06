import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COMICSCHARACTER_TYPE_NAME, COMICSCHARACTER_TYPE_URI

from openapi_server.models.comics_character import ComicsCharacter  # noqa: E501
from openapi_server import util

def comicscharacters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ComicsCharacter

    Gets a list of all instances of ComicsCharacter (more information in http://dbpedia.org/ontology/ComicsCharacter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ComicsCharacter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COMICSCHARACTER_TYPE_URI,
        rdf_type_name=COMICSCHARACTER_TYPE_NAME, 
        kls=ComicsCharacter)

def comicscharacters_id_get(id):  # noqa: E501
    """Get a single ComicsCharacter by its id

    Gets the details of a given ComicsCharacter (more information in http://dbpedia.org/ontology/ComicsCharacter) # noqa: E501

    :param id: The ID of the ComicsCharacter to be retrieved
    :type id: str

    :rtype: ComicsCharacter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COMICSCHARACTER_TYPE_URI,
        rdf_type_name=COMICSCHARACTER_TYPE_NAME, 
        kls=ComicsCharacter)
