import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DOCUMENTTYPE_TYPE_NAME, DOCUMENTTYPE_TYPE_URI

from openapi_server.models.document_type import DocumentType  # noqa: E501
from openapi_server import util

def documenttypes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of DocumentType

    Gets a list of all instances of DocumentType (more information in http://dbpedia.org/ontology/DocumentType) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[DocumentType]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DOCUMENTTYPE_TYPE_URI,
        rdf_type_name=DOCUMENTTYPE_TYPE_NAME, 
        kls=DocumentType)

def documenttypes_id_get(id):  # noqa: E501
    """Get a single DocumentType by its id

    Gets the details of a given DocumentType (more information in http://dbpedia.org/ontology/DocumentType) # noqa: E501

    :param id: The ID of the DocumentType to be retrieved
    :type id: str

    :rtype: DocumentType
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DOCUMENTTYPE_TYPE_URI,
        rdf_type_name=DOCUMENTTYPE_TYPE_NAME, 
        kls=DocumentType)
