import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PUBLICSERVICE_TYPE_NAME, PUBLICSERVICE_TYPE_URI

from openapi_server.models.public_service import PublicService  # noqa: E501
from openapi_server import util

def publicservices_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PublicService

    Gets a list of all instances of PublicService (more information in http://dbpedia.org/ontology/PublicService) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PublicService]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PUBLICSERVICE_TYPE_URI,
        rdf_type_name=PUBLICSERVICE_TYPE_NAME, 
        kls=PublicService)

def publicservices_id_get(id):  # noqa: E501
    """Get a single PublicService by its id

    Gets the details of a given PublicService (more information in http://dbpedia.org/ontology/PublicService) # noqa: E501

    :param id: The ID of the PublicService to be retrieved
    :type id: str

    :rtype: PublicService
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PUBLICSERVICE_TYPE_URI,
        rdf_type_name=PUBLICSERVICE_TYPE_NAME, 
        kls=PublicService)
