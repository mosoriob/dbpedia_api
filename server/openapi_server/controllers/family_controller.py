import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FAMILY_TYPE_NAME, FAMILY_TYPE_URI

from openapi_server.models.family import Family  # noqa: E501
from openapi_server import util

def familys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Family

    Gets a list of all instances of Family (more information in http://dbpedia.org/ontology/Family) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Family]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FAMILY_TYPE_URI,
        rdf_type_name=FAMILY_TYPE_NAME, 
        kls=Family)

def familys_id_get(id):  # noqa: E501
    """Get a single Family by its id

    Gets the details of a given Family (more information in http://dbpedia.org/ontology/Family) # noqa: E501

    :param id: The ID of the Family to be retrieved
    :type id: str

    :rtype: Family
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FAMILY_TYPE_URI,
        rdf_type_name=FAMILY_TYPE_NAME, 
        kls=Family)
