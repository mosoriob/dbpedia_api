import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import JOURNALIST_TYPE_NAME, JOURNALIST_TYPE_URI

from openapi_server.models.journalist import Journalist  # noqa: E501
from openapi_server import util

def journalists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Journalist

    Gets a list of all instances of Journalist (more information in http://dbpedia.org/ontology/Journalist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Journalist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=JOURNALIST_TYPE_URI,
        rdf_type_name=JOURNALIST_TYPE_NAME, 
        kls=Journalist)

def journalists_id_get(id):  # noqa: E501
    """Get a single Journalist by its id

    Gets the details of a given Journalist (more information in http://dbpedia.org/ontology/Journalist) # noqa: E501

    :param id: The ID of the Journalist to be retrieved
    :type id: str

    :rtype: Journalist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=JOURNALIST_TYPE_URI,
        rdf_type_name=JOURNALIST_TYPE_NAME, 
        kls=Journalist)
