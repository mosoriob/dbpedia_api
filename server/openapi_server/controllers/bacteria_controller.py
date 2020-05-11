import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BACTERIA_TYPE_NAME, BACTERIA_TYPE_URI

from openapi_server.models.bacteria import Bacteria  # noqa: E501
from openapi_server import util

def bacterias_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Bacteria

    Gets a list of all instances of Bacteria (more information in http://dbpedia.org/ontology/Bacteria) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Bacteria]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BACTERIA_TYPE_URI,
        rdf_type_name=BACTERIA_TYPE_NAME, 
        kls=Bacteria)

def bacterias_id_get(id):  # noqa: E501
    """Get a single Bacteria by its id

    Gets the details of a given Bacteria (more information in http://dbpedia.org/ontology/Bacteria) # noqa: E501

    :param id: The ID of the Bacteria to be retrieved
    :type id: str

    :rtype: Bacteria
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BACTERIA_TYPE_URI,
        rdf_type_name=BACTERIA_TYPE_NAME, 
        kls=Bacteria)
