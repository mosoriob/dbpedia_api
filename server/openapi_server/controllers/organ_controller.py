import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ORGAN_TYPE_NAME, ORGAN_TYPE_URI

from openapi_server.models.organ import Organ  # noqa: E501
from openapi_server import util

def organs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Organ

    Gets a list of all instances of Organ (more information in http://dbpedia.org/ontology/Organ) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Organ]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ORGAN_TYPE_URI,
        rdf_type_name=ORGAN_TYPE_NAME, 
        kls=Organ)

def organs_id_get(id):  # noqa: E501
    """Get a single Organ by its id

    Gets the details of a given Organ (more information in http://dbpedia.org/ontology/Organ) # noqa: E501

    :param id: The ID of the Organ to be retrieved
    :type id: str

    :rtype: Organ
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ORGAN_TYPE_URI,
        rdf_type_name=ORGAN_TYPE_NAME, 
        kls=Organ)
