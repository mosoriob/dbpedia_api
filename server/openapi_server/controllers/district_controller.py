import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DISTRICT_TYPE_NAME, DISTRICT_TYPE_URI

from openapi_server.models.district import District  # noqa: E501
from openapi_server import util

def districts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of District

    Gets a list of all instances of District (more information in http://dbpedia.org/ontology/District) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[District]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DISTRICT_TYPE_URI,
        rdf_type_name=DISTRICT_TYPE_NAME, 
        kls=District)

def districts_id_get(id):  # noqa: E501
    """Get a single District by its id

    Gets the details of a given District (more information in http://dbpedia.org/ontology/District) # noqa: E501

    :param id: The ID of the District to be retrieved
    :type id: str

    :rtype: District
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DISTRICT_TYPE_URI,
        rdf_type_name=DISTRICT_TYPE_NAME, 
        kls=District)
