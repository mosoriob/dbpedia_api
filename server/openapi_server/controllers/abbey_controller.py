import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ABBEY_TYPE_NAME, ABBEY_TYPE_URI

from openapi_server.models.abbey import Abbey  # noqa: E501
from openapi_server import util

def abbeys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Abbey

    Gets a list of all instances of Abbey (more information in http://dbpedia.org/ontology/Abbey) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Abbey]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ABBEY_TYPE_URI,
        rdf_type_name=ABBEY_TYPE_NAME, 
        kls=Abbey)

def abbeys_id_get(id):  # noqa: E501
    """Get a single Abbey by its id

    Gets the details of a given Abbey (more information in http://dbpedia.org/ontology/Abbey) # noqa: E501

    :param id: The ID of the Abbey to be retrieved
    :type id: str

    :rtype: Abbey
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ABBEY_TYPE_URI,
        rdf_type_name=ABBEY_TYPE_NAME, 
        kls=Abbey)
