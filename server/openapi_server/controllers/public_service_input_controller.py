import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PUBLICSERVICEINPUT_TYPE_NAME, PUBLICSERVICEINPUT_TYPE_URI

from openapi_server.models.public_service_input import PublicServiceInput  # noqa: E501
from openapi_server import util

def publicserviceinputs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PublicServiceInput

    Gets a list of all instances of PublicServiceInput (more information in http://dbpedia.org/ontology/PublicServiceInput) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PublicServiceInput]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PUBLICSERVICEINPUT_TYPE_URI,
        rdf_type_name=PUBLICSERVICEINPUT_TYPE_NAME, 
        kls=PublicServiceInput)

def publicserviceinputs_id_get(id):  # noqa: E501
    """Get a single PublicServiceInput by its id

    Gets the details of a given PublicServiceInput (more information in http://dbpedia.org/ontology/PublicServiceInput) # noqa: E501

    :param id: The ID of the PublicServiceInput to be retrieved
    :type id: str

    :rtype: PublicServiceInput
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PUBLICSERVICEINPUT_TYPE_URI,
        rdf_type_name=PUBLICSERVICEINPUT_TYPE_NAME, 
        kls=PublicServiceInput)
