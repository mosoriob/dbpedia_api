import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FILE_TYPE_NAME, FILE_TYPE_URI

java.io.File  # noqa: E501
from openapi_server import util

def files_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of File

    Gets a list of all instances of File (more information in http://dbpedia.org/ontology/File) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[File]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FILE_TYPE_URI,
        rdf_type_name=FILE_TYPE_NAME, 
        kls=File)

def files_id_get(id):  # noqa: E501
    """Get a single File by its id

    Gets the details of a given File (more information in http://dbpedia.org/ontology/File) # noqa: E501

    :param id: The ID of the File to be retrieved
    :type id: str

    :rtype: File
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FILE_TYPE_URI,
        rdf_type_name=FILE_TYPE_NAME, 
        kls=File)
