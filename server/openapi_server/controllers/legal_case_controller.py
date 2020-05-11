import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LEGALCASE_TYPE_NAME, LEGALCASE_TYPE_URI

from openapi_server.models.legal_case import LegalCase  # noqa: E501
from openapi_server import util

def legalcases_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of LegalCase

    Gets a list of all instances of LegalCase (more information in http://dbpedia.org/ontology/LegalCase) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[LegalCase]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LEGALCASE_TYPE_URI,
        rdf_type_name=LEGALCASE_TYPE_NAME, 
        kls=LegalCase)

def legalcases_id_get(id):  # noqa: E501
    """Get a single LegalCase by its id

    Gets the details of a given LegalCase (more information in http://dbpedia.org/ontology/LegalCase) # noqa: E501

    :param id: The ID of the LegalCase to be retrieved
    :type id: str

    :rtype: LegalCase
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LEGALCASE_TYPE_URI,
        rdf_type_name=LEGALCASE_TYPE_NAME, 
        kls=LegalCase)
