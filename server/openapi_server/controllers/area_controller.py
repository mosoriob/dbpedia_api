import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AREA_TYPE_NAME, AREA_TYPE_URI

from openapi_server.models.area import Area  # noqa: E501
from openapi_server import util

def areas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Area

    Gets a list of all instances of Area (more information in http://dbpedia.org/ontology/Area) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Area]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AREA_TYPE_URI,
        rdf_type_name=AREA_TYPE_NAME, 
        kls=Area)

def areas_id_get(id):  # noqa: E501
    """Get a single Area by its id

    Gets the details of a given Area (more information in http://dbpedia.org/ontology/Area) # noqa: E501

    :param id: The ID of the Area to be retrieved
    :type id: str

    :rtype: Area
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AREA_TYPE_URI,
        rdf_type_name=AREA_TYPE_NAME, 
        kls=Area)
