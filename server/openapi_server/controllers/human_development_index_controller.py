import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HUMANDEVELOPMENTINDEX_TYPE_NAME, HUMANDEVELOPMENTINDEX_TYPE_URI

from openapi_server.models.human_development_index import HumanDevelopmentIndex  # noqa: E501
from openapi_server import util

def humandevelopmentindexs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HumanDevelopmentIndex

    Gets a list of all instances of HumanDevelopmentIndex (more information in http://dbpedia.org/ontology/HumanDevelopmentIndex) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HumanDevelopmentIndex]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HUMANDEVELOPMENTINDEX_TYPE_URI,
        rdf_type_name=HUMANDEVELOPMENTINDEX_TYPE_NAME, 
        kls=HumanDevelopmentIndex)

def humandevelopmentindexs_id_get(id):  # noqa: E501
    """Get a single HumanDevelopmentIndex by its id

    Gets the details of a given HumanDevelopmentIndex (more information in http://dbpedia.org/ontology/HumanDevelopmentIndex) # noqa: E501

    :param id: The ID of the HumanDevelopmentIndex to be retrieved
    :type id: str

    :rtype: HumanDevelopmentIndex
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HUMANDEVELOPMENTINDEX_TYPE_URI,
        rdf_type_name=HUMANDEVELOPMENTINDEX_TYPE_NAME, 
        kls=HumanDevelopmentIndex)
