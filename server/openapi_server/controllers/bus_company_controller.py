import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BUSCOMPANY_TYPE_NAME, BUSCOMPANY_TYPE_URI

from openapi_server.models.bus_company import BusCompany  # noqa: E501
from openapi_server import util

def buscompanys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BusCompany

    Gets a list of all instances of BusCompany (more information in http://dbpedia.org/ontology/BusCompany) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BusCompany]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BUSCOMPANY_TYPE_URI,
        rdf_type_name=BUSCOMPANY_TYPE_NAME, 
        kls=BusCompany)

def buscompanys_id_get(id):  # noqa: E501
    """Get a single BusCompany by its id

    Gets the details of a given BusCompany (more information in http://dbpedia.org/ontology/BusCompany) # noqa: E501

    :param id: The ID of the BusCompany to be retrieved
    :type id: str

    :rtype: BusCompany
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BUSCOMPANY_TYPE_URI,
        rdf_type_name=BUSCOMPANY_TYPE_NAME, 
        kls=BusCompany)
