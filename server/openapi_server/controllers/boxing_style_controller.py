import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BOXINGSTYLE_TYPE_NAME, BOXINGSTYLE_TYPE_URI

from openapi_server.models.boxing_style import BoxingStyle  # noqa: E501
from openapi_server import util

def boxingstyles_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BoxingStyle

    Gets a list of all instances of BoxingStyle (more information in http://dbpedia.org/ontology/BoxingStyle) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BoxingStyle]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BOXINGSTYLE_TYPE_URI,
        rdf_type_name=BOXINGSTYLE_TYPE_NAME, 
        kls=BoxingStyle)

def boxingstyles_id_get(id):  # noqa: E501
    """Get a single BoxingStyle by its id

    Gets the details of a given BoxingStyle (more information in http://dbpedia.org/ontology/BoxingStyle) # noqa: E501

    :param id: The ID of the BoxingStyle to be retrieved
    :type id: str

    :rtype: BoxingStyle
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BOXINGSTYLE_TYPE_URI,
        rdf_type_name=BOXINGSTYLE_TYPE_NAME, 
        kls=BoxingStyle)
