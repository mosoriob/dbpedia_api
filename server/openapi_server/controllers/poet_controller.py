import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POET_TYPE_NAME, POET_TYPE_URI

from openapi_server.models.poet import Poet  # noqa: E501
from openapi_server import util

def poets_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Poet

    Gets a list of all instances of Poet (more information in http://dbpedia.org/ontology/Poet) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Poet]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POET_TYPE_URI,
        rdf_type_name=POET_TYPE_NAME, 
        kls=Poet)

def poets_id_get(id):  # noqa: E501
    """Get a single Poet by its id

    Gets the details of a given Poet (more information in http://dbpedia.org/ontology/Poet) # noqa: E501

    :param id: The ID of the Poet to be retrieved
    :type id: str

    :rtype: Poet
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POET_TYPE_URI,
        rdf_type_name=POET_TYPE_NAME, 
        kls=Poet)
