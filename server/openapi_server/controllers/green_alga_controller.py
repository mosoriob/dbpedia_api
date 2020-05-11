import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GREENALGA_TYPE_NAME, GREENALGA_TYPE_URI

from openapi_server.models.green_alga import GreenAlga  # noqa: E501
from openapi_server import util

def greenalgas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GreenAlga

    Gets a list of all instances of GreenAlga (more information in http://dbpedia.org/ontology/GreenAlga) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GreenAlga]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GREENALGA_TYPE_URI,
        rdf_type_name=GREENALGA_TYPE_NAME, 
        kls=GreenAlga)

def greenalgas_id_get(id):  # noqa: E501
    """Get a single GreenAlga by its id

    Gets the details of a given GreenAlga (more information in http://dbpedia.org/ontology/GreenAlga) # noqa: E501

    :param id: The ID of the GreenAlga to be retrieved
    :type id: str

    :rtype: GreenAlga
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GREENALGA_TYPE_URI,
        rdf_type_name=GREENALGA_TYPE_NAME, 
        kls=GreenAlga)
