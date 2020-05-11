import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MUNICIPALITY_TYPE_NAME, MUNICIPALITY_TYPE_URI

from openapi_server.models.municipality import Municipality  # noqa: E501
from openapi_server import util

def municipalitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Municipality

    Gets a list of all instances of Municipality (more information in http://dbpedia.org/ontology/Municipality) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Municipality]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MUNICIPALITY_TYPE_URI,
        rdf_type_name=MUNICIPALITY_TYPE_NAME, 
        kls=Municipality)

def municipalitys_id_get(id):  # noqa: E501
    """Get a single Municipality by its id

    Gets the details of a given Municipality (more information in http://dbpedia.org/ontology/Municipality) # noqa: E501

    :param id: The ID of the Municipality to be retrieved
    :type id: str

    :rtype: Municipality
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MUNICIPALITY_TYPE_URI,
        rdf_type_name=MUNICIPALITY_TYPE_NAME, 
        kls=Municipality)
