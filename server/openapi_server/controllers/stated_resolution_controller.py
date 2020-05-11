import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import STATEDRESOLUTION_TYPE_NAME, STATEDRESOLUTION_TYPE_URI

from openapi_server.models.stated_resolution import StatedResolution  # noqa: E501
from openapi_server import util

def statedresolutions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of StatedResolution

    Gets a list of all instances of StatedResolution (more information in http://dbpedia.org/ontology/StatedResolution) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[StatedResolution]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=STATEDRESOLUTION_TYPE_URI,
        rdf_type_name=STATEDRESOLUTION_TYPE_NAME, 
        kls=StatedResolution)

def statedresolutions_id_get(id):  # noqa: E501
    """Get a single StatedResolution by its id

    Gets the details of a given StatedResolution (more information in http://dbpedia.org/ontology/StatedResolution) # noqa: E501

    :param id: The ID of the StatedResolution to be retrieved
    :type id: str

    :rtype: StatedResolution
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=STATEDRESOLUTION_TYPE_URI,
        rdf_type_name=STATEDRESOLUTION_TYPE_NAME, 
        kls=StatedResolution)
