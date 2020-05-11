import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HUMANGENELOCATION_TYPE_NAME, HUMANGENELOCATION_TYPE_URI

from openapi_server.models.human_gene_location import HumanGeneLocation  # noqa: E501
from openapi_server import util

def humangenelocations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HumanGeneLocation

    Gets a list of all instances of HumanGeneLocation (more information in http://dbpedia.org/ontology/HumanGeneLocation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HumanGeneLocation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HUMANGENELOCATION_TYPE_URI,
        rdf_type_name=HUMANGENELOCATION_TYPE_NAME, 
        kls=HumanGeneLocation)

def humangenelocations_id_get(id):  # noqa: E501
    """Get a single HumanGeneLocation by its id

    Gets the details of a given HumanGeneLocation (more information in http://dbpedia.org/ontology/HumanGeneLocation) # noqa: E501

    :param id: The ID of the HumanGeneLocation to be retrieved
    :type id: str

    :rtype: HumanGeneLocation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HUMANGENELOCATION_TYPE_URI,
        rdf_type_name=HUMANGENELOCATION_TYPE_NAME, 
        kls=HumanGeneLocation)
