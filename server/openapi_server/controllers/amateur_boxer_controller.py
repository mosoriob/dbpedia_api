import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AMATEURBOXER_TYPE_NAME, AMATEURBOXER_TYPE_URI

from openapi_server.models.amateur_boxer import AmateurBoxer  # noqa: E501
from openapi_server import util

def amateurboxers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AmateurBoxer

    Gets a list of all instances of AmateurBoxer (more information in http://dbpedia.org/ontology/AmateurBoxer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AmateurBoxer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AMATEURBOXER_TYPE_URI,
        rdf_type_name=AMATEURBOXER_TYPE_NAME, 
        kls=AmateurBoxer)

def amateurboxers_id_get(id):  # noqa: E501
    """Get a single AmateurBoxer by its id

    Gets the details of a given AmateurBoxer (more information in http://dbpedia.org/ontology/AmateurBoxer) # noqa: E501

    :param id: The ID of the AmateurBoxer to be retrieved
    :type id: str

    :rtype: AmateurBoxer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AMATEURBOXER_TYPE_URI,
        rdf_type_name=AMATEURBOXER_TYPE_NAME, 
        kls=AmateurBoxer)
