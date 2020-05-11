import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WEBSITE_TYPE_NAME, WEBSITE_TYPE_URI

from openapi_server.models.website import Website  # noqa: E501
from openapi_server import util

def websites_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Website

    Gets a list of all instances of Website (more information in http://dbpedia.org/ontology/Website) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Website]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WEBSITE_TYPE_URI,
        rdf_type_name=WEBSITE_TYPE_NAME, 
        kls=Website)

def websites_id_get(id):  # noqa: E501
    """Get a single Website by its id

    Gets the details of a given Website (more information in http://dbpedia.org/ontology/Website) # noqa: E501

    :param id: The ID of the Website to be retrieved
    :type id: str

    :rtype: Website
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WEBSITE_TYPE_URI,
        rdf_type_name=WEBSITE_TYPE_NAME, 
        kls=Website)
