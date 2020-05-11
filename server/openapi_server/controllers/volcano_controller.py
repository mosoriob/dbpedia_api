import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VOLCANO_TYPE_NAME, VOLCANO_TYPE_URI

from openapi_server.models.volcano import Volcano  # noqa: E501
from openapi_server import util

def volcanos_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Volcano

    Gets a list of all instances of Volcano (more information in http://dbpedia.org/ontology/Volcano) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Volcano]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VOLCANO_TYPE_URI,
        rdf_type_name=VOLCANO_TYPE_NAME, 
        kls=Volcano)

def volcanos_id_get(id):  # noqa: E501
    """Get a single Volcano by its id

    Gets the details of a given Volcano (more information in http://dbpedia.org/ontology/Volcano) # noqa: E501

    :param id: The ID of the Volcano to be retrieved
    :type id: str

    :rtype: Volcano
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VOLCANO_TYPE_URI,
        rdf_type_name=VOLCANO_TYPE_NAME, 
        kls=Volcano)
