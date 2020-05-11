import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SKIAREA_TYPE_NAME, SKIAREA_TYPE_URI

from openapi_server.models.ski_area import SkiArea  # noqa: E501
from openapi_server import util

def skiareas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SkiArea

    Gets a list of all instances of SkiArea (more information in http://dbpedia.org/ontology/SkiArea) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SkiArea]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SKIAREA_TYPE_URI,
        rdf_type_name=SKIAREA_TYPE_NAME, 
        kls=SkiArea)

def skiareas_id_get(id):  # noqa: E501
    """Get a single SkiArea by its id

    Gets the details of a given SkiArea (more information in http://dbpedia.org/ontology/SkiArea) # noqa: E501

    :param id: The ID of the SkiArea to be retrieved
    :type id: str

    :rtype: SkiArea
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SKIAREA_TYPE_URI,
        rdf_type_name=SKIAREA_TYPE_NAME, 
        kls=SkiArea)
