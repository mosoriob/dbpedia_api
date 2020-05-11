import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import GRANDPRIX_TYPE_NAME, GRANDPRIX_TYPE_URI

from openapi_server.models.grand_prix import GrandPrix  # noqa: E501
from openapi_server import util

def grandprixs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of GrandPrix

    Gets a list of all instances of GrandPrix (more information in http://dbpedia.org/ontology/GrandPrix) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[GrandPrix]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=GRANDPRIX_TYPE_URI,
        rdf_type_name=GRANDPRIX_TYPE_NAME, 
        kls=GrandPrix)

def grandprixs_id_get(id):  # noqa: E501
    """Get a single GrandPrix by its id

    Gets the details of a given GrandPrix (more information in http://dbpedia.org/ontology/GrandPrix) # noqa: E501

    :param id: The ID of the GrandPrix to be retrieved
    :type id: str

    :rtype: GrandPrix
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=GRANDPRIX_TYPE_URI,
        rdf_type_name=GRANDPRIX_TYPE_NAME, 
        kls=GrandPrix)
