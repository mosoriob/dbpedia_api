import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GRAVEMONUMENT_TYPE_NAME, GRAVEMONUMENT_TYPE_URI

from openapi_server.models.grave_monument import GraveMonument  # noqa: E501
from openapi_server import util

def gravemonuments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GraveMonument

    Gets a list of all instances of GraveMonument (more information in http://dbpedia.org/ontology/GraveMonument) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GraveMonument]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GRAVEMONUMENT_TYPE_URI,
        rdf_type_name=GRAVEMONUMENT_TYPE_NAME, 
        kls=GraveMonument)

def gravemonuments_id_get(id):  # noqa: E501
    """Get a single GraveMonument by its id

    Gets the details of a given GraveMonument (more information in http://dbpedia.org/ontology/GraveMonument) # noqa: E501

    :param id: The ID of the GraveMonument to be retrieved
    :type id: str

    :rtype: GraveMonument
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GRAVEMONUMENT_TYPE_URI,
        rdf_type_name=GRAVEMONUMENT_TYPE_NAME, 
        kls=GraveMonument)
