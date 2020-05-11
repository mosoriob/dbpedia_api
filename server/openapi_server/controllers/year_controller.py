import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import YEAR_TYPE_NAME, YEAR_TYPE_URI

from openapi_server.models.year import Year  # noqa: E501
from openapi_server import util

def years_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Year

    Gets a list of all instances of Year (more information in http://dbpedia.org/ontology/Year) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Year]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=YEAR_TYPE_URI,
        rdf_type_name=YEAR_TYPE_NAME, 
        kls=Year)

def years_id_get(id):  # noqa: E501
    """Get a single Year by its id

    Gets the details of a given Year (more information in http://dbpedia.org/ontology/Year) # noqa: E501

    :param id: The ID of the Year to be retrieved
    :type id: str

    :rtype: Year
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=YEAR_TYPE_URI,
        rdf_type_name=YEAR_TYPE_NAME, 
        kls=Year)
