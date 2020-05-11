import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LIGHTHOUSE_TYPE_NAME, LIGHTHOUSE_TYPE_URI

from openapi_server.models.lighthouse import Lighthouse  # noqa: E501
from openapi_server import util

def lighthouses_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Lighthouse

    Gets a list of all instances of Lighthouse (more information in http://dbpedia.org/ontology/Lighthouse) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Lighthouse]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LIGHTHOUSE_TYPE_URI,
        rdf_type_name=LIGHTHOUSE_TYPE_NAME, 
        kls=Lighthouse)

def lighthouses_id_get(id):  # noqa: E501
    """Get a single Lighthouse by its id

    Gets the details of a given Lighthouse (more information in http://dbpedia.org/ontology/Lighthouse) # noqa: E501

    :param id: The ID of the Lighthouse to be retrieved
    :type id: str

    :rtype: Lighthouse
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LIGHTHOUSE_TYPE_URI,
        rdf_type_name=LIGHTHOUSE_TYPE_NAME, 
        kls=Lighthouse)
