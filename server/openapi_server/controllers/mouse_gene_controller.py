import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOUSEGENE_TYPE_NAME, MOUSEGENE_TYPE_URI

from openapi_server.models.mouse_gene import MouseGene  # noqa: E501
from openapi_server import util

def mousegenes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MouseGene

    Gets a list of all instances of MouseGene (more information in http://dbpedia.org/ontology/MouseGene) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MouseGene]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOUSEGENE_TYPE_URI,
        rdf_type_name=MOUSEGENE_TYPE_NAME, 
        kls=MouseGene)

def mousegenes_id_get(id):  # noqa: E501
    """Get a single MouseGene by its id

    Gets the details of a given MouseGene (more information in http://dbpedia.org/ontology/MouseGene) # noqa: E501

    :param id: The ID of the MouseGene to be retrieved
    :type id: str

    :rtype: MouseGene
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOUSEGENE_TYPE_URI,
        rdf_type_name=MOUSEGENE_TYPE_NAME, 
        kls=MouseGene)
