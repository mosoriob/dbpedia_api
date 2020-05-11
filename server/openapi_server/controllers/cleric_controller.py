import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CLERIC_TYPE_NAME, CLERIC_TYPE_URI

from openapi_server.models.cleric import Cleric  # noqa: E501
from openapi_server import util

def clerics_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Cleric

    Gets a list of all instances of Cleric (more information in http://dbpedia.org/ontology/Cleric) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Cleric]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CLERIC_TYPE_URI,
        rdf_type_name=CLERIC_TYPE_NAME, 
        kls=Cleric)

def clerics_id_get(id):  # noqa: E501
    """Get a single Cleric by its id

    Gets the details of a given Cleric (more information in http://dbpedia.org/ontology/Cleric) # noqa: E501

    :param id: The ID of the Cleric to be retrieved
    :type id: str

    :rtype: Cleric
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CLERIC_TYPE_URI,
        rdf_type_name=CLERIC_TYPE_NAME, 
        kls=Cleric)
