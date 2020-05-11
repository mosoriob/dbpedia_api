import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PARISH_TYPE_NAME, PARISH_TYPE_URI

from openapi_server.models.parish import Parish  # noqa: E501
from openapi_server import util

def parishs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Parish

    Gets a list of all instances of Parish (more information in http://dbpedia.org/ontology/Parish) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Parish]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PARISH_TYPE_URI,
        rdf_type_name=PARISH_TYPE_NAME, 
        kls=Parish)

def parishs_id_get(id):  # noqa: E501
    """Get a single Parish by its id

    Gets the details of a given Parish (more information in http://dbpedia.org/ontology/Parish) # noqa: E501

    :param id: The ID of the Parish to be retrieved
    :type id: str

    :rtype: Parish
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PARISH_TYPE_URI,
        rdf_type_name=PARISH_TYPE_NAME, 
        kls=Parish)
