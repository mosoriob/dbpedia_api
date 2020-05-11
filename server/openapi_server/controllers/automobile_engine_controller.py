import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AUTOMOBILEENGINE_TYPE_NAME, AUTOMOBILEENGINE_TYPE_URI

from openapi_server.models.automobile_engine import AutomobileEngine  # noqa: E501
from openapi_server import util

def automobileengines_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AutomobileEngine

    Gets a list of all instances of AutomobileEngine (more information in http://dbpedia.org/ontology/AutomobileEngine) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AutomobileEngine]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AUTOMOBILEENGINE_TYPE_URI,
        rdf_type_name=AUTOMOBILEENGINE_TYPE_NAME, 
        kls=AutomobileEngine)

def automobileengines_id_get(id):  # noqa: E501
    """Get a single AutomobileEngine by its id

    Gets the details of a given AutomobileEngine (more information in http://dbpedia.org/ontology/AutomobileEngine) # noqa: E501

    :param id: The ID of the AutomobileEngine to be retrieved
    :type id: str

    :rtype: AutomobileEngine
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AUTOMOBILEENGINE_TYPE_URI,
        rdf_type_name=AUTOMOBILEENGINE_TYPE_NAME, 
        kls=AutomobileEngine)
