import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TOWN_TYPE_NAME, TOWN_TYPE_URI

from openapi_server.models.town import Town  # noqa: E501
from openapi_server import util

def towns_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Town

    Gets a list of all instances of Town (more information in http://dbpedia.org/ontology/Town) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Town]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TOWN_TYPE_URI,
        rdf_type_name=TOWN_TYPE_NAME, 
        kls=Town)

def towns_id_get(id):  # noqa: E501
    """Get a single Town by its id

    Gets the details of a given Town (more information in http://dbpedia.org/ontology/Town) # noqa: E501

    :param id: The ID of the Town to be retrieved
    :type id: str

    :rtype: Town
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TOWN_TYPE_URI,
        rdf_type_name=TOWN_TYPE_NAME, 
        kls=Town)
