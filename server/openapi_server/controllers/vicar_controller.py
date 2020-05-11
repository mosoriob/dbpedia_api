import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VICAR_TYPE_NAME, VICAR_TYPE_URI

from openapi_server.models.vicar import Vicar  # noqa: E501
from openapi_server import util

def vicars_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Vicar

    Gets a list of all instances of Vicar (more information in http://dbpedia.org/ontology/Vicar) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Vicar]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VICAR_TYPE_URI,
        rdf_type_name=VICAR_TYPE_NAME, 
        kls=Vicar)

def vicars_id_get(id):  # noqa: E501
    """Get a single Vicar by its id

    Gets the details of a given Vicar (more information in http://dbpedia.org/ontology/Vicar) # noqa: E501

    :param id: The ID of the Vicar to be retrieved
    :type id: str

    :rtype: Vicar
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VICAR_TYPE_URI,
        rdf_type_name=VICAR_TYPE_NAME, 
        kls=Vicar)
