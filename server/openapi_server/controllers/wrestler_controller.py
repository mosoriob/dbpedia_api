import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import WRESTLER_TYPE_NAME, WRESTLER_TYPE_URI

from openapi_server.models.wrestler import Wrestler  # noqa: E501
from openapi_server import util

def wrestlers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Wrestler

    Gets a list of all instances of Wrestler (more information in http://dbpedia.org/ontology/Wrestler) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Wrestler]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=WRESTLER_TYPE_URI,
        rdf_type_name=WRESTLER_TYPE_NAME, 
        kls=Wrestler)

def wrestlers_id_get(id):  # noqa: E501
    """Get a single Wrestler by its id

    Gets the details of a given Wrestler (more information in http://dbpedia.org/ontology/Wrestler) # noqa: E501

    :param id: The ID of the Wrestler to be retrieved
    :type id: str

    :rtype: Wrestler
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=WRESTLER_TYPE_URI,
        rdf_type_name=WRESTLER_TYPE_NAME, 
        kls=Wrestler)
