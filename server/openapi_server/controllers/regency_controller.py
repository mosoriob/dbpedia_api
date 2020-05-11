import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import REGENCY_TYPE_NAME, REGENCY_TYPE_URI

from openapi_server.models.regency import Regency  # noqa: E501
from openapi_server import util

def regencys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Regency

    Gets a list of all instances of Regency (more information in http://dbpedia.org/ontology/Regency) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Regency]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=REGENCY_TYPE_URI,
        rdf_type_name=REGENCY_TYPE_NAME, 
        kls=Regency)

def regencys_id_get(id):  # noqa: E501
    """Get a single Regency by its id

    Gets the details of a given Regency (more information in http://dbpedia.org/ontology/Regency) # noqa: E501

    :param id: The ID of the Regency to be retrieved
    :type id: str

    :rtype: Regency
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=REGENCY_TYPE_URI,
        rdf_type_name=REGENCY_TYPE_NAME, 
        kls=Regency)
