import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARCHAEA_TYPE_NAME, ARCHAEA_TYPE_URI

from openapi_server.models.archaea import Archaea  # noqa: E501
from openapi_server import util

def archaeas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Archaea

    Gets a list of all instances of Archaea (more information in http://dbpedia.org/ontology/Archaea) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Archaea]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARCHAEA_TYPE_URI,
        rdf_type_name=ARCHAEA_TYPE_NAME, 
        kls=Archaea)

def archaeas_id_get(id):  # noqa: E501
    """Get a single Archaea by its id

    Gets the details of a given Archaea (more information in http://dbpedia.org/ontology/Archaea) # noqa: E501

    :param id: The ID of the Archaea to be retrieved
    :type id: str

    :rtype: Archaea
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARCHAEA_TYPE_URI,
        rdf_type_name=ARCHAEA_TYPE_NAME, 
        kls=Archaea)
