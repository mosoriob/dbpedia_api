import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WORK_TYPE_NAME, WORK_TYPE_URI

from openapi_server.models.work import Work  # noqa: E501
from openapi_server import util

def works_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Work

    Gets a list of all instances of Work (more information in http://dbpedia.org/ontology/Work) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Work]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WORK_TYPE_URI,
        rdf_type_name=WORK_TYPE_NAME, 
        kls=Work)

def works_id_get(id):  # noqa: E501
    """Get a single Work by its id

    Gets the details of a given Work (more information in http://dbpedia.org/ontology/Work) # noqa: E501

    :param id: The ID of the Work to be retrieved
    :type id: str

    :rtype: Work
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WORK_TYPE_URI,
        rdf_type_name=WORK_TYPE_NAME, 
        kls=Work)
