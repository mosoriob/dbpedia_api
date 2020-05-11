import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ZOO_TYPE_NAME, ZOO_TYPE_URI

from openapi_server.models.zoo import Zoo  # noqa: E501
from openapi_server import util

def zoos_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Zoo

    Gets a list of all instances of Zoo (more information in http://dbpedia.org/ontology/Zoo) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Zoo]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ZOO_TYPE_URI,
        rdf_type_name=ZOO_TYPE_NAME, 
        kls=Zoo)

def zoos_id_get(id):  # noqa: E501
    """Get a single Zoo by its id

    Gets the details of a given Zoo (more information in http://dbpedia.org/ontology/Zoo) # noqa: E501

    :param id: The ID of the Zoo to be retrieved
    :type id: str

    :rtype: Zoo
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ZOO_TYPE_URI,
        rdf_type_name=ZOO_TYPE_NAME, 
        kls=Zoo)
