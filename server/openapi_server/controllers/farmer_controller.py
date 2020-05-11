import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FARMER_TYPE_NAME, FARMER_TYPE_URI

from openapi_server.models.farmer import Farmer  # noqa: E501
from openapi_server import util

def farmers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Farmer

    Gets a list of all instances of Farmer (more information in http://dbpedia.org/ontology/Farmer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Farmer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FARMER_TYPE_URI,
        rdf_type_name=FARMER_TYPE_NAME, 
        kls=Farmer)

def farmers_id_get(id):  # noqa: E501
    """Get a single Farmer by its id

    Gets the details of a given Farmer (more information in http://dbpedia.org/ontology/Farmer) # noqa: E501

    :param id: The ID of the Farmer to be retrieved
    :type id: str

    :rtype: Farmer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FARMER_TYPE_URI,
        rdf_type_name=FARMER_TYPE_NAME, 
        kls=Farmer)
