import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CELEBRITY_TYPE_NAME, CELEBRITY_TYPE_URI

from openapi_server.models.celebrity import Celebrity  # noqa: E501
from openapi_server import util

def celebritys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Celebrity

    Gets a list of all instances of Celebrity (more information in http://dbpedia.org/ontology/Celebrity) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Celebrity]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CELEBRITY_TYPE_URI,
        rdf_type_name=CELEBRITY_TYPE_NAME, 
        kls=Celebrity)

def celebritys_id_get(id):  # noqa: E501
    """Get a single Celebrity by its id

    Gets the details of a given Celebrity (more information in http://dbpedia.org/ontology/Celebrity) # noqa: E501

    :param id: The ID of the Celebrity to be retrieved
    :type id: str

    :rtype: Celebrity
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CELEBRITY_TYPE_URI,
        rdf_type_name=CELEBRITY_TYPE_NAME, 
        kls=Celebrity)
