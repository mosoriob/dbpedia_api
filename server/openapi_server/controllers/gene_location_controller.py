import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GENELOCATION_TYPE_NAME, GENELOCATION_TYPE_URI

from openapi_server.models.gene_location import GeneLocation  # noqa: E501
from openapi_server import util

def genelocations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GeneLocation

    Gets a list of all instances of GeneLocation (more information in http://dbpedia.org/ontology/GeneLocation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GeneLocation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GENELOCATION_TYPE_URI,
        rdf_type_name=GENELOCATION_TYPE_NAME, 
        kls=GeneLocation)

def genelocations_id_get(id):  # noqa: E501
    """Get a single GeneLocation by its id

    Gets the details of a given GeneLocation (more information in http://dbpedia.org/ontology/GeneLocation) # noqa: E501

    :param id: The ID of the GeneLocation to be retrieved
    :type id: str

    :rtype: GeneLocation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GENELOCATION_TYPE_URI,
        rdf_type_name=GENELOCATION_TYPE_NAME, 
        kls=GeneLocation)
