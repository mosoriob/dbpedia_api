import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MONASTRY_TYPE_NAME, MONASTRY_TYPE_URI

from openapi_server.models.monastry import Monastry  # noqa: E501
from openapi_server import util

def monastrys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Monastry

    Gets a list of all instances of Monastry (more information in http://dbpedia.org/ontology/Monastry) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Monastry]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MONASTRY_TYPE_URI,
        rdf_type_name=MONASTRY_TYPE_NAME, 
        kls=Monastry)

def monastrys_id_get(id):  # noqa: E501
    """Get a single Monastry by its id

    Gets the details of a given Monastry (more information in http://dbpedia.org/ontology/Monastry) # noqa: E501

    :param id: The ID of the Monastry to be retrieved
    :type id: str

    :rtype: Monastry
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MONASTRY_TYPE_URI,
        rdf_type_name=MONASTRY_TYPE_NAME, 
        kls=Monastry)
