import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BOOK_TYPE_NAME, BOOK_TYPE_URI

from openapi_server.models.book import Book  # noqa: E501
from openapi_server import util

def books_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Book

    Gets a list of all instances of Book (more information in http://dbpedia.org/ontology/Book) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Book]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BOOK_TYPE_URI,
        rdf_type_name=BOOK_TYPE_NAME, 
        kls=Book)

def books_id_get(id):  # noqa: E501
    """Get a single Book by its id

    Gets the details of a given Book (more information in http://dbpedia.org/ontology/Book) # noqa: E501

    :param id: The ID of the Book to be retrieved
    :type id: str

    :rtype: Book
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BOOK_TYPE_URI,
        rdf_type_name=BOOK_TYPE_NAME, 
        kls=Book)
