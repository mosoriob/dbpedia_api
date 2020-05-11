import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CRUSTACEAN_TYPE_NAME, CRUSTACEAN_TYPE_URI

from openapi_server.models.crustacean import Crustacean  # noqa: E501
from openapi_server import util

def crustaceans_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Crustacean

    Gets a list of all instances of Crustacean (more information in http://dbpedia.org/ontology/Crustacean) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Crustacean]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CRUSTACEAN_TYPE_URI,
        rdf_type_name=CRUSTACEAN_TYPE_NAME, 
        kls=Crustacean)

def crustaceans_id_get(id):  # noqa: E501
    """Get a single Crustacean by its id

    Gets the details of a given Crustacean (more information in http://dbpedia.org/ontology/Crustacean) # noqa: E501

    :param id: The ID of the Crustacean to be retrieved
    :type id: str

    :rtype: Crustacean
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CRUSTACEAN_TYPE_URI,
        rdf_type_name=CRUSTACEAN_TYPE_NAME, 
        kls=Crustacean)
