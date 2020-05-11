import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HUMANGENE_TYPE_NAME, HUMANGENE_TYPE_URI

from openapi_server.models.human_gene import HumanGene  # noqa: E501
from openapi_server import util

def humangenes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HumanGene

    Gets a list of all instances of HumanGene (more information in http://dbpedia.org/ontology/HumanGene) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HumanGene]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HUMANGENE_TYPE_URI,
        rdf_type_name=HUMANGENE_TYPE_NAME, 
        kls=HumanGene)

def humangenes_id_get(id):  # noqa: E501
    """Get a single HumanGene by its id

    Gets the details of a given HumanGene (more information in http://dbpedia.org/ontology/HumanGene) # noqa: E501

    :param id: The ID of the HumanGene to be retrieved
    :type id: str

    :rtype: HumanGene
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HUMANGENE_TYPE_URI,
        rdf_type_name=HUMANGENE_TYPE_NAME, 
        kls=HumanGene)
