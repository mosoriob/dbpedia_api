import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COMPANY_TYPE_NAME, COMPANY_TYPE_URI

from openapi_server.models.company import Company  # noqa: E501
from openapi_server import util

def companys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Company

    Gets a list of all instances of Company (more information in http://dbpedia.org/ontology/Company) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Company]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COMPANY_TYPE_URI,
        rdf_type_name=COMPANY_TYPE_NAME, 
        kls=Company)

def companys_id_get(id):  # noqa: E501
    """Get a single Company by its id

    Gets the details of a given Company (more information in http://dbpedia.org/ontology/Company) # noqa: E501

    :param id: The ID of the Company to be retrieved
    :type id: str

    :rtype: Company
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COMPANY_TYPE_URI,
        rdf_type_name=COMPANY_TYPE_NAME, 
        kls=Company)
