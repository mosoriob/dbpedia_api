import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NARUTOCHARACTER_TYPE_NAME, NARUTOCHARACTER_TYPE_URI

from openapi_server.models.naruto_character import NarutoCharacter  # noqa: E501
from openapi_server import util

def narutocharacters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NarutoCharacter

    Gets a list of all instances of NarutoCharacter (more information in http://dbpedia.org/ontology/NarutoCharacter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NarutoCharacter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NARUTOCHARACTER_TYPE_URI,
        rdf_type_name=NARUTOCHARACTER_TYPE_NAME, 
        kls=NarutoCharacter)

def narutocharacters_id_get(id):  # noqa: E501
    """Get a single NarutoCharacter by its id

    Gets the details of a given NarutoCharacter (more information in http://dbpedia.org/ontology/NarutoCharacter) # noqa: E501

    :param id: The ID of the NarutoCharacter to be retrieved
    :type id: str

    :rtype: NarutoCharacter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NARUTOCHARACTER_TYPE_URI,
        rdf_type_name=NARUTOCHARACTER_TYPE_NAME, 
        kls=NarutoCharacter)
