import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BLAZON_TYPE_NAME, BLAZON_TYPE_URI

from openapi_server.models.blazon import Blazon  # noqa: E501
from openapi_server import util

def blazons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Blazon

    Gets a list of all instances of Blazon (more information in http://dbpedia.org/ontology/Blazon) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Blazon]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BLAZON_TYPE_URI,
        rdf_type_name=BLAZON_TYPE_NAME, 
        kls=Blazon)

def blazons_id_get(id):  # noqa: E501
    """Get a single Blazon by its id

    Gets the details of a given Blazon (more information in http://dbpedia.org/ontology/Blazon) # noqa: E501

    :param id: The ID of the Blazon to be retrieved
    :type id: str

    :rtype: Blazon
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BLAZON_TYPE_URI,
        rdf_type_name=BLAZON_TYPE_NAME, 
        kls=Blazon)
