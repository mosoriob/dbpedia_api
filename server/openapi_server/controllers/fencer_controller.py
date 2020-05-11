import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FENCER_TYPE_NAME, FENCER_TYPE_URI

from openapi_server.models.fencer import Fencer  # noqa: E501
from openapi_server import util

def fencers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Fencer

    Gets a list of all instances of Fencer (more information in http://dbpedia.org/ontology/Fencer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Fencer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FENCER_TYPE_URI,
        rdf_type_name=FENCER_TYPE_NAME, 
        kls=Fencer)

def fencers_id_get(id):  # noqa: E501
    """Get a single Fencer by its id

    Gets the details of a given Fencer (more information in http://dbpedia.org/ontology/Fencer) # noqa: E501

    :param id: The ID of the Fencer to be retrieved
    :type id: str

    :rtype: Fencer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FENCER_TYPE_URI,
        rdf_type_name=FENCER_TYPE_NAME, 
        kls=Fencer)
