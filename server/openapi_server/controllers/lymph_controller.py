import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LYMPH_TYPE_NAME, LYMPH_TYPE_URI

from openapi_server.models.lymph import Lymph  # noqa: E501
from openapi_server import util

def lymphs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Lymph

    Gets a list of all instances of Lymph (more information in http://dbpedia.org/ontology/Lymph) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Lymph]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LYMPH_TYPE_URI,
        rdf_type_name=LYMPH_TYPE_NAME, 
        kls=Lymph)

def lymphs_id_get(id):  # noqa: E501
    """Get a single Lymph by its id

    Gets the details of a given Lymph (more information in http://dbpedia.org/ontology/Lymph) # noqa: E501

    :param id: The ID of the Lymph to be retrieved
    :type id: str

    :rtype: Lymph
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LYMPH_TYPE_URI,
        rdf_type_name=LYMPH_TYPE_NAME, 
        kls=Lymph)
