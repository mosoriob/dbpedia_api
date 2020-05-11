import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ROYALTY_TYPE_NAME, ROYALTY_TYPE_URI

from openapi_server.models.royalty import Royalty  # noqa: E501
from openapi_server import util

def royaltys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Royalty

    Gets a list of all instances of Royalty (more information in http://dbpedia.org/ontology/Royalty) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Royalty]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ROYALTY_TYPE_URI,
        rdf_type_name=ROYALTY_TYPE_NAME, 
        kls=Royalty)

def royaltys_id_get(id):  # noqa: E501
    """Get a single Royalty by its id

    Gets the details of a given Royalty (more information in http://dbpedia.org/ontology/Royalty) # noqa: E501

    :param id: The ID of the Royalty to be retrieved
    :type id: str

    :rtype: Royalty
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ROYALTY_TYPE_URI,
        rdf_type_name=ROYALTY_TYPE_NAME, 
        kls=Royalty)
