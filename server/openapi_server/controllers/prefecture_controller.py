import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PREFECTURE_TYPE_NAME, PREFECTURE_TYPE_URI

from openapi_server.models.prefecture import Prefecture  # noqa: E501
from openapi_server import util

def prefectures_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Prefecture

    Gets a list of all instances of Prefecture (more information in http://dbpedia.org/ontology/Prefecture) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Prefecture]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PREFECTURE_TYPE_URI,
        rdf_type_name=PREFECTURE_TYPE_NAME, 
        kls=Prefecture)

def prefectures_id_get(id):  # noqa: E501
    """Get a single Prefecture by its id

    Gets the details of a given Prefecture (more information in http://dbpedia.org/ontology/Prefecture) # noqa: E501

    :param id: The ID of the Prefecture to be retrieved
    :type id: str

    :rtype: Prefecture
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PREFECTURE_TYPE_URI,
        rdf_type_name=PREFECTURE_TYPE_NAME, 
        kls=Prefecture)
