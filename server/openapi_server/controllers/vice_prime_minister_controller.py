import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VICEPRIMEMINISTER_TYPE_NAME, VICEPRIMEMINISTER_TYPE_URI

from openapi_server.models.vice_prime_minister import VicePrimeMinister  # noqa: E501
from openapi_server import util

def viceprimeministers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of VicePrimeMinister

    Gets a list of all instances of VicePrimeMinister (more information in http://dbpedia.org/ontology/VicePrimeMinister) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[VicePrimeMinister]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VICEPRIMEMINISTER_TYPE_URI,
        rdf_type_name=VICEPRIMEMINISTER_TYPE_NAME, 
        kls=VicePrimeMinister)

def viceprimeministers_id_get(id):  # noqa: E501
    """Get a single VicePrimeMinister by its id

    Gets the details of a given VicePrimeMinister (more information in http://dbpedia.org/ontology/VicePrimeMinister) # noqa: E501

    :param id: The ID of the VicePrimeMinister to be retrieved
    :type id: str

    :rtype: VicePrimeMinister
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VICEPRIMEMINISTER_TYPE_URI,
        rdf_type_name=VICEPRIMEMINISTER_TYPE_NAME, 
        kls=VicePrimeMinister)
