import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DIPLOMA_TYPE_NAME, DIPLOMA_TYPE_URI

from openapi_server.models.diploma import Diploma  # noqa: E501
from openapi_server import util

def diplomas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Diploma

    Gets a list of all instances of Diploma (more information in http://dbpedia.org/ontology/Diploma) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Diploma]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DIPLOMA_TYPE_URI,
        rdf_type_name=DIPLOMA_TYPE_NAME, 
        kls=Diploma)

def diplomas_id_get(id):  # noqa: E501
    """Get a single Diploma by its id

    Gets the details of a given Diploma (more information in http://dbpedia.org/ontology/Diploma) # noqa: E501

    :param id: The ID of the Diploma to be retrieved
    :type id: str

    :rtype: Diploma
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DIPLOMA_TYPE_URI,
        rdf_type_name=DIPLOMA_TYPE_NAME, 
        kls=Diploma)
