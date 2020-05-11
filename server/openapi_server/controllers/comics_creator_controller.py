import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COMICSCREATOR_TYPE_NAME, COMICSCREATOR_TYPE_URI

from openapi_server.models.comics_creator import ComicsCreator  # noqa: E501
from openapi_server import util

def comicscreators_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ComicsCreator

    Gets a list of all instances of ComicsCreator (more information in http://dbpedia.org/ontology/ComicsCreator) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ComicsCreator]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COMICSCREATOR_TYPE_URI,
        rdf_type_name=COMICSCREATOR_TYPE_NAME, 
        kls=ComicsCreator)

def comicscreators_id_get(id):  # noqa: E501
    """Get a single ComicsCreator by its id

    Gets the details of a given ComicsCreator (more information in http://dbpedia.org/ontology/ComicsCreator) # noqa: E501

    :param id: The ID of the ComicsCreator to be retrieved
    :type id: str

    :rtype: ComicsCreator
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COMICSCREATOR_TYPE_URI,
        rdf_type_name=COMICSCREATOR_TYPE_NAME, 
        kls=ComicsCreator)
