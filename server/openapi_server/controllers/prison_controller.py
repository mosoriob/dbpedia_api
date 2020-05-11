import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PRISON_TYPE_NAME, PRISON_TYPE_URI

from openapi_server.models.prison import Prison  # noqa: E501
from openapi_server import util

def prisons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Prison

    Gets a list of all instances of Prison (more information in http://dbpedia.org/ontology/Prison) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Prison]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PRISON_TYPE_URI,
        rdf_type_name=PRISON_TYPE_NAME, 
        kls=Prison)

def prisons_id_get(id):  # noqa: E501
    """Get a single Prison by its id

    Gets the details of a given Prison (more information in http://dbpedia.org/ontology/Prison) # noqa: E501

    :param id: The ID of the Prison to be retrieved
    :type id: str

    :rtype: Prison
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PRISON_TYPE_URI,
        rdf_type_name=PRISON_TYPE_NAME, 
        kls=Prison)
