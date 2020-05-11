import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARACHNID_TYPE_NAME, ARACHNID_TYPE_URI

from openapi_server.models.arachnid import Arachnid  # noqa: E501
from openapi_server import util

def arachnids_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Arachnid

    Gets a list of all instances of Arachnid (more information in http://dbpedia.org/ontology/Arachnid) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Arachnid]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARACHNID_TYPE_URI,
        rdf_type_name=ARACHNID_TYPE_NAME, 
        kls=Arachnid)

def arachnids_id_get(id):  # noqa: E501
    """Get a single Arachnid by its id

    Gets the details of a given Arachnid (more information in http://dbpedia.org/ontology/Arachnid) # noqa: E501

    :param id: The ID of the Arachnid to be retrieved
    :type id: str

    :rtype: Arachnid
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARACHNID_TYPE_URI,
        rdf_type_name=ARACHNID_TYPE_NAME, 
        kls=Arachnid)
