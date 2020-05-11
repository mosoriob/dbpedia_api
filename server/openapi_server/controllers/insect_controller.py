import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import INSECT_TYPE_NAME, INSECT_TYPE_URI

from openapi_server.models.insect import Insect  # noqa: E501
from openapi_server import util

def insects_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Insect

    Gets a list of all instances of Insect (more information in http://dbpedia.org/ontology/Insect) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Insect]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=INSECT_TYPE_URI,
        rdf_type_name=INSECT_TYPE_NAME, 
        kls=Insect)

def insects_id_get(id):  # noqa: E501
    """Get a single Insect by its id

    Gets the details of a given Insect (more information in http://dbpedia.org/ontology/Insect) # noqa: E501

    :param id: The ID of the Insect to be retrieved
    :type id: str

    :rtype: Insect
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=INSECT_TYPE_URI,
        rdf_type_name=INSECT_TYPE_NAME, 
        kls=Insect)
