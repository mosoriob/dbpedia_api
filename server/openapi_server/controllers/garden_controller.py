import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GARDEN_TYPE_NAME, GARDEN_TYPE_URI

from openapi_server.models.garden import Garden  # noqa: E501
from openapi_server import util

def gardens_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Garden

    Gets a list of all instances of Garden (more information in http://dbpedia.org/ontology/Garden) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Garden]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GARDEN_TYPE_URI,
        rdf_type_name=GARDEN_TYPE_NAME, 
        kls=Garden)

def gardens_id_get(id):  # noqa: E501
    """Get a single Garden by its id

    Gets the details of a given Garden (more information in http://dbpedia.org/ontology/Garden) # noqa: E501

    :param id: The ID of the Garden to be retrieved
    :type id: str

    :rtype: Garden
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GARDEN_TYPE_URI,
        rdf_type_name=GARDEN_TYPE_NAME, 
        kls=Garden)
