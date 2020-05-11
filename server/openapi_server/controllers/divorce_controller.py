import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DIVORCE_TYPE_NAME, DIVORCE_TYPE_URI

from openapi_server.models.divorce import Divorce  # noqa: E501
from openapi_server import util

def divorces_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Divorce

    Gets a list of all instances of Divorce (more information in http://dbpedia.org/ontology/Divorce) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Divorce]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DIVORCE_TYPE_URI,
        rdf_type_name=DIVORCE_TYPE_NAME, 
        kls=Divorce)

def divorces_id_get(id):  # noqa: E501
    """Get a single Divorce by its id

    Gets the details of a given Divorce (more information in http://dbpedia.org/ontology/Divorce) # noqa: E501

    :param id: The ID of the Divorce to be retrieved
    :type id: str

    :rtype: Divorce
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DIVORCE_TYPE_URI,
        rdf_type_name=DIVORCE_TYPE_NAME, 
        kls=Divorce)
