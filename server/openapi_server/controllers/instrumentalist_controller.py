import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import INSTRUMENTALIST_TYPE_NAME, INSTRUMENTALIST_TYPE_URI

from openapi_server.models.instrumentalist import Instrumentalist  # noqa: E501
from openapi_server import util

def instrumentalists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Instrumentalist

    Gets a list of all instances of Instrumentalist (more information in http://dbpedia.org/ontology/Instrumentalist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Instrumentalist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=INSTRUMENTALIST_TYPE_URI,
        rdf_type_name=INSTRUMENTALIST_TYPE_NAME, 
        kls=Instrumentalist)

def instrumentalists_id_get(id):  # noqa: E501
    """Get a single Instrumentalist by its id

    Gets the details of a given Instrumentalist (more information in http://dbpedia.org/ontology/Instrumentalist) # noqa: E501

    :param id: The ID of the Instrumentalist to be retrieved
    :type id: str

    :rtype: Instrumentalist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=INSTRUMENTALIST_TYPE_URI,
        rdf_type_name=INSTRUMENTALIST_TYPE_NAME, 
        kls=Instrumentalist)
