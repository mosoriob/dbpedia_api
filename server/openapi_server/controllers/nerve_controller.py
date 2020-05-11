import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NERVE_TYPE_NAME, NERVE_TYPE_URI

from openapi_server.models.nerve import Nerve  # noqa: E501
from openapi_server import util

def nerves_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Nerve

    Gets a list of all instances of Nerve (more information in http://dbpedia.org/ontology/Nerve) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Nerve]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NERVE_TYPE_URI,
        rdf_type_name=NERVE_TYPE_NAME, 
        kls=Nerve)

def nerves_id_get(id):  # noqa: E501
    """Get a single Nerve by its id

    Gets the details of a given Nerve (more information in http://dbpedia.org/ontology/Nerve) # noqa: E501

    :param id: The ID of the Nerve to be retrieved
    :type id: str

    :rtype: Nerve
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NERVE_TYPE_URI,
        rdf_type_name=NERVE_TYPE_NAME, 
        kls=Nerve)
