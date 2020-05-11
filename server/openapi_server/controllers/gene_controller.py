import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GENE_TYPE_NAME, GENE_TYPE_URI

from openapi_server.models.gene import Gene  # noqa: E501
from openapi_server import util

def genes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Gene

    Gets a list of all instances of Gene (more information in http://dbpedia.org/ontology/Gene) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Gene]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GENE_TYPE_URI,
        rdf_type_name=GENE_TYPE_NAME, 
        kls=Gene)

def genes_id_get(id):  # noqa: E501
    """Get a single Gene by its id

    Gets the details of a given Gene (more information in http://dbpedia.org/ontology/Gene) # noqa: E501

    :param id: The ID of the Gene to be retrieved
    :type id: str

    :rtype: Gene
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GENE_TYPE_URI,
        rdf_type_name=GENE_TYPE_NAME, 
        kls=Gene)
