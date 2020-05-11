import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LIGAMENT_TYPE_NAME, LIGAMENT_TYPE_URI

from openapi_server.models.ligament import Ligament  # noqa: E501
from openapi_server import util

def ligaments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Ligament

    Gets a list of all instances of Ligament (more information in http://dbpedia.org/ontology/Ligament) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Ligament]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LIGAMENT_TYPE_URI,
        rdf_type_name=LIGAMENT_TYPE_NAME, 
        kls=Ligament)

def ligaments_id_get(id):  # noqa: E501
    """Get a single Ligament by its id

    Gets the details of a given Ligament (more information in http://dbpedia.org/ontology/Ligament) # noqa: E501

    :param id: The ID of the Ligament to be retrieved
    :type id: str

    :rtype: Ligament
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LIGAMENT_TYPE_URI,
        rdf_type_name=LIGAMENT_TYPE_NAME, 
        kls=Ligament)
