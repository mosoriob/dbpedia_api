import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LETTER_TYPE_NAME, LETTER_TYPE_URI

from openapi_server.models.letter import Letter  # noqa: E501
from openapi_server import util

def letters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Letter

    Gets a list of all instances of Letter (more information in http://dbpedia.org/ontology/Letter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Letter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LETTER_TYPE_URI,
        rdf_type_name=LETTER_TYPE_NAME, 
        kls=Letter)

def letters_id_get(id):  # noqa: E501
    """Get a single Letter by its id

    Gets the details of a given Letter (more information in http://dbpedia.org/ontology/Letter) # noqa: E501

    :param id: The ID of the Letter to be retrieved
    :type id: str

    :rtype: Letter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LETTER_TYPE_URI,
        rdf_type_name=LETTER_TYPE_NAME, 
        kls=Letter)
