import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DEITY_TYPE_NAME, DEITY_TYPE_URI

from openapi_server.models.deity import Deity  # noqa: E501
from openapi_server import util

def deitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Deity

    Gets a list of all instances of Deity (more information in http://dbpedia.org/ontology/Deity) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Deity]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DEITY_TYPE_URI,
        rdf_type_name=DEITY_TYPE_NAME, 
        kls=Deity)

def deitys_id_get(id):  # noqa: E501
    """Get a single Deity by its id

    Gets the details of a given Deity (more information in http://dbpedia.org/ontology/Deity) # noqa: E501

    :param id: The ID of the Deity to be retrieved
    :type id: str

    :rtype: Deity
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DEITY_TYPE_URI,
        rdf_type_name=DEITY_TYPE_NAME, 
        kls=Deity)
