import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BUILDING_TYPE_NAME, BUILDING_TYPE_URI

from openapi_server.models.building import Building  # noqa: E501
from openapi_server import util

def buildings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Building

    Gets a list of all instances of Building (more information in http://dbpedia.org/ontology/Building) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Building]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BUILDING_TYPE_URI,
        rdf_type_name=BUILDING_TYPE_NAME, 
        kls=Building)

def buildings_id_get(id):  # noqa: E501
    """Get a single Building by its id

    Gets the details of a given Building (more information in http://dbpedia.org/ontology/Building) # noqa: E501

    :param id: The ID of the Building to be retrieved
    :type id: str

    :rtype: Building
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BUILDING_TYPE_URI,
        rdf_type_name=BUILDING_TYPE_NAME, 
        kls=Building)
