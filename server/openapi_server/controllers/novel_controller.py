import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NOVEL_TYPE_NAME, NOVEL_TYPE_URI

from openapi_server.models.novel import Novel  # noqa: E501
from openapi_server import util

def novels_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Novel

    Gets a list of all instances of Novel (more information in http://dbpedia.org/ontology/Novel) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Novel]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NOVEL_TYPE_URI,
        rdf_type_name=NOVEL_TYPE_NAME, 
        kls=Novel)

def novels_id_get(id):  # noqa: E501
    """Get a single Novel by its id

    Gets the details of a given Novel (more information in http://dbpedia.org/ontology/Novel) # noqa: E501

    :param id: The ID of the Novel to be retrieved
    :type id: str

    :rtype: Novel
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NOVEL_TYPE_URI,
        rdf_type_name=NOVEL_TYPE_NAME, 
        kls=Novel)
