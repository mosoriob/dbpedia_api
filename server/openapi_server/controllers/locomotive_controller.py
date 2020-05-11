import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LOCOMOTIVE_TYPE_NAME, LOCOMOTIVE_TYPE_URI

from openapi_server.models.locomotive import Locomotive  # noqa: E501
from openapi_server import util

def locomotives_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Locomotive

    Gets a list of all instances of Locomotive (more information in http://dbpedia.org/ontology/Locomotive) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Locomotive]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LOCOMOTIVE_TYPE_URI,
        rdf_type_name=LOCOMOTIVE_TYPE_NAME, 
        kls=Locomotive)

def locomotives_id_get(id):  # noqa: E501
    """Get a single Locomotive by its id

    Gets the details of a given Locomotive (more information in http://dbpedia.org/ontology/Locomotive) # noqa: E501

    :param id: The ID of the Locomotive to be retrieved
    :type id: str

    :rtype: Locomotive
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LOCOMOTIVE_TYPE_URI,
        rdf_type_name=LOCOMOTIVE_TYPE_NAME, 
        kls=Locomotive)
