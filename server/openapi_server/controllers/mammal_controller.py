import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MAMMAL_TYPE_NAME, MAMMAL_TYPE_URI

from openapi_server.models.mammal import Mammal  # noqa: E501
from openapi_server import util

def mammals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Mammal

    Gets a list of all instances of Mammal (more information in http://dbpedia.org/ontology/Mammal) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Mammal]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MAMMAL_TYPE_URI,
        rdf_type_name=MAMMAL_TYPE_NAME, 
        kls=Mammal)

def mammals_id_get(id):  # noqa: E501
    """Get a single Mammal by its id

    Gets the details of a given Mammal (more information in http://dbpedia.org/ontology/Mammal) # noqa: E501

    :param id: The ID of the Mammal to be retrieved
    :type id: str

    :rtype: Mammal
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MAMMAL_TYPE_URI,
        rdf_type_name=MAMMAL_TYPE_NAME, 
        kls=Mammal)
