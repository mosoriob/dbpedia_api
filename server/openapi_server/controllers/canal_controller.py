import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CANAL_TYPE_NAME, CANAL_TYPE_URI

from openapi_server.models.canal import Canal  # noqa: E501
from openapi_server import util

def canals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Canal

    Gets a list of all instances of Canal (more information in http://dbpedia.org/ontology/Canal) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Canal]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CANAL_TYPE_URI,
        rdf_type_name=CANAL_TYPE_NAME, 
        kls=Canal)

def canals_id_get(id):  # noqa: E501
    """Get a single Canal by its id

    Gets the details of a given Canal (more information in http://dbpedia.org/ontology/Canal) # noqa: E501

    :param id: The ID of the Canal to be retrieved
    :type id: str

    :rtype: Canal
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CANAL_TYPE_URI,
        rdf_type_name=CANAL_TYPE_NAME, 
        kls=Canal)
