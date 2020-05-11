import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DISNEYCHARACTER_TYPE_NAME, DISNEYCHARACTER_TYPE_URI

from openapi_server.models.disney_character import DisneyCharacter  # noqa: E501
from openapi_server import util

def disneycharacters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of DisneyCharacter

    Gets a list of all instances of DisneyCharacter (more information in http://dbpedia.org/ontology/DisneyCharacter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[DisneyCharacter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DISNEYCHARACTER_TYPE_URI,
        rdf_type_name=DISNEYCHARACTER_TYPE_NAME, 
        kls=DisneyCharacter)

def disneycharacters_id_get(id):  # noqa: E501
    """Get a single DisneyCharacter by its id

    Gets the details of a given DisneyCharacter (more information in http://dbpedia.org/ontology/DisneyCharacter) # noqa: E501

    :param id: The ID of the DisneyCharacter to be retrieved
    :type id: str

    :rtype: DisneyCharacter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DISNEYCHARACTER_TYPE_URI,
        rdf_type_name=DISNEYCHARACTER_TYPE_NAME, 
        kls=DisneyCharacter)
