import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FACTORY_TYPE_NAME, FACTORY_TYPE_URI

from openapi_server.models.factory import Factory  # noqa: E501
from openapi_server import util

def factorys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Factory

    Gets a list of all instances of Factory (more information in http://dbpedia.org/ontology/Factory) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Factory]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FACTORY_TYPE_URI,
        rdf_type_name=FACTORY_TYPE_NAME, 
        kls=Factory)

def factorys_id_get(id):  # noqa: E501
    """Get a single Factory by its id

    Gets the details of a given Factory (more information in http://dbpedia.org/ontology/Factory) # noqa: E501

    :param id: The ID of the Factory to be retrieved
    :type id: str

    :rtype: Factory
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FACTORY_TYPE_URI,
        rdf_type_name=FACTORY_TYPE_NAME, 
        kls=Factory)
