import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GUITAR_TYPE_NAME, GUITAR_TYPE_URI

from openapi_server.models.guitar import Guitar  # noqa: E501
from openapi_server import util

def guitars_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Guitar

    Gets a list of all instances of Guitar (more information in http://dbpedia.org/ontology/Guitar) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Guitar]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GUITAR_TYPE_URI,
        rdf_type_name=GUITAR_TYPE_NAME, 
        kls=Guitar)

def guitars_id_get(id):  # noqa: E501
    """Get a single Guitar by its id

    Gets the details of a given Guitar (more information in http://dbpedia.org/ontology/Guitar) # noqa: E501

    :param id: The ID of the Guitar to be retrieved
    :type id: str

    :rtype: Guitar
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GUITAR_TYPE_URI,
        rdf_type_name=GUITAR_TYPE_NAME, 
        kls=Guitar)
