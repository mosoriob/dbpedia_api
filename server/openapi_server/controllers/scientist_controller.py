import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SCIENTIST_TYPE_NAME, SCIENTIST_TYPE_URI

from openapi_server.models.scientist import Scientist  # noqa: E501
from openapi_server import util

def scientists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Scientist

    Gets a list of all instances of Scientist (more information in http://dbpedia.org/ontology/Scientist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Scientist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SCIENTIST_TYPE_URI,
        rdf_type_name=SCIENTIST_TYPE_NAME, 
        kls=Scientist)

def scientists_id_get(id):  # noqa: E501
    """Get a single Scientist by its id

    Gets the details of a given Scientist (more information in http://dbpedia.org/ontology/Scientist) # noqa: E501

    :param id: The ID of the Scientist to be retrieved
    :type id: str

    :rtype: Scientist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SCIENTIST_TYPE_URI,
        rdf_type_name=SCIENTIST_TYPE_NAME, 
        kls=Scientist)
