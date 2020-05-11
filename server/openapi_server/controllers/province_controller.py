import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PROVINCE_TYPE_NAME, PROVINCE_TYPE_URI

from openapi_server.models.province import Province  # noqa: E501
from openapi_server import util

def provinces_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Province

    Gets a list of all instances of Province (more information in http://dbpedia.org/ontology/Province) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Province]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PROVINCE_TYPE_URI,
        rdf_type_name=PROVINCE_TYPE_NAME, 
        kls=Province)

def provinces_id_get(id):  # noqa: E501
    """Get a single Province by its id

    Gets the details of a given Province (more information in http://dbpedia.org/ontology/Province) # noqa: E501

    :param id: The ID of the Province to be retrieved
    :type id: str

    :rtype: Province
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PROVINCE_TYPE_URI,
        rdf_type_name=PROVINCE_TYPE_NAME, 
        kls=Province)
