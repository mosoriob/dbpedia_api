import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LINGUIST_TYPE_NAME, LINGUIST_TYPE_URI

from openapi_server.models.linguist import Linguist  # noqa: E501
from openapi_server import util

def linguists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Linguist

    Gets a list of all instances of Linguist (more information in http://dbpedia.org/ontology/Linguist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Linguist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LINGUIST_TYPE_URI,
        rdf_type_name=LINGUIST_TYPE_NAME, 
        kls=Linguist)

def linguists_id_get(id):  # noqa: E501
    """Get a single Linguist by its id

    Gets the details of a given Linguist (more information in http://dbpedia.org/ontology/Linguist) # noqa: E501

    :param id: The ID of the Linguist to be retrieved
    :type id: str

    :rtype: Linguist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LINGUIST_TYPE_URI,
        rdf_type_name=LINGUIST_TYPE_NAME, 
        kls=Linguist)
