import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BUSINESSPERSON_TYPE_NAME, BUSINESSPERSON_TYPE_URI

from openapi_server.models.business_person import BusinessPerson  # noqa: E501
from openapi_server import util

def businesspersons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BusinessPerson

    Gets a list of all instances of BusinessPerson (more information in http://dbpedia.org/ontology/BusinessPerson) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BusinessPerson]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BUSINESSPERSON_TYPE_URI,
        rdf_type_name=BUSINESSPERSON_TYPE_NAME, 
        kls=BusinessPerson)

def businesspersons_id_get(id):  # noqa: E501
    """Get a single BusinessPerson by its id

    Gets the details of a given BusinessPerson (more information in http://dbpedia.org/ontology/BusinessPerson) # noqa: E501

    :param id: The ID of the BusinessPerson to be retrieved
    :type id: str

    :rtype: BusinessPerson
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BUSINESSPERSON_TYPE_URI,
        rdf_type_name=BUSINESSPERSON_TYPE_NAME, 
        kls=BusinessPerson)
