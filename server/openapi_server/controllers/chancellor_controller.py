import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHANCELLOR_TYPE_NAME, CHANCELLOR_TYPE_URI

from openapi_server.models.chancellor import Chancellor  # noqa: E501
from openapi_server import util

def chancellors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Chancellor

    Gets a list of all instances of Chancellor (more information in http://dbpedia.org/ontology/Chancellor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Chancellor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHANCELLOR_TYPE_URI,
        rdf_type_name=CHANCELLOR_TYPE_NAME, 
        kls=Chancellor)

def chancellors_id_get(id):  # noqa: E501
    """Get a single Chancellor by its id

    Gets the details of a given Chancellor (more information in http://dbpedia.org/ontology/Chancellor) # noqa: E501

    :param id: The ID of the Chancellor to be retrieved
    :type id: str

    :rtype: Chancellor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHANCELLOR_TYPE_URI,
        rdf_type_name=CHANCELLOR_TYPE_NAME, 
        kls=Chancellor)
