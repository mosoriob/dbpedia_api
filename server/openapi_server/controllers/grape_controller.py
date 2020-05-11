import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GRAPE_TYPE_NAME, GRAPE_TYPE_URI

from openapi_server.models.grape import Grape  # noqa: E501
from openapi_server import util

def grapes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Grape

    Gets a list of all instances of Grape (more information in http://dbpedia.org/ontology/Grape) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Grape]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GRAPE_TYPE_URI,
        rdf_type_name=GRAPE_TYPE_NAME, 
        kls=Grape)

def grapes_id_get(id):  # noqa: E501
    """Get a single Grape by its id

    Gets the details of a given Grape (more information in http://dbpedia.org/ontology/Grape) # noqa: E501

    :param id: The ID of the Grape to be retrieved
    :type id: str

    :rtype: Grape
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GRAPE_TYPE_URI,
        rdf_type_name=GRAPE_TYPE_NAME, 
        kls=Grape)
