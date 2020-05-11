import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VEIN_TYPE_NAME, VEIN_TYPE_URI

from openapi_server.models.vein import Vein  # noqa: E501
from openapi_server import util

def veins_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Vein

    Gets a list of all instances of Vein (more information in http://dbpedia.org/ontology/Vein) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Vein]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VEIN_TYPE_URI,
        rdf_type_name=VEIN_TYPE_NAME, 
        kls=Vein)

def veins_id_get(id):  # noqa: E501
    """Get a single Vein by its id

    Gets the details of a given Vein (more information in http://dbpedia.org/ontology/Vein) # noqa: E501

    :param id: The ID of the Vein to be retrieved
    :type id: str

    :rtype: Vein
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VEIN_TYPE_URI,
        rdf_type_name=VEIN_TYPE_NAME, 
        kls=Vein)
