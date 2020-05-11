import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ANIMANGACHARACTER_TYPE_NAME, ANIMANGACHARACTER_TYPE_URI

from openapi_server.models.animanga_character import AnimangaCharacter  # noqa: E501
from openapi_server import util

def animangacharacters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AnimangaCharacter

    Gets a list of all instances of AnimangaCharacter (more information in http://dbpedia.org/ontology/AnimangaCharacter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AnimangaCharacter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ANIMANGACHARACTER_TYPE_URI,
        rdf_type_name=ANIMANGACHARACTER_TYPE_NAME, 
        kls=AnimangaCharacter)

def animangacharacters_id_get(id):  # noqa: E501
    """Get a single AnimangaCharacter by its id

    Gets the details of a given AnimangaCharacter (more information in http://dbpedia.org/ontology/AnimangaCharacter) # noqa: E501

    :param id: The ID of the AnimangaCharacter to be retrieved
    :type id: str

    :rtype: AnimangaCharacter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ANIMANGACHARACTER_TYPE_URI,
        rdf_type_name=ANIMANGACHARACTER_TYPE_NAME, 
        kls=AnimangaCharacter)
