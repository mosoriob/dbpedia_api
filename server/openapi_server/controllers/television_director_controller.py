import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TELEVISIONDIRECTOR_TYPE_NAME, TELEVISIONDIRECTOR_TYPE_URI

from openapi_server.models.television_director import TelevisionDirector  # noqa: E501
from openapi_server import util

def televisiondirectors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TelevisionDirector

    Gets a list of all instances of TelevisionDirector (more information in http://dbpedia.org/ontology/TelevisionDirector) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TelevisionDirector]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TELEVISIONDIRECTOR_TYPE_URI,
        rdf_type_name=TELEVISIONDIRECTOR_TYPE_NAME, 
        kls=TelevisionDirector)

def televisiondirectors_id_get(id):  # noqa: E501
    """Get a single TelevisionDirector by its id

    Gets the details of a given TelevisionDirector (more information in http://dbpedia.org/ontology/TelevisionDirector) # noqa: E501

    :param id: The ID of the TelevisionDirector to be retrieved
    :type id: str

    :rtype: TelevisionDirector
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TELEVISIONDIRECTOR_TYPE_URI,
        rdf_type_name=TELEVISIONDIRECTOR_TYPE_NAME, 
        kls=TelevisionDirector)
