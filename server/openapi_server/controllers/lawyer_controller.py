import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LAWYER_TYPE_NAME, LAWYER_TYPE_URI

from openapi_server.models.lawyer import Lawyer  # noqa: E501
from openapi_server import util

def lawyers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Lawyer

    Gets a list of all instances of Lawyer (more information in http://dbpedia.org/ontology/Lawyer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Lawyer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LAWYER_TYPE_URI,
        rdf_type_name=LAWYER_TYPE_NAME, 
        kls=Lawyer)

def lawyers_id_get(id):  # noqa: E501
    """Get a single Lawyer by its id

    Gets the details of a given Lawyer (more information in http://dbpedia.org/ontology/Lawyer) # noqa: E501

    :param id: The ID of the Lawyer to be retrieved
    :type id: str

    :rtype: Lawyer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LAWYER_TYPE_URI,
        rdf_type_name=LAWYER_TYPE_NAME, 
        kls=Lawyer)
