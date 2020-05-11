import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DANCER_TYPE_NAME, DANCER_TYPE_URI

from openapi_server.models.dancer import Dancer  # noqa: E501
from openapi_server import util

def dancers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Dancer

    Gets a list of all instances of Dancer (more information in http://dbpedia.org/ontology/Dancer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Dancer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DANCER_TYPE_URI,
        rdf_type_name=DANCER_TYPE_NAME, 
        kls=Dancer)

def dancers_id_get(id):  # noqa: E501
    """Get a single Dancer by its id

    Gets the details of a given Dancer (more information in http://dbpedia.org/ontology/Dancer) # noqa: E501

    :param id: The ID of the Dancer to be retrieved
    :type id: str

    :rtype: Dancer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DANCER_TYPE_URI,
        rdf_type_name=DANCER_TYPE_NAME, 
        kls=Dancer)
