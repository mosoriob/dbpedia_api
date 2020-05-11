import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PROFESSOR_TYPE_NAME, PROFESSOR_TYPE_URI

from openapi_server.models.professor import Professor  # noqa: E501
from openapi_server import util

def professors_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Professor

    Gets a list of all instances of Professor (more information in http://dbpedia.org/ontology/Professor) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Professor]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PROFESSOR_TYPE_URI,
        rdf_type_name=PROFESSOR_TYPE_NAME, 
        kls=Professor)

def professors_id_get(id):  # noqa: E501
    """Get a single Professor by its id

    Gets the details of a given Professor (more information in http://dbpedia.org/ontology/Professor) # noqa: E501

    :param id: The ID of the Professor to be retrieved
    :type id: str

    :rtype: Professor
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PROFESSOR_TYPE_URI,
        rdf_type_name=PROFESSOR_TYPE_NAME, 
        kls=Professor)
