import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WRITER_TYPE_NAME, WRITER_TYPE_URI

from openapi_server.models.writer import Writer  # noqa: E501
from openapi_server import util

def writers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Writer

    Gets a list of all instances of Writer (more information in http://dbpedia.org/ontology/Writer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Writer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WRITER_TYPE_URI,
        rdf_type_name=WRITER_TYPE_NAME, 
        kls=Writer)

def writers_id_get(id):  # noqa: E501
    """Get a single Writer by its id

    Gets the details of a given Writer (more information in http://dbpedia.org/ontology/Writer) # noqa: E501

    :param id: The ID of the Writer to be retrieved
    :type id: str

    :rtype: Writer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WRITER_TYPE_URI,
        rdf_type_name=WRITER_TYPE_NAME, 
        kls=Writer)
