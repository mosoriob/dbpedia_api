import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CANOEIST_TYPE_NAME, CANOEIST_TYPE_URI

from openapi_server.models.canoeist import Canoeist  # noqa: E501
from openapi_server import util

def canoeists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Canoeist

    Gets a list of all instances of Canoeist (more information in http://dbpedia.org/ontology/Canoeist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Canoeist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CANOEIST_TYPE_URI,
        rdf_type_name=CANOEIST_TYPE_NAME, 
        kls=Canoeist)

def canoeists_id_get(id):  # noqa: E501
    """Get a single Canoeist by its id

    Gets the details of a given Canoeist (more information in http://dbpedia.org/ontology/Canoeist) # noqa: E501

    :param id: The ID of the Canoeist to be retrieved
    :type id: str

    :rtype: Canoeist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CANOEIST_TYPE_URI,
        rdf_type_name=CANOEIST_TYPE_NAME, 
        kls=Canoeist)
