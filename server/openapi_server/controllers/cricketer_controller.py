import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CRICKETER_TYPE_NAME, CRICKETER_TYPE_URI

from openapi_server.models.cricketer import Cricketer  # noqa: E501
from openapi_server import util

def cricketers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Cricketer

    Gets a list of all instances of Cricketer (more information in http://dbpedia.org/ontology/Cricketer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Cricketer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CRICKETER_TYPE_URI,
        rdf_type_name=CRICKETER_TYPE_NAME, 
        kls=Cricketer)

def cricketers_id_get(id):  # noqa: E501
    """Get a single Cricketer by its id

    Gets the details of a given Cricketer (more information in http://dbpedia.org/ontology/Cricketer) # noqa: E501

    :param id: The ID of the Cricketer to be retrieved
    :type id: str

    :rtype: Cricketer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CRICKETER_TYPE_URI,
        rdf_type_name=CRICKETER_TYPE_NAME, 
        kls=Cricketer)
