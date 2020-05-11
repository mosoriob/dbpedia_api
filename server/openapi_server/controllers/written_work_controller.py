import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WRITTENWORK_TYPE_NAME, WRITTENWORK_TYPE_URI

from openapi_server.models.written_work import WrittenWork  # noqa: E501
from openapi_server import util

def writtenworks_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of WrittenWork

    Gets a list of all instances of WrittenWork (more information in http://dbpedia.org/ontology/WrittenWork) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[WrittenWork]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WRITTENWORK_TYPE_URI,
        rdf_type_name=WRITTENWORK_TYPE_NAME, 
        kls=WrittenWork)

def writtenworks_id_get(id):  # noqa: E501
    """Get a single WrittenWork by its id

    Gets the details of a given WrittenWork (more information in http://dbpedia.org/ontology/WrittenWork) # noqa: E501

    :param id: The ID of the WrittenWork to be retrieved
    :type id: str

    :rtype: WrittenWork
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WRITTENWORK_TYPE_URI,
        rdf_type_name=WRITTENWORK_TYPE_NAME, 
        kls=WrittenWork)
