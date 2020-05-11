import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AMPHIBIAN_TYPE_NAME, AMPHIBIAN_TYPE_URI

from openapi_server.models.amphibian import Amphibian  # noqa: E501
from openapi_server import util

def amphibians_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Amphibian

    Gets a list of all instances of Amphibian (more information in http://dbpedia.org/ontology/Amphibian) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Amphibian]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AMPHIBIAN_TYPE_URI,
        rdf_type_name=AMPHIBIAN_TYPE_NAME, 
        kls=Amphibian)

def amphibians_id_get(id):  # noqa: E501
    """Get a single Amphibian by its id

    Gets the details of a given Amphibian (more information in http://dbpedia.org/ontology/Amphibian) # noqa: E501

    :param id: The ID of the Amphibian to be retrieved
    :type id: str

    :rtype: Amphibian
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AMPHIBIAN_TYPE_URI,
        rdf_type_name=AMPHIBIAN_TYPE_NAME, 
        kls=Amphibian)
