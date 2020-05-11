import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MANHUA_TYPE_NAME, MANHUA_TYPE_URI

from openapi_server.models.manhua import Manhua  # noqa: E501
from openapi_server import util

def manhuas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Manhua

    Gets a list of all instances of Manhua (more information in http://dbpedia.org/ontology/Manhua) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Manhua]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MANHUA_TYPE_URI,
        rdf_type_name=MANHUA_TYPE_NAME, 
        kls=Manhua)

def manhuas_id_get(id):  # noqa: E501
    """Get a single Manhua by its id

    Gets the details of a given Manhua (more information in http://dbpedia.org/ontology/Manhua) # noqa: E501

    :param id: The ID of the Manhua to be retrieved
    :type id: str

    :rtype: Manhua
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MANHUA_TYPE_URI,
        rdf_type_name=MANHUA_TYPE_NAME, 
        kls=Manhua)
