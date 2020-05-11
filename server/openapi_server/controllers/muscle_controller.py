import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MUSCLE_TYPE_NAME, MUSCLE_TYPE_URI

from openapi_server.models.muscle import Muscle  # noqa: E501
from openapi_server import util

def muscles_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Muscle

    Gets a list of all instances of Muscle (more information in http://dbpedia.org/ontology/Muscle) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Muscle]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MUSCLE_TYPE_URI,
        rdf_type_name=MUSCLE_TYPE_NAME, 
        kls=Muscle)

def muscles_id_get(id):  # noqa: E501
    """Get a single Muscle by its id

    Gets the details of a given Muscle (more information in http://dbpedia.org/ontology/Muscle) # noqa: E501

    :param id: The ID of the Muscle to be retrieved
    :type id: str

    :rtype: Muscle
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MUSCLE_TYPE_URI,
        rdf_type_name=MUSCLE_TYPE_NAME, 
        kls=Muscle)
