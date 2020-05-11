import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOUSEGENELOCATION_TYPE_NAME, MOUSEGENELOCATION_TYPE_URI

from openapi_server.models.mouse_gene_location import MouseGeneLocation  # noqa: E501
from openapi_server import util

def mousegenelocations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MouseGeneLocation

    Gets a list of all instances of MouseGeneLocation (more information in http://dbpedia.org/ontology/MouseGeneLocation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MouseGeneLocation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOUSEGENELOCATION_TYPE_URI,
        rdf_type_name=MOUSEGENELOCATION_TYPE_NAME, 
        kls=MouseGeneLocation)

def mousegenelocations_id_get(id):  # noqa: E501
    """Get a single MouseGeneLocation by its id

    Gets the details of a given MouseGeneLocation (more information in http://dbpedia.org/ontology/MouseGeneLocation) # noqa: E501

    :param id: The ID of the MouseGeneLocation to be retrieved
    :type id: str

    :rtype: MouseGeneLocation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOUSEGENELOCATION_TYPE_URI,
        rdf_type_name=MOUSEGENELOCATION_TYPE_NAME, 
        kls=MouseGeneLocation)
