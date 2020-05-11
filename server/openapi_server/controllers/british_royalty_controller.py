import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BRITISHROYALTY_TYPE_NAME, BRITISHROYALTY_TYPE_URI

from openapi_server.models.british_royalty import BritishRoyalty  # noqa: E501
from openapi_server import util

def britishroyaltys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BritishRoyalty

    Gets a list of all instances of BritishRoyalty (more information in http://dbpedia.org/ontology/BritishRoyalty) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BritishRoyalty]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BRITISHROYALTY_TYPE_URI,
        rdf_type_name=BRITISHROYALTY_TYPE_NAME, 
        kls=BritishRoyalty)

def britishroyaltys_id_get(id):  # noqa: E501
    """Get a single BritishRoyalty by its id

    Gets the details of a given BritishRoyalty (more information in http://dbpedia.org/ontology/BritishRoyalty) # noqa: E501

    :param id: The ID of the BritishRoyalty to be retrieved
    :type id: str

    :rtype: BritishRoyalty
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BRITISHROYALTY_TYPE_URI,
        rdf_type_name=BRITISHROYALTY_TYPE_NAME, 
        kls=BritishRoyalty)
