import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DOCUMENT_TYPE_NAME, DOCUMENT_TYPE_URI

from openapi_server.models.document import Document  # noqa: E501
from openapi_server import util

def documents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Document

    Gets a list of all instances of Document (more information in http://dbpedia.org/ontology/Document) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Document]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DOCUMENT_TYPE_URI,
        rdf_type_name=DOCUMENT_TYPE_NAME, 
        kls=Document)

def documents_id_get(id):  # noqa: E501
    """Get a single Document by its id

    Gets the details of a given Document (more information in http://dbpedia.org/ontology/Document) # noqa: E501

    :param id: The ID of the Document to be retrieved
    :type id: str

    :rtype: Document
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DOCUMENT_TYPE_URI,
        rdf_type_name=DOCUMENT_TYPE_NAME, 
        kls=Document)
