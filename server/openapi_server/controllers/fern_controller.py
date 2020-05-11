import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FERN_TYPE_NAME, FERN_TYPE_URI

from openapi_server.models.fern import Fern  # noqa: E501
from openapi_server import util

def ferns_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Fern

    Gets a list of all instances of Fern (more information in http://dbpedia.org/ontology/Fern) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Fern]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FERN_TYPE_URI,
        rdf_type_name=FERN_TYPE_NAME, 
        kls=Fern)

def ferns_id_get(id):  # noqa: E501
    """Get a single Fern by its id

    Gets the details of a given Fern (more information in http://dbpedia.org/ontology/Fern) # noqa: E501

    :param id: The ID of the Fern to be retrieved
    :type id: str

    :rtype: Fern
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FERN_TYPE_URI,
        rdf_type_name=FERN_TYPE_NAME, 
        kls=Fern)
