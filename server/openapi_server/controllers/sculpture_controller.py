import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SCULPTURE_TYPE_NAME, SCULPTURE_TYPE_URI

from openapi_server.models.sculpture import Sculpture  # noqa: E501
from openapi_server import util

def sculptures_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Sculpture

    Gets a list of all instances of Sculpture (more information in http://dbpedia.org/ontology/Sculpture) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Sculpture]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SCULPTURE_TYPE_URI,
        rdf_type_name=SCULPTURE_TYPE_NAME, 
        kls=Sculpture)

def sculptures_id_get(id):  # noqa: E501
    """Get a single Sculpture by its id

    Gets the details of a given Sculpture (more information in http://dbpedia.org/ontology/Sculpture) # noqa: E501

    :param id: The ID of the Sculpture to be retrieved
    :type id: str

    :rtype: Sculpture
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SCULPTURE_TYPE_URI,
        rdf_type_name=SCULPTURE_TYPE_NAME, 
        kls=Sculpture)
