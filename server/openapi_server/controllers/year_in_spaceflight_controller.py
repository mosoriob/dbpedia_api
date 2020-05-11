import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import YEARINSPACEFLIGHT_TYPE_NAME, YEARINSPACEFLIGHT_TYPE_URI

from openapi_server.models.year_in_spaceflight import YearInSpaceflight  # noqa: E501
from openapi_server import util

def yearinspaceflights_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of YearInSpaceflight

    Gets a list of all instances of YearInSpaceflight (more information in http://dbpedia.org/ontology/YearInSpaceflight) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[YearInSpaceflight]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=YEARINSPACEFLIGHT_TYPE_URI,
        rdf_type_name=YEARINSPACEFLIGHT_TYPE_NAME, 
        kls=YearInSpaceflight)

def yearinspaceflights_id_get(id):  # noqa: E501
    """Get a single YearInSpaceflight by its id

    Gets the details of a given YearInSpaceflight (more information in http://dbpedia.org/ontology/YearInSpaceflight) # noqa: E501

    :param id: The ID of the YearInSpaceflight to be retrieved
    :type id: str

    :rtype: YearInSpaceflight
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=YEARINSPACEFLIGHT_TYPE_URI,
        rdf_type_name=YEARINSPACEFLIGHT_TYPE_NAME, 
        kls=YearInSpaceflight)
