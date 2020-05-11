import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PUBLICSERVICEOUTPUT_TYPE_NAME, PUBLICSERVICEOUTPUT_TYPE_URI

from openapi_server.models.public_service_output import PublicServiceOutput  # noqa: E501
from openapi_server import util

def publicserviceoutputs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PublicServiceOutput

    Gets a list of all instances of PublicServiceOutput (more information in http://dbpedia.org/ontology/PublicServiceOutput) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PublicServiceOutput]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PUBLICSERVICEOUTPUT_TYPE_URI,
        rdf_type_name=PUBLICSERVICEOUTPUT_TYPE_NAME, 
        kls=PublicServiceOutput)

def publicserviceoutputs_id_get(id):  # noqa: E501
    """Get a single PublicServiceOutput by its id

    Gets the details of a given PublicServiceOutput (more information in http://dbpedia.org/ontology/PublicServiceOutput) # noqa: E501

    :param id: The ID of the PublicServiceOutput to be retrieved
    :type id: str

    :rtype: PublicServiceOutput
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PUBLICSERVICEOUTPUT_TYPE_URI,
        rdf_type_name=PUBLICSERVICEOUTPUT_TYPE_NAME, 
        kls=PublicServiceOutput)
