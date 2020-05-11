import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PHOTOGRAPHER_TYPE_NAME, PHOTOGRAPHER_TYPE_URI

from openapi_server.models.photographer import Photographer  # noqa: E501
from openapi_server import util

def photographers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Photographer

    Gets a list of all instances of Photographer (more information in http://dbpedia.org/ontology/Photographer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Photographer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PHOTOGRAPHER_TYPE_URI,
        rdf_type_name=PHOTOGRAPHER_TYPE_NAME, 
        kls=Photographer)

def photographers_id_get(id):  # noqa: E501
    """Get a single Photographer by its id

    Gets the details of a given Photographer (more information in http://dbpedia.org/ontology/Photographer) # noqa: E501

    :param id: The ID of the Photographer to be retrieved
    :type id: str

    :rtype: Photographer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PHOTOGRAPHER_TYPE_URI,
        rdf_type_name=PHOTOGRAPHER_TYPE_NAME, 
        kls=Photographer)
