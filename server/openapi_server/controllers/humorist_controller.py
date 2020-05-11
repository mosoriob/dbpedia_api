import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HUMORIST_TYPE_NAME, HUMORIST_TYPE_URI

from openapi_server.models.humorist import Humorist  # noqa: E501
from openapi_server import util

def humorists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Humorist

    Gets a list of all instances of Humorist (more information in http://dbpedia.org/ontology/Humorist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Humorist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HUMORIST_TYPE_URI,
        rdf_type_name=HUMORIST_TYPE_NAME, 
        kls=Humorist)

def humorists_id_get(id):  # noqa: E501
    """Get a single Humorist by its id

    Gets the details of a given Humorist (more information in http://dbpedia.org/ontology/Humorist) # noqa: E501

    :param id: The ID of the Humorist to be retrieved
    :type id: str

    :rtype: Humorist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HUMORIST_TYPE_URI,
        rdf_type_name=HUMORIST_TYPE_NAME, 
        kls=Humorist)
