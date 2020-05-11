import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MONARCH_TYPE_NAME, MONARCH_TYPE_URI

from openapi_server.models.monarch import Monarch  # noqa: E501
from openapi_server import util

def monarchs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Monarch

    Gets a list of all instances of Monarch (more information in http://dbpedia.org/ontology/Monarch) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Monarch]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MONARCH_TYPE_URI,
        rdf_type_name=MONARCH_TYPE_NAME, 
        kls=Monarch)

def monarchs_id_get(id):  # noqa: E501
    """Get a single Monarch by its id

    Gets the details of a given Monarch (more information in http://dbpedia.org/ontology/Monarch) # noqa: E501

    :param id: The ID of the Monarch to be retrieved
    :type id: str

    :rtype: Monarch
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MONARCH_TYPE_URI,
        rdf_type_name=MONARCH_TYPE_NAME, 
        kls=Monarch)
