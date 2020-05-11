import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CONIFER_TYPE_NAME, CONIFER_TYPE_URI

from openapi_server.models.conifer import Conifer  # noqa: E501
from openapi_server import util

def conifers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Conifer

    Gets a list of all instances of Conifer (more information in http://dbpedia.org/ontology/Conifer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Conifer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CONIFER_TYPE_URI,
        rdf_type_name=CONIFER_TYPE_NAME, 
        kls=Conifer)

def conifers_id_get(id):  # noqa: E501
    """Get a single Conifer by its id

    Gets the details of a given Conifer (more information in http://dbpedia.org/ontology/Conifer) # noqa: E501

    :param id: The ID of the Conifer to be retrieved
    :type id: str

    :rtype: Conifer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CONIFER_TYPE_URI,
        rdf_type_name=CONIFER_TYPE_NAME, 
        kls=Conifer)
