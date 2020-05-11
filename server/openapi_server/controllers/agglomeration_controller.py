import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AGGLOMERATION_TYPE_NAME, AGGLOMERATION_TYPE_URI

from openapi_server.models.agglomeration import Agglomeration  # noqa: E501
from openapi_server import util

def agglomerations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Agglomeration

    Gets a list of all instances of Agglomeration (more information in http://dbpedia.org/ontology/Agglomeration) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Agglomeration]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AGGLOMERATION_TYPE_URI,
        rdf_type_name=AGGLOMERATION_TYPE_NAME, 
        kls=Agglomeration)

def agglomerations_id_get(id):  # noqa: E501
    """Get a single Agglomeration by its id

    Gets the details of a given Agglomeration (more information in http://dbpedia.org/ontology/Agglomeration) # noqa: E501

    :param id: The ID of the Agglomeration to be retrieved
    :type id: str

    :rtype: Agglomeration
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AGGLOMERATION_TYPE_URI,
        rdf_type_name=AGGLOMERATION_TYPE_NAME, 
        kls=Agglomeration)
