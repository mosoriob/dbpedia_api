import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POEM_TYPE_NAME, POEM_TYPE_URI

from openapi_server.models.poem import Poem  # noqa: E501
from openapi_server import util

def poems_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Poem

    Gets a list of all instances of Poem (more information in http://dbpedia.org/ontology/Poem) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Poem]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POEM_TYPE_URI,
        rdf_type_name=POEM_TYPE_NAME, 
        kls=Poem)

def poems_id_get(id):  # noqa: E501
    """Get a single Poem by its id

    Gets the details of a given Poem (more information in http://dbpedia.org/ontology/Poem) # noqa: E501

    :param id: The ID of the Poem to be retrieved
    :type id: str

    :rtype: Poem
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POEM_TYPE_URI,
        rdf_type_name=POEM_TYPE_NAME, 
        kls=Poem)
