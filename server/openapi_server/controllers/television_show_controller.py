import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TELEVISIONSHOW_TYPE_NAME, TELEVISIONSHOW_TYPE_URI

from openapi_server.models.television_show import TelevisionShow  # noqa: E501
from openapi_server import util

def televisionshows_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TelevisionShow

    Gets a list of all instances of TelevisionShow (more information in http://dbpedia.org/ontology/TelevisionShow) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TelevisionShow]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TELEVISIONSHOW_TYPE_URI,
        rdf_type_name=TELEVISIONSHOW_TYPE_NAME, 
        kls=TelevisionShow)

def televisionshows_id_get(id):  # noqa: E501
    """Get a single TelevisionShow by its id

    Gets the details of a given TelevisionShow (more information in http://dbpedia.org/ontology/TelevisionShow) # noqa: E501

    :param id: The ID of the TelevisionShow to be retrieved
    :type id: str

    :rtype: TelevisionShow
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TELEVISIONSHOW_TYPE_URI,
        rdf_type_name=TELEVISIONSHOW_TYPE_NAME, 
        kls=TelevisionShow)
