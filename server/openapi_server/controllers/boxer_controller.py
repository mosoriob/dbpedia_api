import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BOXER_TYPE_NAME, BOXER_TYPE_URI

from openapi_server.models.boxer import Boxer  # noqa: E501
from openapi_server import util

def boxers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Boxer

    Gets a list of all instances of Boxer (more information in http://dbpedia.org/ontology/Boxer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Boxer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BOXER_TYPE_URI,
        rdf_type_name=BOXER_TYPE_NAME, 
        kls=Boxer)

def boxers_id_get(id):  # noqa: E501
    """Get a single Boxer by its id

    Gets the details of a given Boxer (more information in http://dbpedia.org/ontology/Boxer) # noqa: E501

    :param id: The ID of the Boxer to be retrieved
    :type id: str

    :rtype: Boxer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BOXER_TYPE_URI,
        rdf_type_name=BOXER_TYPE_NAME, 
        kls=Boxer)
