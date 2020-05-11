import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import REPTILE_TYPE_NAME, REPTILE_TYPE_URI

from openapi_server.models.reptile import Reptile  # noqa: E501
from openapi_server import util

def reptiles_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Reptile

    Gets a list of all instances of Reptile (more information in http://dbpedia.org/ontology/Reptile) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Reptile]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=REPTILE_TYPE_URI,
        rdf_type_name=REPTILE_TYPE_NAME, 
        kls=Reptile)

def reptiles_id_get(id):  # noqa: E501
    """Get a single Reptile by its id

    Gets the details of a given Reptile (more information in http://dbpedia.org/ontology/Reptile) # noqa: E501

    :param id: The ID of the Reptile to be retrieved
    :type id: str

    :rtype: Reptile
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=REPTILE_TYPE_URI,
        rdf_type_name=REPTILE_TYPE_NAME, 
        kls=Reptile)
